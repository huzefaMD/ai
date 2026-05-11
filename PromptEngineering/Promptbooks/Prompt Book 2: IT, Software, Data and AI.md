Coding & Debugging

Prompt 1 — Code Review & Optimisation Plan

"You are a senior software engineer with expertise in [programming language/framework]. I have a codebase for a [type of application — e.g., e-commerce site, chatbot, mobile app] that works but runs slowly.
Review the code for:


1. Inefficient loops or redundant logic.

2. Poor memory management.

3. Opportunities to replace custom code with standard libraries.

4. Security vulnerabilities (SQL injection, XSS).

5. Best practices for scalability.

Provide output in 2 sections: a table of issues (with line numbers & problem description) and an optimised code snippet for each fix."

Prompt 2 — Bug Reproduction & Fix Documentation

"You are a QA (Quality Assurance) automation tester and developer. I have a bug where [describe bug behaviour] in my [framework/app type].
Create a debugging report that includes:


Exact steps to reproduce the bug.

Screenshots or logs showing the issue.

The suspected root cause in the code.

The corrected code segment.

Unit test cases to ensure the bug doesn’t reappear.

Output in debugging report format with code blocks."

Prompt 3 — Multi-Language Code Conversion

"You are a cross-platform developer. Convert my [programming language] code for [feature/function] into [target language], ensuring:


Exact feature parity.

Proper syntax & library usage in the target language.

Equivalent performance or better.

Inline comments explaining logic.

A quick performance test script in the target language.

Output in side-by-side original vs converted code format."

Prompt 4 — Algorithm Efficiency Upgrade

"You are a competitive programming expert. My current [sorting/searching/matching/etc.] algorithm in [language] works but is slow on large datasets.
Optimise it by:


Suggesting a faster algorithm (e.g., replacing bubble sort with merge sort).

Explaining time & space complexity differences.

Providing optimised code.

Writing performance benchmarks comparing both versions.

Output in comparative performance report format."

Prompt 5 — Debugging API Integration Issues

"You are an API integration specialist. My app in [language/framework] fails to fetch data from [API name] correctly.
Diagnose the problem by:


Reviewing my API request code.

Checking authentication & endpoint issues.

Suggesting correct request format with example.

Adding error handling for network failures.

Writing a test function to validate the fix.

Output in debugging log + corrected code block."

Prompt 6 — Code Refactoring for Readability & Maintainability

"You are a senior code architect. Refactor my [language/framework] code for [feature/function] so it is:


Easier to read with proper indentation & naming conventions.

Modularised into reusable functions or classes.

Documented with meaningful comments.

Compliant with [specific coding standard, e.g., PEP8 for Python].

Unit tested to ensure functionality remains unchanged.

Output in before/after code comparison format with a change log."

Prompt 7 — Legacy Code Modernisation Plan

"You are a legacy systems upgrade specialist. My [old programming language or framework] code needs to be upgraded to [modern equivalent] while preserving functionality.
Include:


Identification of outdated functions/libraries.

Recommended replacements & modern equivalents.

Compatibility concerns with the new environment.

Performance benefits after modernisation.

Step-by-step migration plan with testing checkpoints.

Output in legacy-to-modern migration report format."

Prompt 8 — Continuous Integration (CI) Debugging Setup

"You are a DevOps engineer. Configure a CI pipeline for my [language/framework] project to automatically run code linting, unit tests, and integration tests whenever code is pushed.
Include:


Recommended CI tool (GitHub Actions, Jenkins, GitLab CI).

Pipeline configuration script.

Test coverage reporting setup.

Common CI errors & how to fix them.

Notification integration (Slack/Email) for failed builds.

Output in pipeline YAML file + setup guide."

Prompt 9 — Memory Leak Detection & Fix

"You are a performance optimisation engineer. Analyse my [language/framework] application for memory leaks and:


Identify possible causes from code structure.

Suggest profiling tools (Valgrind, Perf, Chrome DevTools).

Provide a step-by-step method to reproduce memory growth.

Fix the leak with corrected code examples.

Suggest long-term prevention strategies.

Output in diagnostic report + corrected code samples."

Prompt 10 — Multi-Threading Bug Resolution

"You are a concurrency programming specialist. My [language/framework] application faces race conditions and deadlocks.
Include:


Detailed explanation of the issue.

Steps to identify which thread is causing the block.

Corrected thread-safe code.

Recommended locking or async patterns.

Performance benchmarks after fix.

Output in bug analysis + updated code format."

Prompt 11 — Automated Unit Test Generation

"You are a test automation engineer. Write automated unit test scripts for my [language/framework] code covering [feature/function].
Include:


Test cases for normal, boundary, and error conditions.

Assertions for expected output.

Mock data creation.

Code coverage percentage target (e.g., >80%).

How to run tests in CI/CD pipeline.

Output in ready-to-run test script format."

Prompt 12 — SQL Query Debugging & Optimisation

"You are a database performance engineer. Optimise my slow SQL queries for [database type: MySQL, PostgreSQL, etc.].
Include:


Query execution plan analysis.

Indexing strategy.

Query rewriting for speed.

Caching recommendations.

Before/after execution time comparison.

Output in query optimisation report with revised SQL statements."

Prompt 13 — Cross-Browser Bug Fix Plan

"You are a front-end debugging expert. My web app works on Chrome but fails in Firefox & Safari.
Include:


List of browser compatibility issues.

Code fixes using cross-browser safe APIs.

CSS vendor prefixing guide.

Polyfill recommendations for unsupported features.

Testing checklist for all major browsers.

Output in browser compatibility report + fixed code snippets."

Prompt 14 — API Rate Limit Error Resolution

"You are an API performance consultant. My app hits rate limits when fetching data from [API name].
Include:


How to detect rate limit headers.

Backoff strategies & caching techniques.

Batch request examples.

Code modifications for retry logic.

Test scenarios to confirm the fix.

Output in rate limit handling guide + updated code."

