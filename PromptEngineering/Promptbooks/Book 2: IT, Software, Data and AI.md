# Coding & Debugging

## Prompt 1 — Code Review & Optimisation Plan

`
"You are a senior software engineer with expertise in [programming language/framework]. I have a codebase for a [type of application — e.g., e-commerce site, chatbot, mobile app] that works but runs slowly.
Review the code for:
`

`````
1. Inefficient loops or redundant logic.

2. Poor memory management.

3. Opportunities to replace custom code with standard libraries.

4. Security vulnerabilities (SQL injection, XSS).

5. Best practices for scalability.
`````

`
Provide output in 2 sections: a table of issues (with line numbers & problem description) and an optimised code snippet for each fix."
`

## Prompt 2 — Bug Reproduction & Fix Documentation

`
"You are a QA (Quality Assurance) automation tester and developer. I have a bug where [describe bug behaviour] in my [framework/app type].
`

`
Create a debugging report that includes:
`

`````
1. Exact steps to reproduce the bug.

2. Screenshots or logs showing the issue.

3. The suspected root cause in the code.

4. The corrected code segment.

5. Unit test cases to ensure the bug doesn’t reappear.
`````
`
Output in debugging report format with code blocks."
`

## Prompt 3 — Multi-Language Code Conversion

`
"You are a cross-platform developer. Convert my [programming language] code for [feature/function] into [target language], ensuring:
`

`````
1. Exact feature parity.

2. Proper syntax & library usage in the target language.

3. Equivalent performance or better.

4. Inline comments explaining logic.

5. A quick performance test script in the target language.
`````

`
Output in side-by-side original vs converted code format."
`

## Prompt 4 — Algorithm Efficiency Upgrade

`
"You are a competitive programming expert. My current [sorting/searching/matching/etc.] algorithm in [language] works but is slow on large datasets.
`

`
Optimise it by:
`

````
1. Suggesting a faster algorithm (e.g., replacing bubble sort with merge sort).

2. Explaining time & space complexity differences.

3. Providing optimised code.

4. Writing performance benchmarks comparing both versions.
````

`
Output in comparative performance report format."
`

## Prompt 5 — Debugging API Integration Issues

`
"You are an API integration specialist. My app in [language/framework] fails to fetch data from [API name] correctly.
Diagnose the problem by:
`

`````
1. Reviewing my API request code.

2. Checking authentication & endpoint issues.

3. Suggesting correct request format with example.

4. Adding error handling for network failures.

5. Writing a test function to validate the fix.
`````

`
Output in debugging log + corrected code block."
`

## Prompt 6 — Code Refactoring for Readability & Maintainability

`
"You are a senior code architect. Refactor my [language/framework] code for [feature/function] so it is:
`

`````
1. Easier to read with proper indentation & naming conventions.

2. Modularised into reusable functions or classes.

3. Documented with meaningful comments.

4. Compliant with [specific coding standard, e.g., PEP8 for Python].

5. Unit tested to ensure functionality remains unchanged.
`````

`
Output in before/after code comparison format with a change log."
`

## Prompt 7 — Legacy Code Modernisation Plan

`
"You are a legacy systems upgrade specialist. My [old programming language or framework] code needs to be upgraded to [modern equivalent] while preserving functionality.
`

`
Include:
`

`````
1. Identification of outdated functions/libraries.

2. Recommended replacements & modern equivalents.

3. Compatibility concerns with the new environment.

4. Performance benefits after modernisation.

5. Step-by-step migration plan with testing checkpoints.
`````

`
Output in legacy-to-modern migration report format."
`

## Prompt 8 — Continuous Integration (CI) Debugging Setup

`
"You are a DevOps engineer. Configure a CI pipeline for my [language/framework] project to automatically run code linting, unit tests, and integration tests whenever code is pushed.
`

`
Include:
`

`````
1. Recommended CI tool (GitHub Actions, Jenkins, GitLab CI).

2. Pipeline configuration script.

3. Test coverage reporting setup.

4. Common CI errors & how to fix them.

5. Notification integration (Slack/Email) for failed builds.
`````

`
Output in pipeline YAML file + setup guide."
`

## Prompt 9 — Memory Leak Detection & Fix

`
"You are a performance optimisation engineer. Analyse my [language/framework] application for memory leaks and:
`

`````
1. Identify possible causes from code structure.

2. Suggest profiling tools (Valgrind, Perf, Chrome DevTools).

3. Provide a step-by-step method to reproduce memory growth.

4. Fix the leak with corrected code examples.

5. Suggest long-term prevention strategies.
`````

`
Output in diagnostic report + corrected code samples."
`

## Prompt 10 — Multi-Threading Bug Resolution

`
"You are a concurrency programming specialist. My [language/framework] application faces race conditions and deadlocks.
`

`
Include:
`

`````
1. Detailed explanation of the issue.

2. Steps to identify which thread is causing the block.

3. Corrected thread-safe code.

4. Recommended locking or async patterns.

5. Performance benchmarks after fix.
`````

`
Output in bug analysis + updated code format."
`

## Prompt 11 — Automated Unit Test Generation

`
"You are a test automation engineer. Write automated unit test scripts for my [language/framework] code covering [feature/function].
`

`
Include:
`

`````
1. Test cases for normal, boundary, and error conditions.

2. Assertions for expected output.

3. Mock data creation.

4. Code coverage percentage target (e.g., >80%).

5. How to run tests in CI/CD pipeline.
`````

`
Output in ready-to-run test script format."
`

## Prompt 12 — SQL Query Debugging & Optimisation

`
"You are a database performance engineer. Optimise my slow SQL queries for [database type: MySQL, PostgreSQL, etc.].
`

`
Include:
`

`````
1. Query execution plan analysis.

2. Indexing strategy.

3. Query rewriting for speed.

4. Caching recommendations.

5. Before/after execution time comparison.
`````

`
Output in query optimisation report with revised SQL statements."
`

## Prompt 13 — Cross-Browser Bug Fix Plan

`
"You are a front-end debugging expert. My web app works on Chrome but fails in Firefox & Safari.
`

`
Include:
`

`````
1. List of browser compatibility issues.

2. Code fixes using cross-browser safe APIs.

3. CSS vendor prefixing guide.

4. Polyfill recommendations for unsupported features.

5. Testing checklist for all major browsers.
`````

`
Output in browser compatibility report + fixed code snippets."
`

## Prompt 14 — API Rate Limit Error Resolution

`
"You are an API performance consultant. My app hits rate limits when fetching data from [API name].
`

`
Include:
`

`````
1. How to detect rate limit headers.

2. Backoff strategies & caching techniques.

3. Batch request examples.

4. Code modifications for retry logic.

5. Test scenarios to confirm the fix.
`````

`
Output in rate limit handling guide + updated code."
`

## Prompt 15 — Deployment Bug Fix Checklist

`
"You are a deployment engineer. My application works locally but fails in production.
`

`
Include:
`

`````
1. Environment variable checks.

2. Dependency version mismatches.

3. Server configuration issues.

4. Build process verification.

5. Automated rollback setup.
`````

`
Output in deployment debugging checklist format."
`

## Prompt 16 — Version Control Conflict Resolution

`
"You are a Git (Version Control) expert. Resolve merge conflicts in my [repository name] while ensuring no functionality loss.
`

`
Include:
`

````
1. Step-by-step conflict resolution process.

2. Commit best practices to avoid future issues.

3. Branch management guidelines.

4. Git command examples for common scenarios.
````

`
Output in merge resolution guide with Git commands."
`

## Prompt 17 — Security Vulnerability Patch Plan

`
"You are a cybersecurity code auditor. Review my [language/framework] code for vulnerabilities like SQL injection, XSS, and CSRF.
`

`
Include:
`

````
1. Vulnerability list with risk levels.

2. Code patches with secure alternatives.

3. OWASP (Open Web Application Security Project) best practice checklist.

4. Security testing tools list.
````

`
Output in vulnerability report + patched code samples."
`

## Prompt 18 — Cloud Function Debugging Guide

`
"You are a cloud application developer. Debug my [AWS Lambda / Google Cloud Function / Azure Function] which is failing intermittently.
`

`
Include:
`

`````
1. Log analysis methods.

2. Error pattern detection.

3. Code changes for reliability.

4. Testing with local emulators.

5. Deployment steps after fix.
`````

`
Output in debugging flowchart + corrected function code."
`

## Prompt 19 — Mobile App Crash Analysis

`
"You are a mobile app debugging expert. Analyse my [Android/iOS] app for crash reports related to [feature/function].
`

`
Include:
`

`````
1. Crash log interpretation.

2. Root cause identification.

3. Code corrections.

4. Device-specific fixes.

5. Testing plan for all OS versions.
`````

`
Output in crash report + updated code block."
`

## Prompt 20 — Real-Time Error Monitoring Setup

`
"You are a site reliability engineer. Set up a real-time error tracking system for my [language/framework] app.
`

`
Include:
`

`````
1. Recommended monitoring tools (Sentry, New Relic, Datadog).

2. Setup steps for integration.

3. Error categorisation for alerts.

4. Dashboard layout suggestions.

5. Weekly reporting format.
`````

`
Output in tool setup guide + dashboard screenshot mockup."
`

## Prompt 21 — Data Processing Script Debugging

`
"You are a data engineer. My Python ETL (Extract, Transform, Load) script fails at the transformation stage.
`

`
Include:
`

`````
1. Step-by-step debugging for data type mismatches.

2. Handling null values & schema changes.

3. Logging setup for error tracking.

4. Optimised data transformation logic.

5. Unit tests for validation.
`````

`
Output in debugging report + corrected script."
`

## Prompt 22 — Infinite Loop Prevention in Code

`
"You are a software safety expert. Analyse my [language] code for infinite loop risks and fix them.
`

`
Include:
`

````
1. Detection of loops without termination conditions.

2. Corrected loop conditions.

3. Safeguards to prevent reoccurrence.

4. Performance benchmarks after fix.
````

`
Output in before/after code format."
`

## Prompt 23 — Automated Code Documentation Generator

`
"You are a documentation automation consultant. Set up an auto-documentation system for my [language/framework] project.
`

`
Include:
`

````
1. Recommended tools (e.g., JSDoc, Sphinx).

2. Integration into CI/CD pipeline.

3. Style guide for consistent doc formatting.

4. Sample generated documentation.
````

`
Output in documentation setup guide + example output."
`

## Prompt 24 — Debugging Scheduler & Cron Job Failures

`
"You are a backend engineer. My scheduled tasks in [language/framework] fail intermittently.
`

`
Include:
`

`````
1. Log analysis to find failure points.

2. Corrected cron expressions.

3. Error handling logic.

4. Monitoring alerts setup.

5. Retry mechanism.
`````

`
Output in debugging report + fixed scheduling script."
`

## Prompt 25 — Codebase Technical Debt Reduction Plan

`
"You are a senior software architect. Analyse my [language/framework] codebase for technical debt and create a 3-month cleanup roadmap.
`

`
Include:
`

`````
1. List of outdated dependencies.

2. Code smells & fixes.

3. Testing coverage improvement.

4. Refactoring priorities.

5. Risk mitigation plan.
`````

`
Output in technical debt report + phased action plan."
`

