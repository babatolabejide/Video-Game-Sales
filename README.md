# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## Video Game Sales and Ratings Explorer

The Video Game Sales and Ratings Explorer is a comprehensive data analysis tool designed to explore and compare video game sales, ratings, and genre performance over time. The project leverages the Video Game Sales Dataset from Kaggle, which includes data on game sales, ratings, genres, and platforms.

Target Audience:
Game publishers, market analysts, and game developers.

Business Case:

Key Questions:
What factors influence game ratings?
Which genres have higher sales and ratings?

Value:
Provides actionable insights for strategic marketing and game development.
Supports data-driven decision-making in the gaming industry.

## Dataset Content

The project uses the Video Game Sales Dataset from Kaggle. The dataset contains:

* Game Sales: Global sales figures, regional sales data.
* Ratings: User and critic ratings.
* Genres: Classification of games into genres (e.g., Action, RPG, Strategy).
* Platforms: Data on platforms on which games were released.
* Additional Metrics: Release dates and publisher information.

## Business Requirements

* Market Insight: Identify key factors that drive game ratings and sales.
* Genre Performance: Understand which genres excel in both sales and ratings.
* Trend Analysis: Analyze how game sales and ratings have evolved over time.
* Strategic Guidance: Provide insights to support marketing and game development strategies.

## Hypotheses and Validation

Hypotheses:

1. Rating Influence Hypothesis: Games in certain genres (e.g., Action or RPG) consistently receive higher ratings due to better production quality or audience appeal.
2. Sales Correlation Hypothesis: There is a positive correlation between high ratings and high sales, indicating that better-reviewed games tend to sell more.

Validation Approach:

* Descriptive Analysis: Use summary statistics and visualizations to inspect rating distributions and sales figures.
* Visual Correlation: Generate scatter plots and heatmaps to assess correlations between sales, ratings, and genres.
* Trend Analysis: Use line plots to compare sales trends over time across genres.

## Project Plan

High-Level Steps:

1. Data Collection & Cleaning:
* Download and inspect the Video Game Sales Dataset.
* Clean the dataset (handle missing values, standardize column names, format data types).
2. Exploratory Data Analysis (EDA):
* Generate descriptive statistics and initial visualizations.
* Identify key variables and relationships.
3. Hypothesis Testing & Visualization:
* Create visualizations to test the hypotheses (line plots, bar plots, scatter plots, and heatmaps).
* Document findings and insights from the analysis.
4. Dashboard Design:
* Plan and design an interactive dashboard using Streamlit.
* Map business requirements to specific visualizations and interactive filters.
5. Documentation & Deployment:
* Document the project workflow in a comprehensive README and Jupyter Notebook.
* Deploy the dashboard on a cloud platform (e.g., Heroku) and update the live link.
## Data Management:
* Collection: Data obtained from Kaggle.
* Processing: Data cleaned and preprocessed using Pandas.
* Storage: Organized in dedicated folders (e.g., /data, /notebooks).
* Version Control: All code and documentation maintained with Git and pushed to GitHub.
## Research Methodologies:
* Exploratory Data Analysis: For initial insights and descriptive statistics.
* Visualization: To illustrate trends and correlations.
* Correlation Analysis: To test hypotheses without deploying complex machine learning models.
## Analysis Techniques Used
* Descriptive Statistics: Summarizing central tendencies and dispersions.
* Time-Series Analysis: Tracking sales and rating trends over time.
* Correlation Analysis: Using scatter plots and heatmaps to visualize relationships.
Visualization Libraries:
* Matplotlib & Seaborn: For static plots (bar plots, histograms).
* Plotly Express: For interactive visualizations (line plots, scatter plots).

Limitations:

* The analysis is limited by the available variables in the dataset.
* Certain niche genres may have sparse data, which could affect trend analysis.
* No advanced predictive modeling is included; the focus remains on visualizing and exploring correlations.

## Generative AI Tools Usage
* Ideation and Design:
Used ChatGPT to brainstorm visualization ideas and refine project hypotheses.
* Code Optimization:
Employed AI tools for code suggestions during data cleaning and visualization.
* Dashboard Layout:
Leveraged generative AI for feedback on user interface design and interactive elements.

## Ethical Considerations
* Data Privacy:
The dataset is publicly available on Kaggle and contains no personal information.
* Bias and Fairness:
Acknowledge potential biases in user ratings and genre classifications.
Document any limitations in the data that might impact the fairness of conclusions.
* Transparency:
All steps from data cleaning to visualization are fully documented to ensure reproducibility.

## Dashboard Design
Dashboard Pages and Content:

* Home Page:
Overview of the project purpose, key metrics, and executive summary.
* Sales Trends:
Interactive line plot displaying game sales trends over time.
* Genre Performance:
Bar plot showing average ratings by genre.
* Sales vs. Ratings:
Scatter plot comparing sales figures against game ratings.
* Correlation Analysis:
Heatmap illustrating correlations between sales, ratings, and other metrics.
* Filters and Widgets:
Options to filter data by release year, genre, and platform.

* Communication Strategy:
Visualizations are designed with clear labels and tooltips.
Narrative sections explain complex insights in simple terms for non-technical users.
Interactive elements enable deeper exploration for technical users.

## Unfixed Bugs and Limitations
* Interactive Rendering:
Some interactive plots may experience slower rendering on lower-end devices.
* Data Gaps:
Sparse data in certain niche genres may limit detailed trend analysis.
* Known Issues:
Minor filtering glitches in the dashboard are identified but will be addressed in future updates.

## Development Roadmap
* Challenges Faced:
Inconsistent data formatting and missing values.
Variability in data quality across genres and platforms.
* Strategies and Future Plans:
Continue refining data cleaning procedures.
Expand the dashboard with additional interactive features.
Explore advanced visualization techniques and additional datasets for broader insights.
* New Skills to Learn:
Advanced dashboard interactivity using Streamlit.
Cloud deployment strategies and optimization techniques.
Enhanced data visualization techniques using Plotly.

## Main Data Analysis Libraries
* Pandas: Data cleaning and manipulation.
* Matplotlib & Seaborn: Creating static visualizations.
* Plotly Express: Developing interactive visualizations.
* Streamlit: Building the interactive dashboard.
* Jupyter Notebook: Documenting the workflow and analysis.

## Credits and Acknowledgements

## Content and Media Sources:
* Dataset: Video Game Sales Dataset from Kaggle.
* Tutorials and Guidance: Code snippets and visualization techniques adapted from online tutorials, Kaggle kernels, and community resources.
* Generative AI Assistance: Ideas and code optimizations provided by ChatGPT and other AI tools.

Acknowledgements:
Special thanks to mentors, peers, and the data science community for their invaluable support and feedback throughout the project.