Prompt 15 — Deployment Bug Fix Checklist

"You are a deployment engineer. My application works locally but fails in production.
Include:


Environment variable checks.

Dependency version mismatches.

Server configuration issues.

Build process verification.

Automated rollback setup.

Output in deployment debugging checklist format."

Prompt 16 — Version Control Conflict Resolution

"You are a Git (Version Control) expert. Resolve merge conflicts in my [repository name] while ensuring no functionality loss.
Include:


Step-by-step conflict resolution process.

Commit best practices to avoid future issues.

Branch management guidelines.

Git command examples for common scenarios.

Output in merge resolution guide with Git commands."

Prompt 17 — Security Vulnerability Patch Plan

"You are a cybersecurity code auditor. Review my [language/framework] code for vulnerabilities like SQL injection, XSS, and CSRF.
Include:


Vulnerability list with risk levels.

Code patches with secure alternatives.

OWASP (Open Web Application Security Project) best practice checklist.

Security testing tools list.

Output in vulnerability report + patched code samples."

Prompt 18 — Cloud Function Debugging Guide

"You are a cloud application developer. Debug my [AWS Lambda / Google Cloud Function / Azure Function] which is failing intermittently.
Include:


Log analysis methods.

Error pattern detection.

Code changes for reliability.

Testing with local emulators.

Deployment steps after fix.

Output in debugging flowchart + corrected function code."

Prompt 19 — Mobile App Crash Analysis

"You are a mobile app debugging expert. Analyse my [Android/iOS] app for crash reports related to [feature/function].
Include:


Crash log interpretation.

Root cause identification.

Code corrections.

Device-specific fixes.

Testing plan for all OS versions.

Output in crash report + updated code block."

Prompt 20 — Real-Time Error Monitoring Setup

"You are a site reliability engineer. Set up a real-time error tracking system for my [language/framework] app.
Include:


Recommended monitoring tools (Sentry, New Relic, Datadog).

Setup steps for integration.

Error categorisation for alerts.

Dashboard layout suggestions.

Weekly reporting format.

Output in tool setup guide + dashboard screenshot mockup."

Prompt 21 — Data Processing Script Debugging

"You are a data engineer. My Python ETL (Extract, Transform, Load) script fails at the transformation stage.
Include:


Step-by-step debugging for data type mismatches.

Handling null values & schema changes.

Logging setup for error tracking.

Optimised data transformation logic.

Unit tests for validation.

Output in debugging report + corrected script."

Prompt 22 — Infinite Loop Prevention in Code

"You are a software safety expert. Analyse my [language] code for infinite loop risks and fix them.
Include:


Detection of loops without termination conditions.

Corrected loop conditions.

Safeguards to prevent reoccurrence.

Performance benchmarks after fix.

Output in before/after code format."

Prompt 23 — Automated Code Documentation Generator

"You are a documentation automation consultant. Set up an auto-documentation system for my [language/framework] project.
Include:


Recommended tools (e.g., JSDoc, Sphinx).

Integration into CI/CD pipeline.

Style guide for consistent doc formatting.

Sample generated documentation.

Output in documentation setup guide + example output."

Prompt 24 — Debugging Scheduler & Cron Job Failures

"You are a backend engineer. My scheduled tasks in [language/framework] fail intermittently.
Include:


Log analysis to find failure points.

Corrected cron expressions.

Error handling logic.

Monitoring alerts setup.

Retry mechanism.

Output in debugging report + fixed scheduling script."

Prompt 25 — Codebase Technical Debt Reduction Plan

"You are a senior software architect. Analyse my [language/framework] codebase for technical debt and create a 3-month cleanup roadmap.
Include:


List of outdated dependencies.

Code smells & fixes.

Testing coverage improvement.

Refactoring priorities.

Risk mitigation plan.

Output in technical debt report + phased action plan."


Data Analysis & Visualization

Prompt 1 — Full Exploratory Data Analysis (EDA) with Actionable Insights

"You are a Senior Data Analyst with expertise in Python (Pandas, NumPy, Matplotlib, Seaborn) and data storytelling. I have a dataset in CSV format containing sales data for an Indian retail chain (2018–2024) with 50,000 rows and 12 columns (date, location, category, units sold, price, discount, etc.).

Your task:


1. Import and inspect the dataset to understand structure, data types, and column meanings.

2. Generate summary statistics for both numerical and categorical columns, highlighting anomalies.

3. Detect missing values, quantify them column-wise, and suggest domain-specific imputation or removal strategies.

4. Identify outliers using both statistical (Z-score, IQR) and visual (boxplots) methods, explaining potential business causes.

5. Create a correlation heatmap for numerical features and explain the top 5 strongest relationships in simple business terms.

6. Provide at least 3 actionable business insights and possible next analytical steps.

Output format: A Jupyter Notebook with fully commented code, inline plots, and a concluding Markdown section explaining insights in non-technical language."

Prompt 2 — Interactive KPI Dashboard for Decision-Makers

"You are a Business Intelligence (BI) Dashboard Expert skilled in Power BI, Tableau, and Google Data Studio. I have quarterly sales data for multiple product categories in India for the last 5 years.

Your task:


1. Identify 5–7 key performance indicators (KPIs) relevant to retail business health (e.g., total revenue, gross margin, average order value, conversion rate).

2. Design an interactive dashboard layout showing KPIs as cards at the top, trend charts in the middle, and filters (by time, category, location) on the side.

3. Include drill-down capability so a user can click on a KPI and view detailed breakdowns by category, region, or month.

4. Add a geographic heatmap showing sales distribution across states, with hover tooltips.

5. Include an export-to-PDF function for monthly reporting.

Output format: Provide a step-by-step dashboard build guide (tool-agnostic), a mockup diagram of the dashboard, and sample formulas for KPI calculations."

Prompt 3 — Predictive Sales Forecasting with Model Comparison