# Data Analysis & Visualization

## Prompt 1 — Full Exploratory Data Analysis (EDA) with Actionable Insights

`
"You are a Senior Data Analyst with expertise in Python (Pandas, NumPy, Matplotlib, Seaborn) and data storytelling. I have a dataset in CSV format containing sales data for an Indian retail chain (2018–2024) with 50,000 rows and 12 columns (date, location, category, units sold, price, discount, etc.).
`

`
Your task:
`

`````
1. Import and inspect the dataset to understand structure, data types, and column meanings.

2. Generate summary statistics for both numerical and categorical columns, highlighting anomalies.

3. Detect missing values, quantify them column-wise, and suggest domain-specific imputation or removal strategies.

4. Identify outliers using both statistical (Z-score, IQR) and visual (boxplots) methods, explaining potential business causes.

5. Create a correlation heatmap for numerical features and explain the top 5 strongest relationships in simple business terms.

6. Provide at least 3 actionable business insights and possible next analytical steps.
`````

`
Output format: A Jupyter Notebook with fully commented code, inline plots, and a concluding Markdown section explaining insights in non-technical language."
`

## Prompt 2 — Interactive KPI Dashboard for Decision-Makers

`
"You are a Business Intelligence (BI) Dashboard Expert skilled in Power BI, Tableau, and Google Data Studio. I have quarterly sales data for multiple product categories in India for the last 5 years.
`

`
Your task:
`

`````
1. Identify 5–7 key performance indicators (KPIs) relevant to retail business health (e.g., total revenue, gross margin, average order value, conversion rate).

2. Design an interactive dashboard layout showing KPIs as cards at the top, trend charts in the middle, and filters (by time, category, location) on the side.

3. Include drill-down capability so a user can click on a KPI and view detailed breakdowns by category, region, or month.

4. Add a geographic heatmap showing sales distribution across states, with hover tooltips.

5. Include an export-to-PDF function for monthly reporting.
`````

`
Output format: Provide a step-by-step dashboard build guide (tool-agnostic), a mockup diagram of the dashboard, and sample formulas for KPI calculations."
`

## Prompt 3 — Predictive Sales Forecasting with Model Comparison

`
"You are a Data Scientist specialising in forecasting. I have monthly sales data for an e-commerce platform from January 2018 to December 2024.
`

`
Your task:
`

`````
1. Perform time-series decomposition to analyse trend, seasonality, and residual components.

2. Build at least two forecasting models (ARIMA/SARIMA and Facebook Prophet).

3. Compare model performance using RMSE (Root Mean Squared Error) and MAPE (Mean Absolute Percentage Error).

4. Plot actual vs predicted sales for both models and highlight differences.

5. Provide recommendations for which model to deploy, along with a 12-month sales forecast.
`````

`
Output format: A Python Jupyter Notebook with all code, plots, and a Markdown cell comparing models with business-friendly explanations."
`

## Prompt 4 — Automated Data Cleaning and Preprocessing Script

`
"You are a Data Preprocessing Automation Specialist skilled in Python and Pandas. I have a CSV file containing a mix of numerical, categorical, and datetime fields, with missing values and inconsistent formats.
`

`
Your task:
`

`````
1. Write a reusable Python script to detect and handle missing values using mean/median/mode or forward-fill/backward-fill depending on the column type.

2. Remove duplicate rows and flag near-duplicates for manual review.

3. Normalise numerical columns (min-max or z-score scaling) and encode categorical columns (label or one-hot encoding as appropriate).

4. Convert date columns to proper datetime format and extract features (day, month, year, day-of-week).

5. Save the cleaned dataset to a new CSV file with a timestamped filename.
`````

`
Output format: A fully commented Python script that can be reused for different datasets, with clear function definitions."
`

## Prompt 5 — Business Data Storytelling for Stakeholder Reports

`
"You are a Business Data Storyteller with experience in creating executive summaries from analytical results. I have analysed customer purchase behaviour for my online store and want to present findings to the leadership team.
`

`
Your task:
`

`````
1. Frame the analysis as a story — starting with the problem, key findings, and implications.

2. Select only the 5–7 most impactful visuals from the analysis, ensuring they are simple and easy to understand.

3. Explain each chart in 1–2 sentences highlighting what matters for the business.

4. Conclude with 3 actionable recommendations, each tied to a business outcome (e.g., revenue growth, cost saving).

5. Create a 2-slide PowerPoint layout that can be used in a leadership meeting.
`````

`
Output format: A concise text storyboard + slide content that a non-technical executive can understand at a glance."
`

## Prompt 6 — Real-Time Data Monitoring and Alerts

`
"You are a Real-Time Data Monitoring Specialist skilled in tools like Grafana, Kibana, and Power BI Streaming Dataflows. I operate a logistics company with live GPS and delivery data flowing in every 15 seconds.
`

`
Your task:
`

`````
1. Design a real-time dashboard that displays vehicle location, delivery status, and delays in near real-time.

2. Implement colour-coded alerts for deliveries delayed beyond SLA (Service Level Agreement) thresholds.

3. Add trend visualisations for daily delivery count, average delivery time, and % on-time rate.

4. Integrate automated alerts via email and SMS for key managers when KPIs cross thresholds.

5. Ensure the system can handle data spikes (e.g., festival season).
`````

`
Output format: A visual architecture diagram + tool integration plan + example SQL queries for alert generation."
`

## Prompt 7 — Sentiment Analysis of Customer Feedback

`
"You are an NLP (Natural Language Processing) Specialist with expertise in Python libraries like NLTK, SpaCy, and Transformers. I have 50,000 customer reviews collected over 2 years.
`

`
Your task:
`

`````````
1. Clean and preprocess the text (remove stopwords, lemmatise, handle emojis).

2. Classify sentiment into positive, neutral, and negative categories using a pre-trained BERT model.

3. Create visualisations:

    1. Sentiment distribution pie chart.

    2. Monthly sentiment trend line chart.

    3. Word cloud for each sentiment category.

5. Identify top 5 positive and top 5 negative themes with example reviews.

6. Provide actionable recommendations for product/service improvement based on sentiment patterns.
`````````

`
Output format: A Jupyter Notebook with code, charts, and a Markdown insights summary."
`

## Prompt 8 — Comparative Category Performance Report

`
"You are a Business Performance Analyst. I have category-wise sales data for 10 product categories over the last 3 years.
`

`
Your task:
`

`````
1. Calculate YoY (Year-over-Year) and MoM (Month-over-Month) growth rates for each category.

2. Rank categories based on revenue, profit margin, and units sold.

3. Create a dashboard view showing category trends side-by-side.

4. Highlight top 3 performing categories and bottom 3 lagging categories.

5. Suggest category-level actions to boost sales and margins for underperformers.
`````

`
Output format: A comparative analysis table + dashboard layout mockup + 1-page action plan."
`

## Prompt 9 — Correlation and Causation Testing

`
"You are a Data Scientist with a focus on statistical inference. I have a dataset on marketing spend (TV, social media, influencer, print) and corresponding sales figures.
`

`
Your task:
`

`````
1. Calculate correlation coefficients for each marketing channel vs sales.

2. Perform hypothesis testing to check statistical significance (p-values).

3. Run a multiple regression analysis to see which channels predict sales best.

4. Visualise results using scatter plots and regression lines.

5. Provide a plain-language explanation of findings for non-technical stakeholders.
`````

`
Output format: Jupyter Notebook with plots + regression output table + simplified insights brief."
`

## Prompt 10 — Customer Churn Prediction and Retention Strategy

`
"You are a Customer Analytics Expert specialising in churn modelling. I have SaaS customer data including sign-up date, usage frequency, support tickets, and payment history.
`

`
Your task:
`

`````
1. Define churn for my business context (e.g., inactive for 60 days).

2. Engineer predictive features from usage and payment history.

3. Build a classification model (Logistic Regression, Random Forest, or XGBoost) to predict churn probability.

4. Evaluate using accuracy, precision, recall, and ROC-AUC.

5. Suggest retention strategies for the top 20% at-risk customers.
`````

`
Output format: Python Notebook with code + confusion matrix + strategic retention plan."
`

## Prompt 11 — Data Visualization Best Practices Guide

`
"You are a Data Visualization Trainer. Prepare a best practices guide for visualising financial performance data for stakeholders.
`

`
Your task:
`

`````
1. Recommend which chart types to use for time-series, category comparison, and part-to-whole analysis.

2. Suggest an accessible, colour-blind-friendly palette.

3. Explain how to avoid misleading scales and data distortion.

4. Include 3 examples of excellent visualisations and explain why they work.

5. Provide 3 poor visualisation examples and show corrected versions.
`````

`
Output format: A 5-page PDF guide with do’s and don’ts + visual examples."
`

## Prompt 12 — Multi-Dataset Integration Workflow

`
"You are a Data Integration Specialist skilled in ETL (Extract, Transform, Load) processes. I have three datasets:
`

```
1. Customer demographics (Excel)

2. Purchase history (CSV)

3. Web analytics data (Google Analytics export)
```

`
Your task:
`

`````
1. Identify common keys for merging datasets.

2. Clean and standardise column formats and naming.

3. Join datasets into a master table.

4. Perform initial descriptive analysis on combined data.

5. Suggest 3 insights achievable only after combining data.
`````

`
Output format: Python Notebook with ETL code + final merged dataset snapshot + insight summary."
`

## Prompt 13 — Interactive Geo-Spatial Sales Mapping

`
"You are a GIS (Geographic Information Systems) Analyst. I have state-wise sales data for India for the past 12 months.
`

`
Your task:
`

`````
1. Create an interactive map showing sales density using a colour gradient.

2. Add filters for month, product category, and sales rep.

3. Display state-level tooltips with key KPIs (revenue, units sold, growth rate).

4. Enable comparison mode for two selected states.

5. Provide export options (PNG, PDF).
`````

`
Output format: Dashboard implementation guide + sample data visualisation screenshot."
`

## Prompt 14 — Industry Benchmark Comparison with Gap Analysis

`
"You are a Market Intelligence Analyst specialising in competitive benchmarking. I have my company’s quarterly performance metrics for revenue, gross margin, and customer acquisition rate, and I have benchmark data for top 5 competitors.
`

`
Your task:
`

`````
1. Normalise all data for fair comparison (e.g., currency conversion, adjusting for fiscal year differences).

2. Create comparative bar charts showing my company vs each competitor for each KPI (Key Performance Indicator).

3. Calculate % variance from industry average for each KPI.

4. Identify areas where my company is above average and where it’s lagging.

5. Provide 5 targeted recommendations to close performance gaps.
`````

`
Output format: A 2-page PDF competitive report with visual comparisons, an executive summary, and a prioritised action list."
`

## Prompt 15 — Data Pipeline Performance Optimisation Plan

`
"You are a Data Engineer experienced in optimising ETL (Extract, Transform, Load) pipelines for speed and efficiency. I have a nightly pipeline that ingests sales, inventory, and customer data into a central warehouse.
`

`
Your task:
`

`````
1. Profile the current pipeline to identify slow queries, inefficient joins, and bottleneck processes.

2. Recommend improvements in query optimisation, indexing, and caching.

3. Suggest parallelisation or batch processing strategies to reduce runtime.

4. Propose monitoring tools to track pipeline health and error rates.

5. Provide an example optimised SQL query and ETL script snippet.
`````

