# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## Video Game Sales and Ratings Explorer

Video Game Sales Explorer is a comprehensive data analysis tool designed to streamline exploration, analysis, and visualization of video game sales data. The tool supports multiple data formats (e.g., CSV) and provides an intuitive interface for both novice and expert data analysts to uncover market trends, genre performance, and regional sales insights in the video game industry.

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

The dataset used is vgsales.csv, sourced from Kaggle (originally compiled by Gregory Smith). 
https://www.kaggle.com/datasets/gregorut/videogamesales
It contains 16,598 records of video game sales with the following columns:

* Rank: Sales rank
* Name: Game title
* Platform: Gaming platform (e.g., Wii, PS3)
* Year: Release year
* Genre: Game genre (e.g., Action, Sports)
* Publisher: Game publisher
* NA_Sales, EU_Sales, JP_Sales, Other_Sales, Global_Sales: Sales in millions by region and worldwide.

The dataset size is approximately 2 MB, well below the repository’s 100 GB limit. Note: It lacks ratings data (e.g., Metacritic scores), so hypotheses initially involving ratings have been adjusted to focus on sales-based insights.

## Business Requirements

1. Market Insight: Identify key markets and their sales dynamics to inform targeted marketing strategies.
2. Genre Performance: Determine which genres perform best in terms of sales to guide game development priorities.
3. Trend Analysis: Analyze sales trends over time to predict future market shifts.
4. Strategic Guidance: Provide actionable insights for stakeholders based on regional and genre-based sales patterns.

## Hypothesis and Validation

1. Hypothesis 1: Action and Sports genres have higher average global sales than other genres.

Validation: Calculate mean sales by genre and compare using a bar plot and statistical tests (e.g., t-test).

2. Hypothesis 2: Sales trends for top genres peak during specific console generations (e.g., 2005-2010).

Validation: Use a line plot to visualize sales over time for top genres and identify peaks.

3. Hypothesis 3: NA and EU sales are strongly correlated, unlike JP sales, due to market similarities.

Validation: Compute correlation coefficients and visualize with scatter and heatmap plots.

## Project Plan

High-Level Steps:

High-Level Steps
1. Data Collection: Obtain vgsales.csv from Kaggle.
2. Data Cleaning: Remove missing values, convert data types, and validate entries.
3. Exploratory Analysis: Generate summary statistics and initial visualizations.
4. Visualization: Create bar, line, scatter, and heatmap plots to address hypotheses and requirements.
5. Dashboard Development: Build an interactive Streamlit app with Plotly visualizations.
6. Deployment: Host the app on Heroku for stakeholder access.

Data Management

* Collection: Downloaded vgsales.csv and stored in /data folder.
* Processing: Cleaned data using Pandas (e.g., dropped NaN in Year and Publisher, converted Year to int) and saved as vgsales_cleaned.csv.
* Analysis: Performed in Jupyter Notebooks (notebooks/data_cleaning.ipynb) with version control via Git.
* Interpretation: Insights derived from visualizations and statistical measures (e.g., correlation).

Research Methodologies
* Why Chosen: Descriptive statistics and visualizations (bar, line, scatter, heatmap) are standard for exploratory data analysis, suitable for sales trends and correlations. Python libraries (Pandas, Seaborn) offer robust, reproducible analysis.
* Rationale: These methods align with the capstone’s emphasis on statistical application and visualization.

## Rationale to Map Business Requirements to Data Visualizations
1. Market Insight → Scatter Plot (NA vs. EU Sales) and Heatmap (Regional Correlations):
Rationale: Reveals sales relationships across regions, guiding market prioritization.
2. Genre Performance → Bar Plot (Average Sales by Genre):
Rationale: Highlights top genres by sales, informing development focus.
3. Trend Analysis → Line Plot (Sales Over Time by Genre):
Rationale: Tracks historical trends, aiding in forecasting.
4. Strategic Guidance → All Plots:
Rationale: Combined insights offer a holistic view for decision-making.

## Analysis Techniques Used
1. Descriptive Statistics: Mean, sum, and correlation (e.g., df.describe(), corr()) to summarize sales.
* Limitations: Assumes data completeness; missing years/publishers were dropped.
* Alternatives: Imputation for missing values (not used due to small percentage).

2. Visualization: Bar, line, scatter, and heatmap plots via Seaborn/Matplotlib.
* Limitations: Static plots lack interactivity; addressed by planning Plotly in dashboard.
3. Structure: Sequential—cleaning, then exploration, then visualization—to ensure data quality before analysis.
* Justification: Prevents garbage-in, garbage-out; aligns with LO5 (data management).
4. Data Limitations: No ratings data; shifted focus to sales correlations.
* Alternative: Plan to source ratings later (e.g., Metacritic API).

## Use of Generative AI
* Ideation: Grok (xAI) suggested hypotheses and plot types based on dataset.
* Design Thinking: Proposed mapping business requirements to visualizations.
* Code Optimization: Provided cleaned, efficient Pandas code and visualization snippets.

## Ethical Considerations
* Data Privacy: Public dataset, no personal data (LO6.1 compliant).
* Bias: Sales overrepresent NA/EU markets; JP and smaller regions underrepresented.
* Mitigation: Noted in insights; future inclusion of diverse datasets planned.
* Fairness: Avoided overgeneralizing genre success due to regional cultural differences.
* Legal: No GDPR issues; data is aggregated and publicly sourced.

## Dashboard Design
Pages and Content
1. Home Page:
* Text Block: Project overview and dataset description.
* Image: Video game sales trend graphic (placeholder).
2. Sales by Genre:
* Bar Plot (Plotly): Interactive average sales by genre with hover details.
* Dropdown: Filter by region (NA, EU, JP, Other).
3. Sales Trends:
* Line Plot (Plotly): Sales over time for top genres.
* Slider: Select year range.
4. Regional Analysis:
* Scatter Plot (Plotly): NA vs. EU sales by genre.
* Heatmap (Plotly): Correlation across regions.
* Checkbox: Toggle genres to include.

Communication to Audiences
Technical: Heatmap and scatter plots with correlation stats for data scientists.
Non-Technical: Bar and line plots with clear titles and legends for stakeholders.

## Unfixed Bugs and Limitations
* Interactive Rendering:
Some interactive plots may experience slower rendering on lower-end devices.
* Data Gaps:
Sparse data in certain niche genres may limit detailed trend analysis.
* Known Issues:
Minor filtering glitches in the dashboard are identified but will be addressed in future updates.

## Knowledge Gaps
* Gap: Limited Streamlit experience.
* Addressed: Planned tutorials and Grok assistance for dashboard setup.

## Development Roadmap
Challenges and Strategies

* Challenge: Missing ratings data.
* Strategy: Refocused on sales; planned future augmentation.
* Challenge: Visualization complexity for dashboard.
* Strategy: Used Grok to prototype plots, will learn Plotly.

Next Skills/Tools
* Learn Plotly for interactive visualizations.
* Explore Streamlit for dashboard deployment.
* Study web scraping for ratings data.

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
* Generative AI Assistance: Ideas and code optimizations provided by Grok.

Acknowledgements:
Special thanks to Vasilica Pavaloi, Niel McEwen and my peers for their invaluable support and feedback throughout the project.