"You are a Data Scientist specialising in forecasting. I have monthly sales data for an e-commerce platform from January 2018 to December 2024.

Your task:


1. Perform time-series decomposition to analyse trend, seasonality, and residual components.

2. Build at least two forecasting models (ARIMA/SARIMA and Facebook Prophet).

3. Compare model performance using RMSE (Root Mean Squared Error) and MAPE (Mean Absolute Percentage Error).

4. Plot actual vs predicted sales for both models and highlight differences.

5. Provide recommendations for which model to deploy, along with a 12-month sales forecast.

Output format: A Python Jupyter Notebook with all code, plots, and a Markdown cell comparing models with business-friendly explanations."

Prompt 4 — Automated Data Cleaning and Preprocessing Script

"You are a Data Preprocessing Automation Specialist skilled in Python and Pandas. I have a CSV file containing a mix of numerical, categorical, and datetime fields, with missing values and inconsistent formats.

Your task:


1. Write a reusable Python script to detect and handle missing values using mean/median/mode or forward-fill/backward-fill depending on the column type.

2. Remove duplicate rows and flag near-duplicates for manual review.

3. Normalise numerical columns (min-max or z-score scaling) and encode categorical columns (label or one-hot encoding as appropriate).

4. Convert date columns to proper datetime format and extract features (day, month, year, day-of-week).

5. Save the cleaned dataset to a new CSV file with a timestamped filename.

Output format: A fully commented Python script that can be reused for different datasets, with clear function definitions."

Prompt 5 — Business Data Storytelling for Stakeholder Reports

"You are a Business Data Storyteller with experience in creating executive summaries from analytical results. I have analysed customer purchase behaviour for my online store and want to present findings to the leadership team.

Your task:


1. Frame the analysis as a story — starting with the problem, key findings, and implications.

2. Select only the 5–7 most impactful visuals from the analysis, ensuring they are simple and easy to understand.

3. Explain each chart in 1–2 sentences highlighting what matters for the business.

4. Conclude with 3 actionable recommendations, each tied to a business outcome (e.g., revenue growth, cost saving).

5. Create a 2-slide PowerPoint layout that can be used in a leadership meeting.

Output format: A concise text storyboard + slide content that a non-technical executive can understand at a glance."

Prompt 6 — Real-Time Data Monitoring and Alerts

"You are a Real-Time Data Monitoring Specialist skilled in tools like Grafana, Kibana, and Power BI Streaming Dataflows. I operate a logistics company with live GPS and delivery data flowing in every 15 seconds.

Your task:


1. Design a real-time dashboard that displays vehicle location, delivery status, and delays in near real-time.

2. Implement colour-coded alerts for deliveries delayed beyond SLA (Service Level Agreement) thresholds.

3. Add trend visualisations for daily delivery count, average delivery time, and % on-time rate.

4. Integrate automated alerts via email and SMS for key managers when KPIs cross thresholds.

5. Ensure the system can handle data spikes (e.g., festival season).

Output format: A visual architecture diagram + tool integration plan + example SQL queries for alert generation."

Prompt 7 — Sentiment Analysis of Customer Feedback

"You are an NLP (Natural Language Processing) Specialist with expertise in Python libraries like NLTK, SpaCy, and Transformers. I have 50,000 customer reviews collected over 2 years.

Your task:


1. Clean and preprocess the text (remove stopwords, lemmatise, handle emojis).

2. Classify sentiment into positive, neutral, and negative categories using a pre-trained BERT model.

3. Create visualisations:

    1. Sentiment distribution pie chart.

    2. Monthly sentiment trend line chart.

    3. Word cloud for each sentiment category.

5. Identify top 5 positive and top 5 negative themes with example reviews.

6. Provide actionable recommendations for product/service improvement based on sentiment patterns.

Output format: A Jupyter Notebook with code, charts, and a Markdown insights summary."

Prompt 8 — Comparative Category Performance Report

"You are a Business Performance Analyst. I have category-wise sales data for 10 product categories over the last 3 years.

Your task:


1. Calculate YoY (Year-over-Year) and MoM (Month-over-Month) growth rates for each category.

2. Rank categories based on revenue, profit margin, and units sold.

3. Create a dashboard view showing category trends side-by-side.

4. Highlight top 3 performing categories and bottom 3 lagging categories.

5. Suggest category-level actions to boost sales and margins for underperformers.

Output format: A comparative analysis table + dashboard layout mockup + 1-page action plan."

Prompt 9 — Correlation and Causation Testing

"You are a Data Scientist with a focus on statistical inference. I have a dataset on marketing spend (TV, social media, influencer, print) and corresponding sales figures.

Your task:


1. Calculate correlation coefficients for each marketing channel vs sales.

2. Perform hypothesis testing to check statistical significance (p-values).

3. Run a multiple regression analysis to see which channels predict sales best.

4. Visualise results using scatter plots and regression lines.

5. Provide a plain-language explanation of findings for non-technical stakeholders.

Output format: Jupyter Notebook with plots + regression output table + simplified insights brief."

Prompt 10 — Customer Churn Prediction and Retention Strategy

"You are a Customer Analytics Expert specialising in churn modelling. I have SaaS customer data including sign-up date, usage frequency, support tickets, and payment history.

Your task:


1. Define churn for my business context (e.g., inactive for 60 days).

2. Engineer predictive features from usage and payment history.

3. Build a classification model (Logistic Regression, Random Forest, or XGBoost) to predict churn probability.

4. Evaluate using accuracy, precision, recall, and ROC-AUC.

5. Suggest retention strategies for the top 20% at-risk customers.

Output format: Python Notebook with code + confusion matrix + strategic retention plan."

Prompt 11 — Data Visualization Best Practices Guide

"You are a Data Visualization Trainer. Prepare a best practices guide for visualising financial performance data for stakeholders.

Your task:


1. Recommend which chart types to use for time-series, category comparison, and part-to-whole analysis.

2. Suggest an accessible, colour-blind-friendly palette.