`
Output format: A technical optimisation plan with a “before vs after” runtime projection chart and sample code."
`

## Prompt 16 — Social Media Engagement Analytics Dashboard

`
"You are a Digital Analytics Expert skilled in API integrations and BI dashboarding. I have social media engagement data from Facebook, Instagram, and LinkedIn for the past 12 months.
`

`
Your task:
`

`````
1. Create a unified dashboard showing platform-wise engagement metrics (likes, comments, shares, saves).

2. Add a filter to view engagement by post type (video, carousel, single image, story).

3. Highlight top 10 performing posts across all platforms with engagement breakdown.

4. Add follower growth trend lines for each platform.

5. Include an insights section suggesting which content format drives the highest engagement.
`````

`
Output format: Dashboard wireframe + API integration guide + engagement insights report."
`

## Prompt 17 — Real Estate Market Analysis with Investment Insights

`
"You are a Real Estate Data Analyst with expertise in property market trends. I have a dataset of property sales in [city] for the last 5 years with columns for location, property type, size, sale price, and date.
`

`
Your task:
`

`````
1. Analyse price trends by property type (apartment, villa, plot).

2. Map high-growth neighbourhoods using price appreciation over time.

3. Identify seasonality patterns in sales volume.

4. Calculate ROI projections for top 5 emerging areas.

5. Provide investment recommendations for buyers targeting high rental yield vs capital appreciation.
`````

`
Output format: A PDF market report with heatmaps, trend charts, and a 1-page “Investor Recommendations” summary."
`

## Prompt 18 — Healthcare Operational Efficiency Analysis

`
"You are a Healthcare Data Analyst working on hospital efficiency improvement. I have anonymised patient visit data, bed occupancy records, and treatment timelines for the past 2 years.
`

`
Your task:
`

`````
1. Calculate average patient wait time, treatment time, and discharge time.

2. Create bed occupancy rate visualisations by department.

3. Identify peak patient inflow periods and staffing shortages.

4. Suggest scheduling optimisations to reduce bottlenecks.

5. Recommend operational changes to improve patient throughput without compromising care quality.
`````

`
Output format: A dashboard layout plan + operational improvement report."
`

## Prompt 19 — Sales Funnel Drop-off Analysis

`
"You are a Marketing Data Analyst focused on conversion rate optimisation. I have e-commerce funnel data for the last quarter showing visits, product views, add-to-cart events, checkout starts, and purchases.
`

`
Your task:
`

`````
1. Calculate conversion rates for each funnel stage.

2. Identify the stage with the highest drop-off rate and quantify the loss in potential revenue.

3. Analyse patterns in drop-off by device type, browser, and traffic source.

4. Suggest at least 5 tactics to improve conversions at the weakest stage.

5. Provide a visual funnel chart showing current vs projected performance if improvements are implemented.
`````

`
Output format: A funnel analysis dashboard + improvement recommendation document."
`

## Prompt 20 — Education Performance Dashboard for Institutions

`
"You are an Education Analytics Specialist. I have school-level student performance data for grades, attendance, and extracurricular participation across multiple branches.
`

`
Your task:
`

`````
1. Create visualisations showing average performance by subject and grade level.

2. Add attendance heatmaps highlighting periods of low attendance.

3. Identify correlations between extracurricular participation and academic performance.

4. Highlight top 5 branches in overall performance and bottom 5 for improvement focus.

5. Recommend targeted interventions for low-performing schools.
`````

`
Output format: Dashboard wireframe + insights brief for school management."
`

## Prompt 21 — Energy Consumption Pattern Analysis for Cost Saving

`
"You are an Energy Data Analyst. I have hourly electricity consumption data for a manufacturing facility over 24 months.
`

`
Your task:
`

`````
1. Identify peak and off-peak consumption periods.

2. Analyse seasonal patterns in energy usage.

3. Quantify potential savings from shifting operations to off-peak hours.

4. Suggest renewable energy integration opportunities.

5. Create a projection model for energy cost savings over the next 12 months.
`````

`
Output format: PDF energy audit report + visual trend charts + savings projection table."
`

## Prompt 22 — Market Basket Analysis for Cross-Selling

`
"You are a Retail Data Mining Specialist. I have point-of-sale transaction data with item-level details for the past 12 months.
`

`
Your task:
`

`````
1. Use association rule mining (Apriori or FP-Growth) to identify frequent item combinations.

2. Calculate support, confidence, and lift for each rule.

3. Highlight top 10 product pairs with highest cross-sell potential.

4. Suggest bundle offers based on analysis.

5. Project potential revenue increase from implementing top 3 bundles.
`````

`
Output format: Association rules table + actionable cross-sell strategy document."
`

## Prompt 23 — Website Traffic and Conversion Analytics

`
"You are a Web Analytics Consultant. I have Google Analytics data for my e-commerce site over the past 6 months.
`

`
Your task:
`

`````
1. Identify top 5 traffic sources and their respective conversion rates.

2. Analyse bounce rate, average session duration, and pages per session.

3. Map the customer journey from landing page to purchase.

4. Highlight underperforming landing pages and suggest optimisation strategies.

5. Provide projected improvement metrics if changes are implemented.
`````

`
Output format: Data Studio dashboard layout + optimisation recommendations report."
`

## Prompt 24 — Manufacturing Process Efficiency Visualisation

`
"You are a Manufacturing Data Engineer. I have IoT sensor data for multiple machines in a production line over the past year.
`

`
Your task:
`

`````
1. Visualise machine uptime/downtime as a Gantt chart.

2. Identify bottlenecks in production flow.

3. Calculate defect rates per machine and per shift.

4. Recommend preventive maintenance schedules.

5. Suggest workflow changes to increase throughput without adding resources.
`````

`
Output format: Factory floor dashboard layout + process improvement plan."
`

## Prompt 25 — Financial Performance Storytelling for Investors

`
"You are a Financial Data Storyteller. I have quarterly income statements, balance sheets, and cash flow statements for the past 3 years.
`

`
Your task:
`

`````
1. Visualise revenue, gross profit, and net profit trends over time.

2. Calculate key financial ratios (ROE, ROA, current ratio, debt-to-equity) and explain their meaning.

3. Highlight major changes in expenses or revenue sources.

4. Provide a year-over-year growth summary.

5. Frame findings in a narrative that inspires investor confidence.
`````

`
Output format: Investor-ready slide deck with visuals, ratio analysis, and growth narrative."
`

# API Integration & Automation

## Prompt 1 — Connecting Multiple APIs for Unified Data

`
"You are an API Integration Engineer with expertise in REST (Representational State Transfer) and GraphQL APIs. I want to create a single automated workflow that combines data from Google Sheets, Shopify, and Google Analytics APIs.
`

`
Your task:
`

`````
1. Authenticate each API using OAuth 2.0 and store tokens securely.

2. Pull product sales data from Shopify, website traffic data from Google Analytics, and inventory data from Google Sheets.

3. Merge the datasets on product ID and date fields for unified reporting.

4. Schedule the workflow to run daily at midnight using a cron job or cloud scheduler.

5. Include logging for errors and success status.
`````

`
Output format: Python script with step-by-step API calls, merged dataset output as CSV, and instructions for deployment in a cloud environment (AWS Lambda or Google Cloud Functions)."
`

## Prompt 2 — Automating Social Media Posting via API

`
"You are a Social Media Automation Specialist experienced with the Meta Graph API, LinkedIn API, and Twitter API (now X API). I manage 3 platforms and want to post the same content automatically at scheduled times.
`

`
Your task:
`

`````
1. Authenticate all platform APIs and handle rate limits.

2. Create a reusable function that posts text, images, and videos from a single JSON file.

3. Add an option to customise captions per platform for optimal engagement.

4. Schedule posts using a job scheduler (like APScheduler in Python).

5. Log post IDs and engagement metrics for tracking.
`````

`
Output format: Python automation script + setup instructions + sample JSON template for post content."
`

## Prompt 3 — Automating Data Entry from Web Forms to CRM

`
"You are a CRM Workflow Automation Engineer skilled in HubSpot, Salesforce, and Zoho CRM APIs. I receive customer leads from a website form and want them automatically added to my CRM with tags for campaign tracking.
`

`
Your task:
`

`````
1. Set up a webhook to receive form submissions in real time.

2. Transform form data into the CRM’s required JSON format.

3. Use the CRM API to create a new lead record with appropriate tags (e.g., “WebForm2024”).

4. Send a confirmation email to the lead using the CRM’s email API.

5. Log each successful lead creation in a Google Sheet via API.
`````

`
Output format: API workflow diagram + example webhook handler code + CRM API call scripts."
`

## Prompt 4 — Email Marketing Automation with API

`
"You are an Email Marketing Automation Expert familiar with Mailchimp, SendGrid, and ActiveCampaign APIs. I want to send a weekly newsletter automatically using my Google Sheets contact list.
`

`
Your task:
`

`````
1. Connect Google Sheets API to read subscriber list.

2. Connect the chosen email service API and authenticate securely.

3. Pull the email template from a stored HTML file.

4. Send emails in batches to avoid exceeding API rate limits.

5. Update the Google Sheet with a “last sent” timestamp for each contact.
`````

`
Output format: Python/Node.js script + deployment guide + API keys & secrets handling instructions."
`

## Prompt 5 — Automating File Backups to Cloud Storage

`
"You are a Cloud Automation Engineer skilled in AWS S3, Google Drive, and Dropbox APIs. I have a folder on my local machine containing financial reports that must be backed up daily to all three cloud platforms.
`

`
Your task:
`

`````
1. Authenticate with all three cloud APIs.

2. Compress the local folder into a timestamped ZIP file.

3. Upload the ZIP file to each cloud platform.

4. Send an email notification with file URLs after successful upload.

5. Log the backup details in a CSV file for auditing.
`````

`
Output format: Shell/Python script + setup instructions + automation scheduling plan."
`

## Prompt 6 — Real-Time Stock Price Tracker with Alerts

`
"You are a Financial Data Automation Specialist experienced in Alpha Vantage, Yahoo Finance, and TradingView APIs. I want to track live stock prices for a watchlist of 10 Indian companies and receive alerts when prices change more than ±3% in a day.
`

`
Your task:
`

`````
1. Connect to the stock price API with authentication.

2. Create a script to fetch and store real-time prices every 5 minutes.

3. Compare the current price with the opening price for percentage change.

4. Trigger an email/SMS alert when the ±3% threshold is crossed.

5. Store all intraday data in a CSV for end-of-day analysis.
`````

`
Output format: Python script + CSV logging + alert system integration plan.
`

`
Input Files & Code Section:
`

```
1. API Key file (api_keys.json) for Alpha Vantage/Yahoo Finance.

2. watchlist.csv containing company ticker symbols.

3. Placeholder for email/SMS sending function."
```

## Prompt 7 — Automating PDF Invoice Creation from Sales Data

`
"You are a Document Automation Engineer skilled in ReportLab, wkhtmltopdf, and Google Docs API. I have daily sales data in CSV format and need automatically generated PDF invoices sent to customers.
`

`
Your task:
`

