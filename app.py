import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

# Set page configuration with dark theme
st.set_page_config(page_title="Video Game Sales Explorer", layout="wide", initial_sidebar_state="expanded")

# Apply dark theme via custom CSS
st.markdown("""
    <style>
    body {
        background-color: #1E1E1E;
        color: white;
    }
    .stApp {
        background-color: #1E1E1E;
    }
    h1, h2, h3, h4, h5, h6, p, label {
        color: white !important;
    }
    .stSidebar {
        background-color: #2A2A2A;
    }
    </style>
""", unsafe_allow_html=True)

# Load data with error handling
@st.cache_data
def load_data():
    try:
        # Use os.path.join to construct the path dynamically
        file_path = os.path.join(os.path.dirname(__file__), 'data', 'vgsales_cleaned.csv')
        if not os.path.exists(file_path):
            st.error("Error: 'vgsales_cleaned.csv' not found in the data folder. Please check the file path or upload the file.")
            return pd.DataFrame()  # Return empty DataFrame as fallback
        return pd.read_csv(file_path)
    except FileNotFoundError as e:
        st.error("FileNotFoundError: The dataset 'vgsales_cleaned.csv' could not be loaded. Check the file path and repository.")
        return pd.DataFrame()  # Return empty DataFrame as fallback

df = load_data()

# Sidebar filters
st.sidebar.header("Filters")
genre_filter = st.sidebar.multiselect("Select Genres", options=df['Genre'].unique(), default=df['Genre'].unique())
year_range = st.sidebar.slider("Select Year Range", min_value=int(df['Year'].min()), max_value=int(df['Year'].max()), 
                               value=(int(df['Year'].min()), int(df['Year'].max())))

# Filter data
df_filtered = df[(df['Genre'].isin(genre_filter)) & 
                 (df['Year'] >= year_range[0]) & (df['Year'] <= year_range[1])]

# Page navigation
page = st.sidebar.radio("Go to", ["Home", "Sales by Genre", "Sales Trends", "Regional Analysis"])

# Home Page
if page == "Home":
    st.title("Video Game Sales Explorer")
    st.markdown("""
        ### Welcome!
        This dashboard explores video game sales trends using the `vgsales.csv` dataset. 
        - **Dataset**: Contains 16,598 records of global and regional sales by genre, platform, and year.
        - **Goal**: Provide insights into market trends, genre performance, and regional dynamics.
        - **Features**: Interactive plots with genre and year filters.
        Use the sidebar to navigate and filter data!
    """)
    st.image("data/videogames.png", caption="Video Game Sales Graphic")  # Update with the correct path to your image

# Sales by Genre Page (Bar Plot)
elif page == "Sales by Genre":
    st.subheader("Average Sales by Genre")
    genre_sales = df_filtered.groupby('Genre')['Global_Sales'].mean().reset_index()
    fig_bar = px.bar(genre_sales, x='Genre', y='Global_Sales', title="Average Global Sales by Genre",
                     color='Genre', color_discrete_sequence=px.colors.qualitative.Dark24)
    fig_bar.update_layout(plot_bgcolor='rgba(0, 0, 0, 0.9)', paper_bgcolor='rgba(0, 0, 0, 0.9)',
                         font_color='white', title_font_color='white')
    st.plotly_chart(fig_bar, use_container_width=True)
    st.markdown("""
        **Insight**: This bar plot shows the average global sales per genre. Use the genre filter to focus on specific categories.
    """)

# Sales Trends Page (Line Plot)
elif page == "Sales Trends":
    st.subheader("Sales Trends Over Time")
    # Select top 5 genres by total sales to reduce clutter
    top_genres = df_filtered.groupby('Genre')['Global_Sales'].sum().nlargest(5).index
    df_top = df_filtered[df_filtered['Genre'].isin(top_genres)]

    # Aggregate sales by year and genre to smooth the plot
    df_trends = df_top.groupby(['Year', 'Genre'])['Global_Sales'].sum().reset_index()

    # Handle outliers by capping extreme values (e.g., Sports spike)
    threshold = df_trends['Global_Sales'].quantile(0.95)  # Cap at 95th percentile
    df_trends['Global_Sales'] = df_trends['Global_Sales'].clip(upper=threshold)

    # Create line plot
    fig_line = px.line(df_trends, x='Year', y='Global_Sales', color='Genre',
                       title="Sales Trends by Top 5 Genres Over Time",
                       color_discrete_sequence=px.colors.qualitative.Dark24)
    fig_line.update_layout(plot_bgcolor='rgba(0, 0, 0, 0.9)', paper_bgcolor='rgba(0, 0, 0, 0.9)',
                          font_color='white', title_font_color='white')
    fig_line.update_traces(line=dict(width=3))  # Thicker lines for visibility
    st.plotly_chart(fig_line, use_container_width=True)
    st.markdown("""
        **Insight**: This line plot shows sales trends for the top 5 genres. Use the year slider to zoom into specific periods. Outliers are capped for better readability.
    """)

# Regional Analysis Page (Scatter and Heatmap)
elif page == "Regional Analysis":
    st.subheader("Regional Sales Analysis")
    
    # Scatter Plot: NA vs. EU Sales
    st.markdown("### NA vs. EU Sales by Genre")
    fig_scatter = px.scatter(df_filtered, x='NA_Sales', y='EU_Sales', color='Genre', size='Global_Sales',
                             title="NA vs. EU Sales by Genre", hover_data=['Name'],
                             color_discrete_sequence=px.colors.qualitative.Dark24)
    fig_scatter.update_layout(plot_bgcolor='rgba(0, 0, 0, 0.9)', paper_bgcolor='rgba(0, 0, 0, 0.9)',
                             font_color='white', title_font_color='white')
    st.plotly_chart(fig_scatter, use_container_width=True)
    st.markdown("""
        **Insight**: This scatter plot explores the relationship between NA and EU sales, with point size reflecting global sales.
    """)

    # Heatmap: Correlation of Sales Across Regions
    st.markdown("### Regional Sales Correlation")
    corr_matrix = df_filtered[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']].corr()
    fig_heatmap = px.imshow(corr_matrix, text_auto=True, color_continuous_scale='RdBu_r',
                            title="Correlation Heatmap of Sales by Region")
    fig_heatmap.update_layout(plot_bgcolor='rgba(0, 0, 0, 0.9)', paper_bgcolor='rgba(0, 0, 0, 0.9)',
                             font_color='white', title_font_color='white')
    st.plotly_chart(fig_heatmap, use_container_width=True)
    st.markdown("""
        **Insight**: This heatmap shows correlations between regional sales. High correlations (e.g., NA and EU) suggest market similarities.
    """)