3. Explain how to avoid misleading scales and data distortion.

4. Include 3 examples of excellent visualisations and explain why they work.

5. Provide 3 poor visualisation examples and show corrected versions.

Output format: A 5-page PDF guide with do’s and don’ts + visual examples."

Prompt 12 — Multi-Dataset Integration Workflow

"You are a Data Integration Specialist skilled in ETL (Extract, Transform, Load) processes. I have three datasets:


 Customer demographics (Excel)

 Purchase history (CSV)

 Web analytics data (Google Analytics export)

Your task:


1. Identify common keys for merging datasets.

2. Clean and standardise column formats and naming.

3. Join datasets into a master table.

4. Perform initial descriptive analysis on combined data.

5. Suggest 3 insights achievable only after combining data.

Output format: Python Notebook with ETL code + final merged dataset snapshot + insight summary."

Prompt 13 — Interactive Geo-Spatial Sales Mapping

"You are a GIS (Geographic Information Systems) Analyst. I have state-wise sales data for India for the past 12 months.

Your task:


1. Create an interactive map showing sales density using a colour gradient.

2. Add filters for month, product category, and sales rep.

3. Display state-level tooltips with key KPIs (revenue, units sold, growth rate).

4. Enable comparison mode for two selected states.

5. Provide export options (PNG, PDF).

Output format: Dashboard implementation guide + sample data visualisation screenshot."

Prompt 14 — Industry Benchmark Comparison with Gap Analysis

"You are a Market Intelligence Analyst specialising in competitive benchmarking. I have my company’s quarterly performance metrics for revenue, gross margin, and customer acquisition rate, and I have benchmark data for top 5 competitors.

Your task:


1. Normalise all data for fair comparison (e.g., currency conversion, adjusting for fiscal year differences).

2. Create comparative bar charts showing my company vs each competitor for each KPI (Key Performance Indicator).

3. Calculate % variance from industry average for each KPI.

4. Identify areas where my company is above average and where it’s lagging.

5. Provide 5 targeted recommendations to close performance gaps.

Output format: A 2-page PDF competitive report with visual comparisons, an executive summary, and a prioritised action list."

Prompt 15 — Data Pipeline Performance Optimisation Plan

"You are a Data Engineer experienced in optimising ETL (Extract, Transform, Load) pipelines for speed and efficiency. I have a nightly pipeline that ingests sales, inventory, and customer data into a central warehouse.

Your task:


1. Profile the current pipeline to identify slow queries, inefficient joins, and bottleneck processes.

2. Recommend improvements in query optimisation, indexing, and caching.

3. Suggest parallelisation or batch processing strategies to reduce runtime.

4. Propose monitoring tools to track pipeline health and error rates.

5. Provide an example optimised SQL query and ETL script snippet.

Output format: A technical optimisation plan with a “before vs after” runtime projection chart and sample code."

Prompt 16 — Social Media Engagement Analytics Dashboard

"You are a Digital Analytics Expert skilled in API integrations and BI dashboarding. I have social media engagement data from Facebook, Instagram, and LinkedIn for the past 12 months.

Your task:


1. Create a unified dashboard showing platform-wise engagement metrics (likes, comments, shares, saves).

2. Add a filter to view engagement by post type (video, carousel, single image, story).

3. Highlight top 10 performing posts across all platforms with engagement breakdown.

4. Add follower growth trend lines for each platform.

5. Include an insights section suggesting which content format drives the highest engagement.

Output format: Dashboard wireframe + API integration guide + engagement insights report."

Prompt 17 — Real Estate Market Analysis with Investment Insights

"You are a Real Estate Data Analyst with expertise in property market trends. I have a dataset of property sales in [city] for the last 5 years with columns for location, property type, size, sale price, and date.

Your task:


1. Analyse price trends by property type (apartment, villa, plot).

2. Map high-growth neighbourhoods using price appreciation over time.

3. Identify seasonality patterns in sales volume.

4. Calculate ROI projections for top 5 emerging areas.

5. Provide investment recommendations for buyers targeting high rental yield vs capital appreciation.

Output format: A PDF market report with heatmaps, trend charts, and a 1-page “Investor Recommendations” summary."

Prompt 18 — Healthcare Operational Efficiency Analysis

"You are a Healthcare Data Analyst working on hospital efficiency improvement. I have anonymised patient visit data, bed occupancy records, and treatment timelines for the past 2 years.

Your task:


1. Calculate average patient wait time, treatment time, and discharge time.

2. Create bed occupancy rate visualisations by department.

3. Identify peak patient inflow periods and staffing shortages.

4. Suggest scheduling optimisations to reduce bottlenecks.

5. Recommend operational changes to improve patient throughput without compromising care quality.

Output format: A dashboard layout plan + operational improvement report."

Prompt 19 — Sales Funnel Drop-off Analysis

"You are a Marketing Data Analyst focused on conversion rate optimisation. I have e-commerce funnel data for the last quarter showing visits, product views, add-to-cart events, checkout starts, and purchases.

Your task:


1. Calculate conversion rates for each funnel stage.

2. Identify the stage with the highest drop-off rate and quantify the loss in potential revenue.

3. Analyse patterns in drop-off by device type, browser, and traffic source.

4. Suggest at least 5 tactics to improve conversions at the weakest stage.

5. Provide a visual funnel chart showing current vs projected performance if improvements are implemented.

Output format: A funnel analysis dashboard + improvement recommendation document."

Prompt 20 — Education Performance Dashboard for Institutions

"You are an Education Analytics Specialist. I have school-level student performance data for grades, attendance, and extracurricular participation across multiple branches.

Your task:


1. Create visualisations showing average performance by subject and grade level.

2. Add attendance heatmaps highlighting periods of low attendance.

3. Identify correlations between extracurricular participation and academic performance.

4. Highlight top 5 branches in overall performance and bottom 5 for improvement focus.