`````
1. Read the CSV to fetch customer details, products, and prices.

2. Generate a branded PDF invoice for each customer.

3. Save the invoice locally and in Google Drive.

4. Email the invoice to the customer with a personalised message.

5. Log invoice status (sent, pending, failed) in a Google Sheet.
`````

`
Output format: Python script + invoice PDF template + Google Drive integration guide.
`

`
Input Files & Code Section:
`

```
1. sales_data.csv with customer and order details.

2. invoice_template.html for branding.

3. API credentials for Google Drive and Gmail."
```

## Prompt 8 — Weather-Based Automation for Agriculture

`
"You are an Agricultural IoT Automation Specialist skilled in OpenWeatherMap API and smart irrigation systems. I want to automate irrigation based on real-time weather data.
`

`
Your task:
`

`````
1. Connect to the OpenWeatherMap API to fetch daily forecasts.

2. If rainfall probability is >70%, delay irrigation by 24 hours.

3. If temperature >35°C, schedule an extra watering cycle.

4. Send an SMS to the farmer confirming the decision.

5. Log all actions in a daily report file.
`````

`
Output format: IoT control script + weather API integration + action logging.
`

`
Input Files & Code Section:
`

```
1. API key file for OpenWeatherMap.

2. farm_config.json with field size, crop type, and irrigation limits.

Placeholder for SMS gateway integration code."
```

## Prompt 9 — Automating YouTube Video Uploads

`
"You are a YouTube API Automation Specialist. I want to upload videos from a folder to YouTube with titles, descriptions, and tags automatically pulled from a CSV file.
`

`
Your task:
`

`````
1. Authenticate using YouTube Data API v3 with OAuth 2.0.

2. Loop through a folder containing video files.

3. Read metadata from a CSV (title, description, tags, privacyStatus).

4. Upload each video with the corresponding metadata.

5. Log upload IDs and publish status.
`````

`
Output format: Python script + CSV metadata mapping + OAuth setup guide.
`

`
Input Files & Code Section:
`

```
1. video_metadata.csv with columns for each video.

2. Folder path for video files.
   
client_secret.json for OAuth credentials."
```

## Prompt 10 — Daily Currency Conversion Automation

`
"You are a Currency Data Automation Specialist. I want to fetch daily INR to USD, EUR, and GBP exchange rates and update them in my Google Sheet automatically.
`

`
Your task:
`

`````
1. Connect to a currency exchange API (e.g., ExchangeRate-API).

2. Fetch latest conversion rates for INR to target currencies.

3. Write data to a specific Google Sheets cell range.

4. Include timestamp of last update.

5. Schedule script to run daily at 8 AM IST.
`````

`
Output format: Python script + Google Sheets API integration + scheduler setup guide.
`

`
Input Files & Code Section:
`

```
1. API key file for ExchangeRate-API.

2. Google Sheets spreadsheet ID.

config.json for target currency list."
```

## Prompt 11 — Automating Job Application Tracking

`
Backstory: You’re a 28-year-old marketing professional applying to multiple companies at once. Keeping track of applications manually is messy — you often forget where you applied, the status, or the interview schedule. You want AI and APIs to track everything automatically.
`

`
Goal: Build an automation that pulls application data from job portals (LinkedIn, Naukri.com) and updates it into a single Google Sheet dashboard daily.
`

`
Prompt:
`

`
"You are a Job Search Workflow Automation Engineer. I want an automated job application tracker that consolidates applications from LinkedIn Jobs and Naukri.com using their APIs/webhooks.
`

`
Your task:
`

`````
1. Authenticate with LinkedIn API and Naukri.com’s developer API (or scrape data if no API exists).

2. Fetch job title, company name, date applied, status (applied, shortlisted, interview scheduled), and job link.

3. Push this data into a Google Sheet in structured columns.

4. Highlight rows where the application has been idle for >14 days.

5. Send me a daily email digest of new application updates.
`````

`
Output format: Google Sheet dashboard + email digest example + API scripts.
`

`
Input Files & Code Section:
`

```
1. API credentials for LinkedIn and Naukri.com

2. Google Sheet ID and credentials JSON

3. Email SMTP settings for sending daily digest"
```

## Prompt 12 — Automating Property Price Tracking for Investment

`
Backstory: You’re a 35-year-old professional looking to invest in property in Bangalore. Prices change fast and manual tracking is too slow. You want a tool that automatically fetches and compares prices across multiple real estate portals.
`

`
Goal: Build a daily property price tracker with alerts for deals under your budget.
`

`
Prompt:
`

`
"You are a Real Estate Data Automation Specialist skilled in integrating housing.com, magicbricks.com, and 99acres.com APIs.
`

`
Your task:
`

`````
1. Fetch property listings for specified locations (e.g., Whitefield, Indiranagar) within a budget range.

2. Extract details — price, size (sqft), price per sqft, location link.

3. Store data in a Google Sheet with a “lowest price this week” column.

4. Trigger an SMS alert when a property price drops more than 5% from last week.

5. Generate a weekly PDF market trend report.
`````

`
Output format: Google Sheet tracker + automated PDF report + SMS alert script.
`

`
Input Files & Code Section:
`

```
1. API credentials or scraping script for property portals

2. property_config.json with budget, preferred locations, size range

Google Sheets & Twilio SMS API credentials"
```

## Prompt 13 — Automating Invoice Payment Reminders

`
Backstory: You run a small design agency. Clients often delay payments, and manually sending reminders eats up your evenings. You want an automated reminder system that sends polite follow-ups.
`

`
Goal: Build an API-based automation that sends reminders at 7, 14, and 21 days after invoice due date.
`

`
Prompt:
`

`
"You are a Business Workflow Automation Specialist. I want to automate client payment reminders using QuickBooks API and Gmail API.
`

`
Your task:
`

`````
1. Pull unpaid invoice data from QuickBooks API with due dates.

2. Identify invoices past due by 7, 14, or 21 days.

3. Send a customised reminder email based on how late the payment is.

4. Log all sent reminders in a Google Sheet.

5. Mark the invoice in QuickBooks with “reminder sent” status.
`````

`
Output format: Automated reminder script + email template files + logging spreadsheet.
`

`
Input Files & Code Section:
`

```
1. QuickBooks API credentials

2. Google API credentials for Gmail & Sheets

email_templates/ folder with HTML templates for 7, 14, 21 days"
```

## Prompt 14 — Automating Resume Screening for Recruitment

`
Backstory: You’re an HR manager for a startup. Hundreds of resumes arrive daily. Manually screening them for skills is impossible. You need an API workflow that filters CVs based on required skills.
`

`
Goal: Automatically screen resumes and send shortlisted profiles to a hiring manager’s email.
`

`
Prompt:
`

`
"You are a Recruitment Automation Specialist. I want to integrate Google Drive API and an NLP model to process incoming resumes.
`

`
Your task:
`

`````
1. Monitor a Google Drive folder for new resumes.

2. Extract text from PDFs/DOCs using an OCR/NLP API.

3. Match candidate skills with a given job description using keyword matching and semantic similarity.

4. Move shortlisted resumes to a “Shortlisted” folder.

5. Email a daily summary to the hiring manager with names and matched skills.
`````

`
Output format: Resume screening script + summary email template + candidate matching report.
`

`
Input Files & Code Section:
`

```
1. Google Drive API credentials

2. Job description text file

3. API key for NLP/OCR service (e.g., Google Cloud Vision, OpenAI)"
```

## Prompt 15 — Automating YouTube Comment Sentiment Analysis

`
Backstory: You’re a content creator with 500K subscribers. It’s impossible to read every comment and spot trends in audience sentiment.
`

`
Goal: Build an API workflow that pulls all new comments, runs sentiment analysis, and gives you a weekly trend report.
`

`
Prompt:
`

`
"You are a Social Media Analytics Automation Engineer. I want a system that fetches my YouTube video comments weekly, analyses sentiment, and creates a dashboard.
`

`
Your task:
`

`````
1. Connect to YouTube Data API to fetch comments for all videos from the last 7 days.

2. Run sentiment analysis using a pre-trained model (e.g., VADER, BERT).

3. Categorise comments as positive, negative, or neutral.

4. Create visualisations showing weekly sentiment trends.

5. Generate a PDF report and store it in Google Drive.
`````

`
Output format: Sentiment analysis notebook + dashboard + weekly PDF.
`

`
Input Files & Code Section:
`

```
1. YouTube API credentials

2. Sentiment analysis model file or package requirements

3. Google Drive API credentials"
```

## Prompt 16 — Automating E-commerce Inventory Updates Across Platforms

`
Backstory: You sell products on Amazon, Flipkart, and your own Shopify store. Inventory changes fast, but updating each platform manually wastes hours and risks overselling.
`

`
Goal: Build an API automation that updates inventory levels across all platforms from a single source.
`

`
Prompt:
`

`
"You are an E-commerce API Integration Specialist. I want a single source of truth for my inventory, updated across Amazon, Flipkart, and Shopify in real time.
`

`
Your task:
`

`````
1. Connect to all three platform APIs using secure authentication (API keys or OAuth).

2. Fetch the latest inventory count from my central warehouse database or Google Sheet.

3. Update product stock levels on each platform.

4. Send me an email if a product’s stock falls below a reorder threshold.

5. Log all updates with timestamp, product ID, and before/after quantities.
`````

`
Output format: Inventory sync script + alert email template + update log file.
`

`
Input Files & Code Section:
`

```
1. API credentials for Amazon, Flipkart, and Shopify

2. inventory.csv or database connection details

Email SMTP settings for low-stock alerts"
```

## Prompt 17 — Automating Customer Support Ticket Categorisation

`
Backstory: Your startup gets 200+ support emails daily. Agents waste time reading and assigning tickets manually.
`

`
Goal: Use APIs and AI to automatically categorise tickets and assign them to the right team.
`

`
Prompt:
`

`
"You are a Customer Service Workflow Automation Engineer. I want to integrate Gmail API, NLP (Natural Language Processing), and a ticketing system API (like Zendesk).
`

`
Your task:
`

`````
1. Fetch new support emails via Gmail API.

2. Run NLP classification to detect category (Billing, Technical Issue, General Query, Complaint).

3. Create a ticket in Zendesk with the detected category.

4. Assign tickets to the relevant department queue.

5. Send an auto-response email to the customer with an estimated resolution time.
`````

`
Output format: Categorisation script + Zendesk integration + auto-reply email templates.
`

`
Input Files & Code Section:
`

```
1. Gmail API credentials

2. NLP model or keyword mapping file

3. Zendesk API credentials"
```

## Prompt 18 — Automating Daily Stock Market Newsletter

`
Backstory: You run a Telegram channel for stock market updates. Manually collecting news, stock prices, and analysis every morning is slow.
`

`
Goal: Generate and send a daily market summary via email and Telegram using APIs.
`

`
Prompt:
`

`
"You are a Financial Automation Developer. I want a daily 7:30 AM IST newsletter combining stock prices, market news, and a short AI-generated analysis.
`

`
Your task:
`

`````
1. Connect to Yahoo Finance API for NIFTY 50, SENSEX, and top 10 stocks data.

2. Pull top 5 market news headlines from News API.

3. Use GPT API to generate a 150-word market analysis.

4. Send the report via Gmail API and post to a Telegram channel via Telegram Bot API.

5. Store all reports in a Google Drive folder for archiving.
`````

`
Output format: Automated newsletter script + Telegram bot setup + daily report template.
`

`
Input Files & Code Section:
`

````
1. Yahoo Finance API key

2. News API key

3. OpenAI GPT API key

Gmail API and Telegram Bot credentials"
````

## Prompt 19 — Automating Attendance Tracking with Face Recognition

`
Backstory: Your office wants to replace manual attendance sheets with automated facial recognition connected to HR software.
`

`
Goal: Build a system that captures attendance via webcam and updates HR records automatically.
`

`
Prompt:
`

`
"You are an AI-Driven HR Automation Specialist. I want a face recognition attendance tracker that integrates with Zoho People API.
`

`
Your task:
`

`````
1. Connect a webcam to capture employee images at check-in/check-out.

2. Run face recognition using an API like AWS Rekognition or OpenCV.

3. Match recognised faces to employee IDs.

4. Update attendance in Zoho People API.

5. Send a daily attendance summary to HR.
`````

`
Output format: Attendance capture script + Zoho API integration + HR report template.
`

`
Input Files & Code Section:
`

```
1. Zoho People API credentials

2. Employee ID to face mapping database

3. Webcam access permissions and recognition API credentials"
```

## Prompt 20 — Automating Podcast Transcription and Upload

`
Backstory: You run a podcast and need transcripts for SEO and accessibility. Doing it manually takes hours.
`

`
Goal: Use APIs to transcribe each new episode and upload the text to your blog automatically.
`

`
Prompt:
`

`
"You are a Content Automation Engineer. I want an automation that listens for new podcast episodes, transcribes them, and publishes to my WordPress blog.
`

`
Your task:
`

`````
1. Monitor an RSS feed for new podcast episodes.

2. Download the audio file.

3. Use AssemblyAI or Google Speech-to-Text API for transcription.

4. Format the transcript into a blog-friendly HTML format.

5. Upload it as a new blog post via WordPress REST API.
`````

`
Output format: End-to-end transcription and upload script + blog post HTML template.
`

`
Input Files & Code Section:
`

```
1. Podcast RSS feed URL

2. Transcription API key

WordPress API credentials"
```

## Prompt 21 — Automating Business KPI Dashboard Updates

`
Backstory: You manage a startup and track sales, expenses, and customer data. You want your KPI dashboard updated automatically every morning.
`

`
Goal: Build an API workflow that pulls data from CRM, accounting software, and marketing tools into a BI dashboard.
`

`
Prompt:
`

`
"You are a Business Intelligence Automation Specialist. I want an automated data pipeline feeding my Power BI dashboard daily.
`

`
Your task:
`

`````
1. Fetch sales data from CRM API (HubSpot or Salesforce).

2. Fetch expenses from accounting API (QuickBooks or Zoho Books).

3. Fetch campaign performance from Google Ads API.

4. Push all data to a Power BI dataset via REST API.

5. Refresh dashboard daily at 7 AM IST.
`````

`
Output format: ETL (Extract, Transform, Load) script + Power BI dataset refresh automation.
`

`
Input Files & Code Section:
`

````
1. CRM API credentials

2. Accounting API credentials

3. Google Ads API credentials

4. Power BI API token"
````

## Prompt 22 — Automating Legal Document Generation

`
Backstory: You’re a lawyer preparing NDAs, contracts, and agreements for clients. Filling them manually is slow.
`

`
Goal: Build an API automation that fills in legal document templates from client data.
`

`
Prompt:
`

`
"You are a Legal Tech Automation Specialist. I want an API-based system that populates legal document templates from a client database.
`

`
Your task:
`

`````
1. Store client details (name, address, contract terms) in a Google Sheet or database.

2. Pull data via API and inject into pre-defined Word/PDF templates.

3. Save final documents in Google Drive and send via Gmail API.

4. Track sent documents in a log sheet.

5. Allow re-generation if client data changes.
`````

`
Output format: Document automation script + legal template folder + logging sheet.
`

`
Input Files & Code Section:
`

```
1. Document templates (Word/PDF)

2. Google Sheets API credentials

Google Drive & Gmail API credentials"
```

## Prompt 23 — Automating Food Delivery Order Processing

`
Backstory: You run a cloud kitchen. Orders from Zomato, Swiggy, and your own website come separately, causing delays.
`

`
Goal: Build an API integration that merges all orders into one system.
`

`
Prompt:
`

`
"You are a Food Tech API Integration Specialist. I want a centralised order management system pulling data from Zomato, Swiggy, and my website.
`

`
Your task:
`

`````
1. Connect to all order APIs with authentication.

2. Merge incoming orders into one dashboard view.

3. Send order confirmation to customers via SMS API.

4. Trigger kitchen ticket printing via printer API.

5. Store all order data for monthly analysis.
`````

`
Output format: Order aggregation script + kitchen display dashboard + SMS integration.
`

`
Input Files & Code Section:
`

```
1. API keys for Zomato, Swiggy, website

2. SMS API credentials

Database connection for order storage"
```

## Prompt 24 — Automating Social Media Comment Replies

`
Backstory: You run a brand page with thousands of comments daily. Replying manually takes too long.
`

`
Goal: Build a system that auto-replies to comments based on sentiment and keywords.
`

`
Prompt:
`

`
"You are a Social Media Engagement Automation Engineer. I want to use Instagram Graph API and NLP to auto-reply to comments.
`

`
Your task:
`

`````
1. Fetch new comments via Instagram API.

2. Run keyword & sentiment analysis to classify the comment.

3. Use a pre-defined reply template for each sentiment type.

4. Post the reply via API.

5. Log all replied comments in Google Sheets.
`````

`
Output format: Comment reply automation script + sentiment keyword mapping + logging sheet.
`

`
Input Files & Code Section:
`

```
1. Instagram Graph API credentials

2. Keyword mapping CSV

3. Google Sheets API credentials"
```

## Prompt 25 — Automating YouTube to Instagram Clip Conversion

`
Backstory: You want to post highlights of your YouTube videos on Instagram Reels automatically.
`

`
Goal: Build an API workflow that trims, captions, and uploads clips from YouTube to Instagram.
`

`
Prompt:
`

`
"You are a Video Content Automation Specialist. I want to pull my latest YouTube videos, create 60-second highlights, auto-caption them, and upload to Instagram.
`

`
Your task:
`

`````
1. Fetch video from YouTube Data API.

2. Trim to highlight section based on timestamps from a CSV.

3. Add captions using an API like Rev.ai.

4. Upload to Instagram via Instagram Graph API.

5. Store uploaded video link in a Google Sheet.
`````

`
Output format: Video processing script + Instagram upload automation + logging system.
`

`
Input Files & Code Section:
`

```
1. YouTube API credentials

2. Instagram Graph API credentials

3. clip_timestamps.csv with video ID and time ranges"
```

# Product Documentation & User Guides

## Prompt 1 — Creating a Step-by-Step User Guide for a Mobile App

`
Backstory: Your startup just launched a budgeting mobile app. Many first-time users uninstall it because they can’t figure out how to set up their first budget.
`

`
Goal: Create a simple, visual, step-by-step guide that walks new users through account creation, linking bank accounts, and setting their first budget.
`

`
Prompt:
`

`
"You are a User Experience Documentation Specialist. I need you to create a beginner-friendly setup guide for our budgeting mobile app.
`

`
Your task:
`

`````
1. Break the guide into 6–8 clear steps.

2. Include screenshots and captions for each step.

3. Write in simple language for non-technical users.

4. Add a troubleshooting section for common signup issues.

5. Format the final document for PDF and in-app help center.
`````

`
Output format: Step-by-step guide (with images) in PDF + HTML version for web embedding.
`

`
Input Files & Code Section:
`

```
1. app_screenshots.zip containing key UI images.

2. Brand style guide PDF for fonts & colors.

CSV file of common user questions from support tickets."
```

## Prompt 2 — Generating API Documentation for a Developer Portal

`
Backstory: You’ve built a public API for your food delivery platform, but developers keep asking for examples and request format details because your docs are incomplete.
`

`
Goal: Create clear, developer-focused API documentation with examples and authentication instructions.
`

`
Prompt:
`

`
"You are a Technical API Documentation Expert. I want you to create API docs for our food delivery API.
`

`
Your task:
`

`````
1. Describe authentication (OAuth 2.0) process clearly.

2. Document all endpoints with methods, parameters, and sample JSON responses.

3. Provide example code snippets in Python, JavaScript, and cURL.

4. Include rate limits and error codes.

5. Add a “Getting Started” quick guide for first-time developers.
`````

`
Output format: Markdown-based API documentation + HTML developer portal version.
`

`
Input Files & Code Section:
`

```
1. OpenAPI/Swagger specification file (api_spec.json).

2. List of example API requests and responses.

Branding assets for developer portal."
```

## Prompt 3 — Writing Release Notes for a SaaS Platform

`
Backstory: Your SaaS analytics tool has frequent updates, but customers are unaware of new features and fixes because release notes are dull and overly technical.
`

`
Goal: Write engaging, customer-friendly release notes for each product update.
`

`
Prompt:
`

`
"You are a Product Communications Writer. I want you to create release notes for our SaaS analytics platform that both inform and excite customers.
`

`
Your task:
`

`````
1. Summarize new features in plain language.

2. Highlight bug fixes and performance improvements.

3. Add screenshots or GIFs for visual impact.

4. Include “How to use” tips for each new feature.

5. Publish in both email newsletter and in-app notifications format.
`````

`
Output format: HTML email template + Markdown release notes file.
`

`
Input Files & Code Section:
`

```
1. Product update changelog CSV.

2. Screenshots/GIFs folder.

3. Customer usage analytics to highlight most-requested features."
```

## Prompt 4 — Creating Onboarding Guides for a CRM Tool

`
Backstory: Your sales team is adopting a new CRM tool, but they’re struggling to switch from spreadsheets to the new system.
`

`
Goal: Create a hands-on onboarding manual for new CRM users.
`

`
Prompt:
`

`
"You are a CRM Onboarding Documentation Specialist. I want an onboarding manual that helps sales reps transition from spreadsheets to our CRM.
`

`
Your task:
`

`````
1. Explain CRM login and account setup.

2. Show how to import contacts from CSV.

3. Demonstrate adding leads, deals, and activities.

4. Include best practices for daily CRM usage.

5. Add a printable “Quick Reference” cheatsheet.
`````

`
Output format: PDF onboarding manual + 1-page cheatsheet.
`

`
Input Files & Code Section:
`

```
1. CRM system screenshots.

2. Sample CSV contact file.

3. Sales workflow diagram."
```

## Prompt 5 — Creating a Knowledge Base Article for a Common Support Issue

`
Backstory: Customers often contact support because they forget their password and can’t reset it.
`

`
Goal: Create a self-service article that reduces these repetitive support requests.
`

`
Prompt:
`

`
"You are a Knowledge Base Content Specialist. I want you to create a help article for “How to Reset Your Password” for our e-commerce platform.
`

`
Your task:
`