5. Recommend targeted interventions for low-performing schools.

Output format: Dashboard wireframe + insights brief for school management."

Prompt 21 — Energy Consumption Pattern Analysis for Cost Saving

"You are an Energy Data Analyst. I have hourly electricity consumption data for a manufacturing facility over 24 months.

Your task:


1. Identify peak and off-peak consumption periods.

2. Analyse seasonal patterns in energy usage.

3. Quantify potential savings from shifting operations to off-peak hours.

4. Suggest renewable energy integration opportunities.

5. Create a projection model for energy cost savings over the next 12 months.

Output format: PDF energy audit report + visual trend charts + savings projection table."

Prompt 22 — Market Basket Analysis for Cross-Selling

"You are a Retail Data Mining Specialist. I have point-of-sale transaction data with item-level details for the past 12 months.

Your task:


1. Use association rule mining (Apriori or FP-Growth) to identify frequent item combinations.

2. Calculate support, confidence, and lift for each rule.

3. Highlight top 10 product pairs with highest cross-sell potential.

4. Suggest bundle offers based on analysis.

5. Project potential revenue increase from implementing top 3 bundles.

Output format: Association rules table + actionable cross-sell strategy document."

Prompt 23 — Website Traffic and Conversion Analytics

"You are a Web Analytics Consultant. I have Google Analytics data for my e-commerce site over the past 6 months.

Your task:


1. Identify top 5 traffic sources and their respective conversion rates.

2. Analyse bounce rate, average session duration, and pages per session.

3. Map the customer journey from landing page to purchase.

4. Highlight underperforming landing pages and suggest optimisation strategies.

5. Provide projected improvement metrics if changes are implemented.

Output format: Data Studio dashboard layout + optimisation recommendations report."

Prompt 24 — Manufacturing Process Efficiency Visualisation

"You are a Manufacturing Data Engineer. I have IoT sensor data for multiple machines in a production line over the past year.

Your task:


1. Visualise machine uptime/downtime as a Gantt chart.

2. Identify bottlenecks in production flow.

3. Calculate defect rates per machine and per shift.

4. Recommend preventive maintenance schedules.

5. Suggest workflow changes to increase throughput without adding resources.

Output format: Factory floor dashboard layout + process improvement plan."

Prompt 25 — Financial Performance Storytelling for Investors

"You are a Financial Data Storyteller. I have quarterly income statements, balance sheets, and cash flow statements for the past 3 years.

Your task:


1. Visualise revenue, gross profit, and net profit trends over time.

2. Calculate key financial ratios (ROE, ROA, current ratio, debt-to-equity) and explain their meaning.

3. Highlight major changes in expenses or revenue sources.

4. Provide a year-over-year growth summary.

5. Frame findings in a narrative that inspires investor confidence.

Output format: Investor-ready slide deck with visuals, ratio analysis, and growth narrative."


API Integration & Automation

Prompt 1 — Connecting Multiple APIs for Unified Data

"You are an API Integration Engineer with expertise in REST (Representational State Transfer) and GraphQL APIs. I want to create a single automated workflow that combines data from Google Sheets, Shopify, and Google Analytics APIs.

Your task:


1. Authenticate each API using OAuth 2.0 and store tokens securely.

2. Pull product sales data from Shopify, website traffic data from Google Analytics, and inventory data from Google Sheets.

3. Merge the datasets on product ID and date fields for unified reporting.

4. Schedule the workflow to run daily at midnight using a cron job or cloud scheduler.

5. Include logging for errors and success status.

Output format: Python script with step-by-step API calls, merged dataset output as CSV, and instructions for deployment in a cloud environment (AWS Lambda or Google Cloud Functions)."

Prompt 2 — Automating Social Media Posting via API

"You are a Social Media Automation Specialist experienced with the Meta Graph API, LinkedIn API, and Twitter API (now X API). I manage 3 platforms and want to post the same content automatically at scheduled times.

Your task:


1. Authenticate all platform APIs and handle rate limits.

2. Create a reusable function that posts text, images, and videos from a single JSON file.

3. Add an option to customise captions per platform for optimal engagement.

4. Schedule posts using a job scheduler (like APScheduler in Python).

5. Log post IDs and engagement metrics for tracking.

Output format: Python automation script + setup instructions + sample JSON template for post content."

Prompt 3 — Automating Data Entry from Web Forms to CRM

"You are a CRM Workflow Automation Engineer skilled in HubSpot, Salesforce, and Zoho CRM APIs. I receive customer leads from a website form and want them automatically added to my CRM with tags for campaign tracking.

Your task:


1. Set up a webhook to receive form submissions in real time.

2. Transform form data into the CRM’s required JSON format.

3. Use the CRM API to create a new lead record with appropriate tags (e.g., “WebForm2024”).

4. Send a confirmation email to the lead using the CRM’s email API.

5. Log each successful lead creation in a Google Sheet via API.

Output format: API workflow diagram + example webhook handler code + CRM API call scripts."

Prompt 4 — Email Marketing Automation with API

"You are an Email Marketing Automation Expert familiar with Mailchimp, SendGrid, and ActiveCampaign APIs. I want to send a weekly newsletter automatically using my Google Sheets contact list.

Your task:


1. Connect Google Sheets API to read subscriber list.

2. Connect the chosen email service API and authenticate securely.

3. Pull the email template from a stored HTML file.

4. Send emails in batches to avoid exceeding API rate limits.

5. Update the Google Sheet with a “last sent” timestamp for each contact.

Output format: Python/Node.js script + deployment guide + API keys & secrets handling instructions."

Prompt 5 — Automating File Backups to Cloud Storage

"You are a Cloud Automation Engineer skilled in AWS S3, Google Drive, and Dropbox APIs. I have a folder on my local machine containing financial reports that must be backed up daily to all three cloud platforms.

Your task:


1. Authenticate with all three cloud APIs.

2. Compress the local folder into a timestamped ZIP file.

3. Upload the ZIP file to each cloud platform.

4. Send an email notification with file URLs after successful upload.

5. Log the backup details in a CSV file for auditing.

Output format: Shell/Python script + setup instructions + automation scheduling plan."

Prompt 6 — Real-Time Stock Price Tracker with Alerts

"You are a Financial Data Automation Specialist experienced in Alpha Vantage, Yahoo Finance, and TradingView APIs. I want to track live stock prices for a watchlist of 10 Indian companies and receive alerts when prices change more than ±3% in a day.

Your task:


1. Connect to the stock price API with authentication.

2. Create a script to fetch and store real-time prices every 5 minutes.

3. Compare the current price with the opening price for percentage change.

4. Trigger an email/SMS alert when the ±3% threshold is crossed.

5. Store all intraday data in a CSV for end-of-day analysis.

Output format: Python script + CSV logging + alert system integration plan.

Input Files & Code Section:


API Key file (api_keys.json) for Alpha Vantage/Yahoo Finance.

watchlist.csv containing company ticker symbols.

Placeholder for email/SMS sending function."

Prompt 7 — Automating PDF Invoice Creation from Sales Data

"You are a Document Automation Engineer skilled in ReportLab, wkhtmltopdf, and Google Docs API. I have daily sales data in CSV format and need automatically generated PDF invoices sent to customers.

Your task:


1. Read the CSV to fetch customer details, products, and prices.

2. Generate a branded PDF invoice for each customer.

3. Save the invoice locally and in Google Drive.

4. Email the invoice to the customer with a personalised message.

5. Log invoice status (sent, pending, failed) in a Google Sheet.

Output format: Python script + invoice PDF template + Google Drive integration guide.

Input Files & Code Section:


sales_data.csv with customer and order details.

invoice_template.html for branding.

API credentials for Google Drive and Gmail."

Prompt 8 — Weather-Based Automation for Agriculture

"You are an Agricultural IoT Automation Specialist skilled in OpenWeatherMap API and smart irrigation systems. I want to automate irrigation based on real-time weather data.

Your task:


1. Connect to the OpenWeatherMap API to fetch daily forecasts.

2. If rainfall probability is >70%, delay irrigation by 24 hours.

3. If temperature >35°C, schedule an extra watering cycle.

4. Send an SMS to the farmer confirming the decision.

5. Log all actions in a daily report file.

Output format: IoT control script + weather API integration + action logging.

Input Files & Code Section:


API key file for OpenWeatherMap.

farm_config.json with field size, crop type, and irrigation limits.

Placeholder for SMS gateway integration code."

Prompt 9 — Automating YouTube Video Uploads

"You are a YouTube API Automation Specialist. I want to upload videos from a folder to YouTube with titles, descriptions, and tags automatically pulled from a CSV file.

Your task:


1. Authenticate using YouTube Data API v3 with OAuth 2.0.

2. Loop through a folder containing video files.

3. Read metadata from a CSV (title, description, tags, privacyStatus).

4. Upload each video with the corresponding metadata.

5. Log upload IDs and publish status.

Output format: Python script + CSV metadata mapping + OAuth setup guide.

Input Files & Code Section:


video_metadata.csv with columns for each video.

Folder path for video files.

client_secret.json for OAuth credentials."

Prompt 10 — Daily Currency Conversion Automation

"You are a Currency Data Automation Specialist. I want to fetch daily INR to USD, EUR, and GBP exchange rates and update them in my Google Sheet automatically.

Your task:


1. Connect to a currency exchange API (e.g., ExchangeRate-API).

2. Fetch latest conversion rates for INR to target currencies.

3. Write data to a specific Google Sheets cell range.

4. Include timestamp of last update.

5. Schedule script to run daily at 8 AM IST.

Output format: Python script + Google Sheets API integration + scheduler setup guide.

Input Files & Code Section:


API key file for ExchangeRate-API.

Google Sheets spreadsheet ID.

config.json for target currency list."

Prompt 11 — Automating Job Application Tracking

Backstory: You’re a 28-year-old marketing professional applying to multiple companies at once. Keeping track of applications manually is messy — you often forget where you applied, the status, or the interview schedule. You want AI and APIs to track everything automatically.

Goal: Build an automation that pulls application data from job portals (LinkedIn, Naukri.com) and updates it into a single Google Sheet dashboard daily.

Prompt:

"You are a Job Search Workflow Automation Engineer. I want an automated job application tracker that consolidates applications from LinkedIn Jobs and Naukri.com using their APIs/webhooks.

Your task:


1. Authenticate with LinkedIn API and Naukri.com’s developer API (or scrape data if no API exists).

2. Fetch job title, company name, date applied, status (applied, shortlisted, interview scheduled), and job link.

3. Push this data into a Google Sheet in structured columns.

4. Highlight rows where the application has been idle for >14 days.

5. Send me a daily email digest of new application updates.

Output format: Google Sheet dashboard + email digest example + API scripts.

Input Files & Code Section:


API credentials for LinkedIn and Naukri.com

Google Sheet ID and credentials JSON

Email SMTP settings for sending daily digest"

Prompt 12 — Automating Property Price Tracking for Investment

Backstory: You’re a 35-year-old professional looking to invest in property in Bangalore. Prices change fast and manual tracking is too slow. You want a tool that automatically fetches and compares prices across multiple real estate portals.

Goal: Build a daily property price tracker with alerts for deals under your budget.

Prompt:

"You are a Real Estate Data Automation Specialist skilled in integrating housing.com, magicbricks.com, and 99acres.com APIs.

Your task:


1. Fetch property listings for specified locations (e.g., Whitefield, Indiranagar) within a budget range.

2. Extract details — price, size (sqft), price per sqft, location link.

3. Store data in a Google Sheet with a “lowest price this week” column.

4. Trigger an SMS alert when a property price drops more than 5% from last week.

5. Generate a weekly PDF market trend report.