`````
1. Write clear, step-by-step instructions.

2. Include desktop and mobile screenshots.

3. Provide tips for strong password creation.

4. Add troubleshooting for common reset errors.

5. Format for search engine optimization (SEO).
`````

`
Output format: HTML article for help center + PDF version for offline use.
`

`
Input Files & Code Section:
`

```
1. Screenshot set for password reset flow.

2. Branding guide for help center articles.

3. List of top password reset issues from support logs."
```

## Prompt 6 — Creating Interactive Tutorials for a Project Management Tool

`
Backstory: Your project management SaaS tool has powerful features, but most customers only use the basic ones because they’re unaware of advanced capabilities.
`

`
Goal: Build interactive, click-through tutorials inside the app to teach advanced features.
`

`
Prompt:
`

`
"You are a Product Education Content Developer. I need you to create in-app interactive tutorials for our project management platform.
`

`
Your task:
`

`````
1. Select top 5 underused advanced features.

2. Create step-by-step walkthrough scripts for each.

3. Use tooltips, highlights, and click prompts to guide the user.

4. Include progress tracking so users can resume later.

5. Prepare text, screenshots, and instructional videos for each step.
`````

`
Output format: JSON tutorial script for app integration + video files + image assets.
`

`
Input Files & Code Section:
`

```
1. Feature usage analytics CSV.

2. UI screenshot set.

3. In-app tutorial framework documentation."
```

## Prompt 7 — Writing Compliance & Policy Documentation

Backstory: You’ve launched a fintech app, but regulatory requirements demand that you publish clear compliance policies for users.

Goal: Draft customer-facing compliance documentation that is accurate but easy to understand.

Prompt:

"You are a Regulatory Documentation Specialist. I want you to create compliance and privacy policies for our fintech app.

Your task:


1. Review applicable regulations (RBI, GDPR, PCI DSS).

2. Write privacy policy, data handling policy, and terms of service.

3. Ensure language is plain and free of legal jargon where possible.

4. Include diagrams showing data flow and storage locations.

5. Format for both web and PDF publication.

Output format: Policy documents in DOCX, PDF, and HTML formats.

Input Files & Code Section:


Current draft compliance notes.

Legal team’s checklist.

Data flow diagrams."

Prompt 8 — Documenting API Integration for Third-Party Partners

Backstory: You offer a payment API that third-party merchants can integrate, but integration requests are delayed due to unclear documentation.

Goal: Create a developer-friendly integration manual.

Prompt:

"You are a Partner Integration Documentation Engineer. I want you to create a full integration manual for our payment API.

Your task:


1. Describe authentication, endpoint usage, and required parameters.

2. Provide step-by-step integration example for a sample merchant app.

3. Include common error codes and troubleshooting steps.

4. Add code examples in PHP, Node.js, and Python.

5. Include test environment setup instructions.

Output format: Markdown integration manual + HTML version for partner portal.

Input Files & Code Section:


API reference (swagger.yaml).

Sandbox API credentials.

Sample merchant application codebase."

Prompt 9 — Creating Internal Developer Documentation

Backstory: Your dev team has grown quickly, but onboarding new engineers takes weeks because there’s no central engineering guide.

Goal: Document internal codebase, architecture, and workflows.

Prompt:

"You are an Internal Engineering Documentation Specialist. I want a central developer handbook for our engineering team.

Your task:


1. Describe project architecture with diagrams.

2. Document coding standards and naming conventions.

3. Include instructions for local environment setup.

4. Explain CI/CD pipeline processes.

5. Maintain this as a living document in the repo.

Output format: Developer handbook in Markdown + PDF export.

Input Files & Code Section:


Architecture diagrams.

Existing dev onboarding notes.

Git repository README.md."

Prompt 10 — Writing Feature Comparison Guides

Backstory: Many customers ask how your product compares to competitors, but your sales team doesn’t have a clear document to share.

Goal: Create a side-by-side feature comparison guide.

Prompt:

"You are a Competitive Product Documentation Writer. I want a feature comparison document between our tool and top 3 competitors.

Your task:


1. List key features side-by-side in a table.

2. Use simple, customer-friendly language.

3. Highlight where our product is stronger.

4. Include screenshots for visual comparison.

5. Format for both sales decks and website FAQ.

Output format: Comparison PDF + PPT slide deck.

Input Files & Code Section:


Competitor feature research spreadsheet.

Product screenshots folder.

Brand guidelines for colors and fonts."

Prompt 11 — Creating Troubleshooting Flowcharts

Backstory: Your tech support team spends hours on calls walking users through fixes for common issues.

Goal: Create self-help troubleshooting flowcharts.

Prompt:

"You are a Technical Troubleshooting Documentation Designer. I want to create visual flowcharts for common problems with our SaaS tool.

Your task:


1. Select top 5 recurring issues from support logs.

2. Create clear yes/no flowcharts for each problem.

3. Use icons and colors to make steps easy to follow.

4. Add estimated time for each fix step.

5. Export to PDF for customers and PNG for website.

Output format: Flowchart diagrams in PNG + consolidated PDF booklet.

Input Files & Code Section:


Support ticket analysis CSV.

Company color palette file.

Icon set for diagrams."

Prompt 12 — Creating Voice & Tone Guidelines

Backstory: Multiple writers contribute to your help center, but the style is inconsistent.

Goal: Create a unified voice & tone guide for all documentation writers.

Prompt:

"You are a Content Style Guide Specialist. I want a voice & tone guideline document for our documentation team.

Your task:


1. Define brand personality in writing.

2. Provide examples of do’s and don’ts.

3. Include guidelines for writing for technical vs. non-technical audiences.

4. Cover accessibility considerations (readability, alt text, etc.).

5. Provide templates for different content types.

Output format: Voice & tone PDF + quick reference card.

Input Files & Code Section:


Existing help articles.

Marketing brand guide.

Feedback from customer surveys."

Prompt 13 — Writing Contextual Tooltips for a Web Application

Backstory: Your SaaS dashboard is feature-rich, but many first-time users don’t understand what certain buttons or fields do.

Goal: Create short, contextual tooltips that explain features without overwhelming the user.

Prompt:

"You are a UX Microcopy Documentation Specialist. I want you to create clear, concise tooltips for our SaaS dashboard.

Your task:


1. Identify 30 key UI elements needing tooltips.

2. Write short descriptions (max 20 words) in plain language.

3. Ensure consistency in style and tone.

4. Include an internal reference table mapping tooltip text to UI elements.

5. Provide JSON/CSV format for direct integration with the UI codebase.

Output format: Tooltip text table (CSV + JSON) + implementation guide.

Input Files & Code Section:


UI element list CSV.

Screenshot set of dashboard UI.

Branding style guide."

Prompt 14 — Creating a Quick Start Guide for a Developer SDK (Software Development Kit)

Backstory: Developers integrating your SDK are struggling because there’s no concise “first steps” documentation.

Goal: Build a quick start guide that allows developers to implement the SDK within 30 minutes.

Prompt:

"You are a Developer Onboarding Documentation Expert. I want a quick start guide for our JavaScript SDK.

Your task:


1. Include installation steps via npm/yarn.

2. Show basic initialization code with example API calls.

3. Document common config options and defaults.

4. Provide a working sample app repository link.

5. Add troubleshooting tips for common setup errors.

Output format: Markdown quick start guide + PDF export.

Input Files & Code Section:


SDK code sample repository link.

API key for sandbox testing.

Screenshot folder for sample outputs."

Prompt 15 — Documenting Accessibility Features for Users with Disabilities

Backstory: Your platform is accessible, but many users with disabilities don’t know about the available features.

Goal: Create an accessibility guide showcasing these features.

Prompt:

"You are an Accessibility Documentation Specialist. I want an accessibility features guide for our learning platform.

Your task:


1. List all accessibility options (keyboard shortcuts, screen reader support, high contrast mode).

2. Provide step-by-step activation instructions for each.

3. Add compatibility notes for different browsers/devices.

4. Include best practices for accessible usage.

5. Format as both web and audio versions for accessibility.

Output format: PDF + HTML + MP3 narration.

Input Files & Code Section:


Feature list CSV.

Accessibility testing report.

Screenshots and icon assets."

Prompt 16 — Creating Interactive FAQs with Search Functionality

Backstory: Your current FAQ page is static and users struggle to find relevant answers quickly.

Goal: Build a searchable, interactive FAQ system.

Prompt:

"You are a Help Center Experience Designer. I want to turn our static FAQ page into an interactive, searchable database.

Your task:


1. Convert FAQs into a searchable JSON format.

2. Tag each FAQ with categories and keywords.

3. Implement autocomplete for search queries.

4. Include expand/collapse answers for better UX.

5. Provide embed code for website integration.

Output format: FAQ database (JSON) + HTML/CSS/JS embed code.

Input Files & Code Section:


Existing FAQ text in CSV.

Website brand style guide.

JavaScript library documentation for search."

Prompt 17 — Writing Maintenance Manuals for Hardware Products

Backstory: Customers often damage devices because they don’t follow maintenance guidelines.

Goal: Write a detailed maintenance and care manual.

Prompt:

"You are a Hardware Technical Writer. I want a maintenance manual for our smart home thermostat.

Your task:


1. List cleaning, calibration, and firmware update procedures.

2. Provide do’s and don’ts with illustrations.

3. Include seasonal maintenance reminders.

4. Add troubleshooting section for physical faults.

5. Format for both printed booklet and online PDF.

Output format: Illustrated manual in PDF + printable A5 booklet.

Input Files & Code Section:


Product engineering diagrams.

Service checklist from repair team.

Image asset folder."

Prompt 18 — Documenting Multi-Language Product Instructions

Backstory: You sell in multiple countries, but product instructions are only in English.

Goal: Create multilingual product manuals.

Prompt:

"You are a Multilingual Documentation Specialist. I want product instructions for our kitchen appliance in English, Hindi, and Tamil.

Your task:


1. Translate existing manual while keeping technical accuracy.

2. Adapt units (metric/imperial) as needed.

3. Include culturally relevant examples.

4. Ensure formatting works for all languages.

5. Provide print-ready and web-ready versions.

Output format: PDF manuals in all 3 languages.

Input Files & Code Section:


Current English manual (DOCX).

Brand typography guidelines.

Translation glossary file."

Prompt 19 — Creating How-To Videos for Common Tasks

Backstory: Written guides are available, but some customers prefer video walkthroughs.

Goal: Produce short tutorial videos for key product functions.

Prompt:

"You are a Video Documentation Producer. I want 5 short (under 2 mins each) tutorial videos for our e-learning platform.

Your task:


1. Write video scripts for each task.

2. Record screen captures with voiceover.

3. Add captions and callout graphics.

4. Export in MP4 for YouTube and MOV for in-app playback.

5. Provide thumbnail images for each video.

Output format: Video files + scripts + thumbnails.

Input Files & Code Section:


Task list CSV.

Brand video intro/outro files.

Voiceover style guide."

Prompt 20 — Creating an API Changelog Page

Backstory: API updates break client integrations because developers aren’t notified in time.

Goal: Publish a public API changelog with versioning details.

Prompt:

"You are an API Documentation Manager. I want a live API changelog page for our developer portal.

Your task:


1. Track API version changes with release dates.

2. Add summaries of new/removed/modified endpoints.