Output format: Google Sheet tracker + automated PDF report + SMS alert script.

Input Files & Code Section:


API credentials or scraping script for property portals

property_config.json with budget, preferred locations, size range

Google Sheets & Twilio SMS API credentials"

Prompt 13 — Automating Invoice Payment Reminders

Backstory: You run a small design agency. Clients often delay payments, and manually sending reminders eats up your evenings. You want an automated reminder system that sends polite follow-ups.

Goal: Build an API-based automation that sends reminders at 7, 14, and 21 days after invoice due date.

Prompt:

"You are a Business Workflow Automation Specialist. I want to automate client payment reminders using QuickBooks API and Gmail API.

Your task:


1. Pull unpaid invoice data from QuickBooks API with due dates.

2. Identify invoices past due by 7, 14, or 21 days.

3. Send a customised reminder email based on how late the payment is.

4. Log all sent reminders in a Google Sheet.

5. Mark the invoice in QuickBooks with “reminder sent” status.

Output format: Automated reminder script + email template files + logging spreadsheet.

Input Files & Code Section:


QuickBooks API credentials

Google API credentials for Gmail & Sheets

email_templates/ folder with HTML templates for 7, 14, 21 days"

Prompt 14 — Automating Resume Screening for Recruitment

Backstory: You’re an HR manager for a startup. Hundreds of resumes arrive daily. Manually screening them for skills is impossible. You need an API workflow that filters CVs based on required skills.

Goal: Automatically screen resumes and send shortlisted profiles to a hiring manager’s email.

Prompt:

"You are a Recruitment Automation Specialist. I want to integrate Google Drive API and an NLP model to process incoming resumes.

Your task:


1. Monitor a Google Drive folder for new resumes.

2. Extract text from PDFs/DOCs using an OCR/NLP API.

3. Match candidate skills with a given job description using keyword matching and semantic similarity.

4. Move shortlisted resumes to a “Shortlisted” folder.

5. Email a daily summary to the hiring manager with names and matched skills.

Output format: Resume screening script + summary email template + candidate matching report.

Input Files & Code Section:


Google Drive API credentials

Job description text file

API key for NLP/OCR service (e.g., Google Cloud Vision, OpenAI)"

Prompt 15 — Automating YouTube Comment Sentiment Analysis

Backstory: You’re a content creator with 500K subscribers. It’s impossible to read every comment and spot trends in audience sentiment.

Goal: Build an API workflow that pulls all new comments, runs sentiment analysis, and gives you a weekly trend report.

Prompt:

"You are a Social Media Analytics Automation Engineer. I want a system that fetches my YouTube video comments weekly, analyses sentiment, and creates a dashboard.

Your task:


1. Connect to YouTube Data API to fetch comments for all videos from the last 7 days.

2. Run sentiment analysis using a pre-trained model (e.g., VADER, BERT).

3. Categorise comments as positive, negative, or neutral.

4. Create visualisations showing weekly sentiment trends.

5. Generate a PDF report and store it in Google Drive.

Output format: Sentiment analysis notebook + dashboard + weekly PDF.

Input Files & Code Section:


YouTube API credentials

Sentiment analysis model file or package requirements

Google Drive API credentials"

Prompt 16 — Automating E-commerce Inventory Updates Across Platforms

Backstory: You sell products on Amazon, Flipkart, and your own Shopify store. Inventory changes fast, but updating each platform manually wastes hours and risks overselling.

Goal: Build an API automation that updates inventory levels across all platforms from a single source.

Prompt:

"You are an E-commerce API Integration Specialist. I want a single source of truth for my inventory, updated across Amazon, Flipkart, and Shopify in real time.

Your task:


1. Connect to all three platform APIs using secure authentication (API keys or OAuth).

2. Fetch the latest inventory count from my central warehouse database or Google Sheet.

3. Update product stock levels on each platform.

4. Send me an email if a product’s stock falls below a reorder threshold.

5. Log all updates with timestamp, product ID, and before/after quantities.

Output format: Inventory sync script + alert email template + update log file.

Input Files & Code Section:


API credentials for Amazon, Flipkart, and Shopify

inventory.csv or database connection details

Email SMTP settings for low-stock alerts"

Prompt 17 — Automating Customer Support Ticket Categorisation

Backstory: Your startup gets 200+ support emails daily. Agents waste time reading and assigning tickets manually.

Goal: Use APIs and AI to automatically categorise tickets and assign them to the right team.

Prompt:

"You are a Customer Service Workflow Automation Engineer. I want to integrate Gmail API, NLP (Natural Language Processing), and a ticketing system API (like Zendesk).

Your task:


1. Fetch new support emails via Gmail API.

2. Run NLP classification to detect category (Billing, Technical Issue, General Query, Complaint).

3. Create a ticket in Zendesk with the detected category.

4. Assign tickets to the relevant department queue.

5. Send an auto-response email to the customer with an estimated resolution time.

Output format: Categorisation script + Zendesk integration + auto-reply email templates.

Input Files & Code Section:


Gmail API credentials

NLP model or keyword mapping file

Zendesk API credentials"

Prompt 18 — Automating Daily Stock Market Newsletter

Backstory: You run a Telegram channel for stock market updates. Manually collecting news, stock prices, and analysis every morning is slow.

Goal: Generate and send a daily market summary via email and Telegram using APIs.

Prompt:

"You are a Financial Automation Developer. I want a daily 7:30 AM IST newsletter combining stock prices, market news, and a short AI-generated analysis.

Your task:


1. Connect to Yahoo Finance API for NIFTY 50, SENSEX, and top 10 stocks data.

2. Pull top 5 market news headlines from News API.

3. Use GPT API to generate a 150-word market analysis.

4. Send the report via Gmail API and post to a Telegram channel via Telegram Bot API.

5. Store all reports in a Google Drive folder for archiving.

Output format: Automated newsletter script + Telegram bot setup + daily report template.

Input Files & Code Section:


Yahoo Finance API key