3. Highlight breaking changes in red.

4. Provide migration notes for affected endpoints.

5. Update automatically via CI/CD when code changes are merged.

Output format: Markdown changelog + HTML portal page.

Input Files & Code Section:


Git commit history.

API spec change diff file.

Developer portal access."

Prompt 21 — Writing Internal Product Playbooks for Support Staff

Backstory: Support staff often escalate tickets unnecessarily because they lack clear product troubleshooting guidelines.

Goal: Create internal product playbooks for the support team.

Prompt:

"You are a Support Operations Documentation Specialist. I want to create internal playbooks for handling common customer issues.

Your task:


1. Document step-by-step troubleshooting workflows.

2. Include escalation criteria for each case.

3. Provide scripts for customer communication.

4. Add visual aids where relevant.

5. Store in an internal wiki for easy updates.

Output format: Playbook PDFs + wiki pages.

Input Files & Code Section:


Support ticket history CSV.

Current internal notes.

Diagram/image assets."

Prompt 22 — Documenting Integration with Popular Third-Party Tools

Backstory: Customers want to connect your product with tools like Slack, Google Sheets, and Zapier, but don’t know how.

Goal: Create integration guides for top requested tools.

Prompt:

"You are a Third-Party Integration Documentation Specialist. I want guides for integrating our platform with Slack, Google Sheets, and Zapier.

Your task:


1. Write step-by-step instructions with screenshots.

2. Show real-life use case examples for each integration.

3. Add troubleshooting tips for API errors.

4. Include estimated setup time for each.

5. Format for help center and PDF export.

Output format: 3 integration guides in PDF + HTML.

Input Files & Code Section:


Integration API credentials.

User request survey results.

Screenshot set for each tool."

Prompt 23 — Creating Printable Cheat Sheets for Power Users

Backstory: Advanced users want quick reference material without reading long manuals.

Goal: Create compact, printable cheat sheets.

Prompt:

"You are a Productivity Documentation Designer. I want a one-page quick reference cheat sheet for our desktop productivity app.

Your task:


1. Include top keyboard shortcuts.

2. Add quick access menu navigation.

3. Include power user tips.

4. Use icons and color coding for readability.

5. Provide in A4 and Letter size PDFs.

Output format: Cheat sheet PDF in two sizes.

Input Files & Code Section:


Shortcut list CSV.

App UI screenshots.

Icon asset folder."

Prompt 24 — Creating User Story-Based Tutorials

Backstory: Customers understand better when tutorials follow real-world scenarios.

Goal: Write tutorials framed as user stories.

Prompt:

"You are a Scenario-Based Learning Documentation Specialist. I want tutorials that walk through tasks using real customer scenarios.

Your task:


1. Select top 3 customer use cases.

2. Write tutorials in story format.

3. Include relevant screenshots and tips.

4. End each with key takeaways.

5. Format for blog and PDF.

Output format: 3 story-based tutorials in HTML + PDF.

Input Files & Code Section:


Customer interview transcripts.

Screenshot set.

Branding style guide."

Prompt 25 — Creating AI-Assisted Product Guides

Backstory: You want to experiment with AI-generated personalized product guides for new users.

Goal: Create a template that AI can use to generate tailored guides.

Prompt:

"You are an AI-Enhanced Documentation Designer. I want a product guide template that AI can fill with user-specific tips.

Your task:


1. Create placeholders for user goals and usage history.

2. Include a modular structure for different product features.

3. Provide instructions for AI prompt generation.

4. Add export options for PDF and HTML.

5. Ensure template is editable in Google Docs.

Output format: Editable DOCX template + JSON structure for AI integration.

Input Files & Code Section:


User onboarding questionnaire template.

Feature description database.

AI prompt library file."


Cybersecurity & Data Privacy

Prompt 1 — Automating Security Log Monitoring

Backstory: You’re an IT administrator for a mid-sized company. Your security logs are massive, and manually scanning them for threats is impossible. Last year, you missed a brute-force attack because it got buried in the logs.

Goal: Create an automated pipeline that monitors security logs, flags suspicious activity, and sends real-time alerts.

Prompt:

"You are a Cybersecurity Automation Engineer. I want a script that scans server logs in real time and alerts me of suspicious activity such as failed login attempts, unusual IP addresses, or data spikes.

Your task:


1. Connect to the server log files via API or secure SSH.

2. Parse log entries and match against predefined threat patterns (failed logins >5 in 1 minute, foreign IP access, large file downloads).

3. Send an alert email/SMS if a threat is detected.

4. Store flagged events in a database for future analysis.

5. Generate a daily security summary report.

Output format: Security monitoring script + threat pattern list + alert notification system.

Input Files & Code Section:


Path to log files or log API endpoint

Threat detection rules CSV

Email/SMS API credentials"

Prompt 2 — Automating Data Backup with Encryption

Backstory: You manage sensitive medical records for a clinic. If your system crashes or is hacked, you can’t risk losing unencrypted patient data.

Goal: Automate daily backups to cloud storage with strong encryption.

Prompt:

"You are a Data Security Engineer. I want an automated backup system that encrypts files before uploading them to cloud storage (AWS S3, Google Drive).

Your task:


1. Identify sensitive folders for backup.

2. Compress and encrypt files using AES-256 encryption.

3. Upload encrypted backups to cloud storage via API.

4. Store encryption keys securely in a password vault.

5. Maintain a backup log with timestamps and checksum hashes.

Output format: Encrypted backup script + cloud upload integration + key storage instructions.

Input Files & Code Section:


Encryption key file (secure vault reference)

Cloud API credentials

List of file/folder paths for backup"

Prompt 3 — Automating Phishing Email Detection

Backstory: Your employees keep falling for phishing emails, leading to security risks. Manual awareness training isn’t enough.

Goal: Build an API-based system that scans incoming emails and flags potential phishing attempts.

Prompt:

"You are an Email Security Automation Specialist. I want to integrate Gmail API with an AI phishing detection model.

Your task:


1. Fetch incoming emails via Gmail API.

2. Scan sender domains, suspicious keywords, and link redirections.

3. Assign a risk score to each email.

4. Move high-risk emails to a “Quarantine” folder.

5. Send a weekly phishing report to the security team.

Output format: Email scanning script + risk scoring system + quarantine folder setup.

Input Files & Code Section:


Gmail API credentials

Keyword/risk pattern JSON file

AI phishing detection model file"

Prompt 4 — Automating GDPR Data Deletion Requests

Backstory: Your European customers often request data deletion under GDPR laws. Handling requests manually is time-consuming and error-prone.

Goal: Automate GDPR “Right to be Forgotten” requests.

Prompt:

"You are a Privacy Compliance Automation Expert. I want a workflow that processes GDPR deletion requests automatically.

Your task:


1. Receive requests via a secure web form.

2. Authenticate the requester’s identity via email verification.

3. Locate all user data across databases and APIs.

4. Delete or anonymise the data as per GDPR guidelines.

5. Send a confirmation email and store a compliance log.

Output format: Deletion automation script + compliance report template + GDPR checklist.

Input Files & Code Section:


Database connection details

Web form API endpoint

Email verification script"

Prompt 5 — Automating Vulnerability Scans

Backstory: You’re a security analyst at a SaaS startup. You run vulnerability scans manually once a month, but threats change daily.

Goal: Schedule automated vulnerability scans for all production servers.

Prompt:

"You are a Security Scan Automation Engineer. I want to run daily vulnerability scans and generate reports automatically.

Your task:


1. Integrate with a vulnerability scanning tool API (e.g., Nessus, OpenVAS).

2. Schedule scans for all server IPs.

3. Export scan results to a PDF and store in a secure folder.

4. Send a daily email summary with high-risk vulnerabilities.

5. Track vulnerability history in a Google Sheet.

Output format: Scheduled scan automation + PDF reporting script + risk tracking spreadsheet.

Input Files & Code Section:


Vulnerability scanner API credentials

Server IP list CSV

Google Sheets API credentials"

Prompt 6 — Automating Two-Factor Authentication (2FA) Setup for All Users

Backstory: You’re a system admin at a mid-sized company. Many employees still use only passwords to log in, making the company vulnerable to credential theft.

Goal: Enforce and automate 2FA setup across all employee accounts using APIs.

Prompt:

"You are an Identity & Access Management Automation Specialist. I want to roll out mandatory Two-Factor Authentication for all company accounts in Google Workspace.

Your task:


1. Use Google Admin SDK API to identify accounts without 2FA enabled.

2. Send automated emails prompting users to enable 2FA.

3. Provide a one-click link to the 2FA setup page.

4. Disable accounts not compliant after 7 days.

5. Generate a compliance report for management.

Output format: 2FA enforcement script + email template + compliance report spreadsheet.

Input Files & Code Section:


Google Admin SDK API credentials

Email template file

Compliance tracking CSV"

Prompt 7 — Automating Data Breach Monitoring with Dark Web Scans

Backstory: A client’s credentials were leaked on the dark web, and you only found out weeks later. You want to monitor this proactively.

Goal: Create an automation that scans the dark web for stolen company credentials.

Prompt:

"You are a Threat Intelligence Automation Engineer. I want to integrate HaveIBeenPwned API and a dark web monitoring API to scan for leaked email/password combinations.

Your task:


1. Fetch employee email list from HR database.

2. Query APIs for data breaches linked to these emails.

3. Flag and notify affected employees to reset passwords.

4. The store results in an encrypted database.

5. Send a monthly summary to the security team.

Output format: Breach monitoring script + notification template + encrypted breach database.

Input Files & Code Section:


API keys for HaveIBeenPwned and dark web monitoring tool

Employee email list CSV

Email SMTP settings for alerts"

Prompt 8 — Automating Role-Based Access Control (RBAC) Updates

Backstory: Employees change departments often, but their access permissions stay the same, leaving old data vulnerable.

Goal: Automate RBAC updates based on HR records.

Prompt:

"You are an Access Control Automation Expert. I want an integration between our HR system and internal application APIs to update user permissions automatically.

Your task:


1. Fetch updated employee roles from HR system API.

2. Compare current permissions in application API.

3. Add/remove access rights based on role changes.

4. Log all changes with timestamps.

5. Notify IT admin for high-privilege changes.

Output format: RBAC sync script + permissions change log + alert email template.

Input Files & Code Section:


HR system API credentials

Application API credentials

Role-to-permission mapping JSON"

Prompt 9 — Automating Security Awareness Quizzes

Backstory: Employees forget cybersecurity best practices unless reminded regularly.

Goal: Send automated monthly security quizzes to employees via email.

Prompt:

"You are a Security Training Automation Specialist. I want a system that emails a short quiz to employees each month and records their scores.

Your task:


1. Store quiz questions in a Google Sheet or database.

2. Send quiz links via Gmail API.

3. Collect responses via Google Forms API.

4. Calculate scores and store in a results sheet.

5. Flag employees who score below 70% for follow-up training.

Output format: Quiz automation script + question bank file + results dashboard.

Input Files & Code Section:


Google Sheets API credentials

Gmail API credentials

Quiz question CSV or database file"

Prompt 10 — Automating SSL Certificate Expiry Alerts

Backstory: One of your client websites went down because the SSL certificate expired — and nobody noticed in time.