News API key

OpenAI GPT API key

Gmail API and Telegram Bot credentials"

Prompt 19 — Automating Attendance Tracking with Face Recognition

Backstory: Your office wants to replace manual attendance sheets with automated facial recognition connected to HR software.

Goal: Build a system that captures attendance via webcam and updates HR records automatically.

Prompt:

"You are an AI-Driven HR Automation Specialist. I want a face recognition attendance tracker that integrates with Zoho People API.

Your task:


1. Connect a webcam to capture employee images at check-in/check-out.

2. Run face recognition using an API like AWS Rekognition or OpenCV.

3. Match recognised faces to employee IDs.

4. Update attendance in Zoho People API.

5. Send a daily attendance summary to HR.

Output format: Attendance capture script + Zoho API integration + HR report template.

Input Files & Code Section:


Zoho People API credentials

Employee ID to face mapping database

Webcam access permissions and recognition API credentials"

Prompt 20 — Automating Podcast Transcription and Upload

Backstory: You run a podcast and need transcripts for SEO and accessibility. Doing it manually takes hours.

Goal: Use APIs to transcribe each new episode and upload the text to your blog automatically.

Prompt:

"You are a Content Automation Engineer. I want an automation that listens for new podcast episodes, transcribes them, and publishes to my WordPress blog.

Your task:


1. Monitor an RSS feed for new podcast episodes.

2. Download the audio file.

3. Use AssemblyAI or Google Speech-to-Text API for transcription.

4. Format the transcript into a blog-friendly HTML format.

5. Upload it as a new blog post via WordPress REST API.

Output format: End-to-end transcription and upload script + blog post HTML template.

Input Files & Code Section:


Podcast RSS feed URL

Transcription API key

WordPress API credentials"

Prompt 21 — Automating Business KPI Dashboard Updates

Backstory: You manage a startup and track sales, expenses, and customer data. You want your KPI dashboard updated automatically every morning.

Goal: Build an API workflow that pulls data from CRM, accounting software, and marketing tools into a BI dashboard.

Prompt:

"You are a Business Intelligence Automation Specialist. I want an automated data pipeline feeding my Power BI dashboard daily.

Your task:


1. Fetch sales data from CRM API (HubSpot or Salesforce).

2. Fetch expenses from accounting API (QuickBooks or Zoho Books).

3. Fetch campaign performance from Google Ads API.

4. Push all data to a Power BI dataset via REST API.

5. Refresh dashboard daily at 7 AM IST.

Output format: ETL (Extract, Transform, Load) script + Power BI dataset refresh automation.

Input Files & Code Section:


CRM API credentials

Accounting API credentials

Google Ads API credentials

Power BI API token"

Prompt 22 — Automating Legal Document Generation

Backstory: You’re a lawyer preparing NDAs, contracts, and agreements for clients. Filling them manually is slow.

Goal: Build an API automation that fills in legal document templates from client data.

Prompt:

"You are a Legal Tech Automation Specialist. I want an API-based system that populates legal document templates from a client database.

Your task:


1. Store client details (name, address, contract terms) in a Google Sheet or database.

2. Pull data via API and inject into pre-defined Word/PDF templates.

3. Save final documents in Google Drive and send via Gmail API.

4. Track sent documents in a log sheet.

5. Allow re-generation if client data changes.

Output format: Document automation script + legal template folder + logging sheet.

Input Files & Code Section:


Document templates (Word/PDF)

Google Sheets API credentials

Google Drive & Gmail API credentials"

Prompt 23 — Automating Food Delivery Order Processing

Backstory: You run a cloud kitchen. Orders from Zomato, Swiggy, and your own website come separately, causing delays.

Goal: Build an API integration that merges all orders into one system.

Prompt:

"You are a Food Tech API Integration Specialist. I want a centralised order management system pulling data from Zomato, Swiggy, and my website.

Your task:


1. Connect to all order APIs with authentication.

2. Merge incoming orders into one dashboard view.

3. Send order confirmation to customers via SMS API.

4. Trigger kitchen ticket printing via printer API.

5. Store all order data for monthly analysis.

Output format: Order aggregation script + kitchen display dashboard + SMS integration.

Input Files & Code Section:


API keys for Zomato, Swiggy, website

SMS API credentials

Database connection for order storage"

Prompt 24 — Automating Social Media Comment Replies

Backstory: You run a brand page with thousands of comments daily. Replying manually takes too long.

Goal: Build a system that auto-replies to comments based on sentiment and keywords.

Prompt:

"You are a Social Media Engagement Automation Engineer. I want to use Instagram Graph API and NLP to auto-reply to comments.

Your task:


1. Fetch new comments via Instagram API.

2. Run keyword & sentiment analysis to classify the comment.

3. Use a pre-defined reply template for each sentiment type.

4. Post the reply via API.

5. Log all replied comments in Google Sheets.

Output format: Comment reply automation script + sentiment keyword mapping + logging sheet.

Input Files & Code Section:


Instagram Graph API credentials

Keyword mapping CSV

Google Sheets API credentials"

Prompt 25 — Automating YouTube to Instagram Clip Conversion

Backstory: You want to post highlights of your YouTube videos on Instagram Reels automatically.

Goal: Build an API workflow that trims, captions, and uploads clips from YouTube to Instagram.

Prompt:

"You are a Video Content Automation Specialist. I want to pull my latest YouTube videos, create 60-second highlights, auto-caption them, and upload to Instagram.

Your task:


1. Fetch video from YouTube Data API.

2. Trim to highlight section based on timestamps from a CSV.

3. Add captions using an API like Rev.ai.

4. Upload to Instagram via Instagram Graph API.

5. Store uploaded video link in a Google Sheet.

Output format: Video processing script + Instagram upload automation + logging system.

Input Files & Code Section:


YouTube API credentials

Instagram Graph API credentials

clip_timestamps.csv with video ID and time ranges"


Product Documentation & User Guides