Goal: Monitor SSL expiry dates and send alerts before expiration.

Prompt:

"You are a Web Security Automation Engineer. I want a system that checks SSL certificate expiry dates for a list of domains.

Your task:


1. Fetch SSL certificate details for each domain.

2. Identify expiry dates within the next 30 days.

3. Send alert emails with renewal instructions.

4. Update a tracking sheet with expiry status.

5. Repeat the check daily.

Output format: SSL monitoring script + expiry alert template + tracking spreadsheet.

Input Files & Code Section:


Domain list CSV

Email SMTP settings

Google Sheets API credentials"

Prompt 11 — Automating Endpoint Device Compliance Checks

Backstory: Your company has a Bring Your Own Device (BYOD) policy, but many employees connect with outdated or unpatched devices, creating security gaps.

Goal: Automatically check if employee devices meet compliance requirements before allowing network access.

Prompt:

"You are an Endpoint Security Automation Engineer. I want a system that verifies employee device compliance (OS version, antivirus status, firewall enabled) every time they connect to the company network.

Your task:


1. Integrate with an endpoint management API (e.g., Microsoft Intune, Jamf).

2. Collect device compliance data in real time.

3. Block network access if the device fails checks.

4. Notify the employee with steps to fix compliance issues.

5. Log all non-compliant devices for security audits.

Output format: Compliance check script + access control API integration + remediation email template.

Input Files & Code Section:


Endpoint management API credentials

Compliance rule configuration file (JSON)

Network access control API credentials"

Prompt 12 — Automating Sensitive File Access Alerts

Backstory: You store financial reports in a shared drive, and last quarter a contractor downloaded files they weren’t supposed to access.

Goal: Set up real-time alerts for access to sensitive files.

Prompt:

"You are a File Access Monitoring Specialist. I want an automation that detects and alerts whenever certain high-security files are accessed.

Your task:


1. Connect to Google Drive API or internal file server API.

2. Monitor access logs for the target file/folder.

3. Trigger an alert when access is detected outside approved user list.

4. Record details: user ID, timestamp, IP address.

5. Send an incident report to the security team.

Output format: File access monitoring script + alerting system + incident report format.

Input Files & Code Section:


File/folder ID list CSV

Approved user list CSV

Email/SMS API credentials"

Prompt 13 — Automating Database Security Audits

Backstory: Your customer database holds personal information, but monthly manual security audits take too much time and miss critical misconfigurations.

Goal: Automate periodic database security audits and reporting.

Prompt:

"You are a Database Security Automation Expert. I want a script that scans for vulnerabilities in our MySQL/PostgreSQL databases and generates a security report.

Your task:


1. Connect to the database securely.

2. Check for weak passwords, outdated versions, excessive user privileges.

3. Identify unused accounts and revoke access.

4. Generate a PDF report with recommendations.

5. Email the report to the database administrator.

Output format: Database audit script + PDF report template + email delivery function.

Input Files & Code Section:


Database connection credentials (secured)

Vulnerability scan checklist JSON

Email SMTP settings"

Prompt 14 — Automating USB Device Restrictions

Backstory: An employee once copied sensitive data onto a personal USB drive without permission.

Goal: Automatically detect and block unapproved USB devices.

Prompt:

"You are an Endpoint Device Control Automation Specialist. I want a system that blocks all USB devices except approved company drives.

Your task:


1. Detect when a USB device is connected.

2. Compare its serial number against the approved list.

3. Block access if not approved.

4. Send an alert to the IT security team.

5. Log all USB connection attempts.

Output format: USB restriction script + approved device list + alert and log system.

Input Files & Code Section:


Approved USB device serial number list CSV

Endpoint monitoring API credentials"

Prompt 15 — Automating Password Expiry Reminders

Backstory: Employees often forget to change passwords on time, leading to expired accounts and downtime.

Goal: Send automated password change reminders.

Prompt:

"You are an Account Security Automation Specialist. I want to integrate with Active Directory (AD) to send reminders before password expiry.

Your task:


1. Connect to AD via API or LDAP.

2. Fetch users whose passwords expire within 10 days.

3. Send email reminders at 10, 5, and 2 days before expiry.

4. Track who changes passwords after reminders.

5. Generate a monthly compliance report.

Output format: Reminder script + email template + compliance tracking sheet.

Input Files & Code Section:


AD connection details

Email SMTP credentials"

Prompt 16 — Automating Encrypted File Sharing

Backstory: Your legal team frequently shares confidential documents with clients, but sending via regular email is risky.

Goal: Create a secure encrypted file-sharing automation.

Prompt:

"You are a Secure File Transfer Automation Expert. I want to encrypt files and send them via a secure download link that expires after 48 hours.

Your task:


1. Accept file upload from the legal team.

2. Encrypt the file using AES-256.

3. Upload to secure cloud storage.

4. Generate a time-limited download link.

5. Email the link to the client with a decryption key sent separately.

Output format: Secure sharing script + encryption guide + link expiration setup.

Input Files & Code Section:


Encryption key management file

Cloud storage API credentials"

Prompt 17 — Automating Insider Threat Detection

Backstory: A recently resigned employee downloaded large volumes of data before leaving.

Goal: Detect unusual internal data access patterns.

Prompt:

"You are an Insider Threat Monitoring Specialist. I want a system that flags abnormal access activity by employees.

Your task:


1. Collect access logs from file servers, databases, and cloud storage.

2. Identify sudden spikes in file downloads or sensitive data access.

3. Compare against the user’s historical activity patterns.

4. Flag anomalies and send alerts to security admins.

5. Log all incidents for investigation.

Output format: Threat detection script + anomaly detection rules + alert system.

Input Files & Code Section:


Access log API endpoints

User activity baseline data CSV

Email/SMS API credentials"

Prompt 18 — Automating Compliance Document Management

Backstory: You must submit ISO 27001 compliance reports annually, but collecting required documents is messy.

Goal: Automate collection and organisation of compliance evidence.

Prompt:

"You are a Compliance Automation Specialist. I want a system that fetches logs, audit reports, and policy documents from multiple systems into one folder.

Your task:


1. Connect to APIs for security tools, HR systems, and monitoring platforms.

2. Download latest compliance-related files.

3. Store them in a structured folder by category and date.

4. Generate a manifest listing all collected documents.

5. Zip and archive the folder.

Output format: Document collection script + manifest file + folder structure template.

Input Files & Code Section:


API credentials for each system

Compliance checklist JSON"

Prompt 19 — Automating Ransomware Simulation Drills

Backstory: You want your IT team prepared for ransomware attacks, but training is irregular.

Goal: Automate simulated ransomware drills.

Prompt:

"You are a Cybersecurity Training Automation Engineer. I want a script that simulates a ransomware infection without actually encrypting files.

Your task:


1. Rename and lock sample files in a sandbox environment.

2. Display a mock ransom note.

3. Test the IT team’s incident response process.

4. Record time taken to respond.

5. Generate a performance report.

Output format: Simulation script + ransom note template + performance report.

Input Files & Code Section:


Sandbox environment setup file

Sample file set"

Prompt 20 — Automating API Security Testing

Backstory: Your company’s APIs are public-facing, and you want to test them regularly for vulnerabilities.

Goal: Create an automated API penetration testing tool.

Prompt:

"You are an API Security Testing Specialist. I want a script that runs OWASP API Security Top 10 checks on all company APIs.

Your task:


1. Load list of API endpoints from a file.

2. Run tests for authentication flaws, excessive data exposure, and injection attacks.

3. Record findings in a structured report.

4. Notify developers of high-risk vulnerabilities.

5. Store results for trend analysis.

Output format: API security scan script + vulnerability report + notification system.

Input Files & Code Section:


API endpoint list CSV

API security rules JSON"

Prompt 21 — Automating Cloud Security Policy Enforcement

Backstory: Your cloud storage contains sensitive client contracts, but some employees make files public by mistake.

Goal: Automatically detect and fix misconfigured cloud permissions.

Prompt:

"You are a Cloud Security Automation Specialist. I want a system that scans all files in Google Drive/AWS S3 for public access and restricts them to approved users only.

Your task:


1. Connect to the cloud storage API.

2. Identify files/folders with public sharing enabled.

3. Automatically remove public access.

4. Notify the file owner about the change.

5. Log all permission changes for audits.

Output format: Permission scan script + remediation log + owner notification email template.

Input Files & Code Section:


Cloud storage API credentials

Approved user list CSV

Notification email template"

Prompt 22 — Automating Incident Response Playbook Execution

Backstory: In case of a security breach, your IT team follows a manual checklist, which delays containment.

Goal: Automate the first 10 minutes of incident response.

Prompt:

"You are a Security Incident Automation Engineer. I want a system that executes predefined playbook actions when a breach is detected.

Your task:


1. Receive breach alert from SIEM (Security Information and Event Management) tool.

2. Isolate affected servers from the network.

3. Collect logs and system snapshots.

4. Notify the security team and management.

5. Update the incident tracking system.

Output format: Incident response script + action log + notification system.

Input Files & Code Section:


SIEM API credentials

Server isolation commands script

Incident tracking tool API key"

Prompt 23 — Automating Encrypted Chat for Sensitive Communications

Backstory: Your legal team sometimes needs to chat securely with external lawyers, but regular Slack channels are not safe enough.

Goal: Provide an automated, temporary encrypted chat channel.

Prompt:

"You are a Secure Communications Automation Specialist. I want a tool that creates an encrypted chat room that expires after 24 hours.

Your task:


1. Generate a secure chat room via API (e.g., Matrix, Rocket.Chat).

2. Require password-protected entry.

3. Enable end-to-end encryption for all messages.

4. Automatically delete the chat room and logs after expiry.

5. Email participants the join link and password.

Output format: Chat room creation script + deletion automation + participant email template.

Input Files & Code Section:


Secure chat API credentials

Participant email list CSV"

Prompt 24 — Automating Malware File Scanning for Uploads

Backstory: Your website allows file uploads for client documents, but there’s a risk of malicious files being uploaded.

Goal: Automatically scan all uploaded files for malware.

Prompt:

"You are a File Security Automation Engineer. I want an integration that scans each uploaded file with a malware detection API before it’s stored.

Your task:


1. Intercept file uploads via the web application backend.

2. Scan files using VirusTotal or ClamAV API.

3. Reject and quarantine suspicious files.

4. Notify the uploader about rejection.

5. Log scan results for audits.

Output format: File scanning script + quarantine folder setup + log file format.

Input Files & Code Section:


Malware scanning API credentials

File storage path configuration

Notification email template"

Prompt 25 — Automating Security Patch Deployment

Backstory: A zero-day vulnerability was discovered last month, but patching all systems took your team over a week.

Goal: Deploy security patches automatically across all servers.

Prompt:

"You are a Patch Management Automation Specialist. I want a script that applies critical security patches across all systems as soon as they’re available.

Your task:


1. Check vendor API or repositories for new patches.

2. Download and install patches automatically.

3. Reboot systems if required, during off-hours.

4. Notify admins of patch completion.

5. Maintain a patch history log.

Output format: Patch automation script + reboot schedule + patch log.

Input Files & Code Section:


Server list CSV

Patch repository URLs

Admin email list"






