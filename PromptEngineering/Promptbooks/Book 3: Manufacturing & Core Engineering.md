# Production Workflow Optimisation

## Prompt 1 — Reducing Production Line Bottlenecks

`Backstory: You are a production manager in an automotive manufacturing plant facing delays on your assembly line. Management wants faster throughput without compromising quality.`

`Goal: Create an AI-driven analysis to identify, simulate, and solve bottlenecks.`

`Prompt:`

`"You are an AI Manufacturing Workflow Analyst. Analyze my production line process flow chart to identify key bottlenecks.`

`````
Your task:


1. Map the sequence of steps in the current workflow.

2. Identify steps with the longest cycle times and highest downtime.

3. Simulate possible solutions (e.g., parallel processing, equipment upgrades).

4. Estimate improvement percentages for each solution.

5. Recommend a final plan with cost-benefit analysis.
``````

` Output format: PDF improvement report + Gantt chart simulation file. `

`Input Files & Code Section:`

```
1. Current workflow diagram (Visio/PDF).

2. Production cycle time logs (Excel).

3. Machine downtime report (CSV)."
```
## Prompt 2 — Predictive Maintenance Scheduling

`Backstory: In your FMCG plant, unexpected equipment breakdowns are causing losses. You want AI to help predict and schedule maintenance.`

`Goal: Create a preventive maintenance calendar using historical data.`

`Prompt:`

`"You are an AI Predictive Maintenance Planner. Use my machine performance and repair history to predict future breakdowns and suggest maintenance dates.`

``````
Your task:


1. Analyze MTBF (Mean Time Between Failures) for each machine.

2. Identify early warning signs in sensor data.

3. Recommend preventive maintenance windows.

4. Balance downtime with production targets.

5. Export schedule for integration with SAP ERP.
``````

`Output format: Excel maintenance schedule + PDF risk report.`

`Input Files & Code Section:`

```
1. Machine performance logs (CSV).

2. Maintenance history files.

SAP ERP downtime export."
```
## Prompt 3 — Optimising Raw Material Usage

`Backstory: Your factory is over-ordering raw materials, causing excess inventory costs.`

`Goal: Use AI to forecast optimal raw material requirements.`

`Prompt:`

`"You are an AI Inventory Forecasting Expert. Analyze past 12 months’ production and sales data to forecast optimal raw material orders.`

``````
Your task:


1. Forecast demand for next quarter using time-series models.

2. Suggest order quantities that maintain a lean inventory.

3. Highlight seasonal or demand-driven variations.

4. Include safety stock calculations.

5. Provide supplier order scheduling plan.
``````
`Output format: Excel procurement plan + PDF forecasting report.`

`Input Files & Code Section:`

```
1. Sales data (CSV).

2. Raw material stock history (Excel).

Supplier lead time chart."
```
## Prompt 4 — Energy Efficiency Improvement Plan

`Backstory: Your manufacturing facility’s energy bills are rising, and management wants to reduce energy usage.`

`Goal: Build an AI-driven energy saving action plan.`

`Prompt:`

`"You are an AI Industrial Energy Auditor. Audit my plant’s energy usage and recommend efficiency improvements.`

`````
Your task:


1. Identify highest energy-consuming machines.

2. Suggest operational changes and retrofits.

3. Estimate ROI for each change.

4. Compare energy savings with government green subsidies.

5. Provide a phased implementation plan.
`````

`Output format: PDF audit report + Excel savings forecast.`

`Input Files & Code Section:`

```
1. Electricity consumption logs.

2. Machine efficiency ratings.

Government subsidy policy documents."
```
## Prompt 5 — Reducing Product Defects with AI

`Backstory: Your quality control (QC) team reports that defect rates are rising. You want AI to help detect root causes.`

`Goal: Create a defect reduction workflow using AI insights.`

`Prompt:`

`"You are an AI Quality Control Analyst. Analyze my production defect data and suggest ways to reduce faulty output.`

``````
Your task:


1. Classify defects by type, machine, and operator.

2. Detect recurring defect patterns.

3. Recommend process or equipment adjustments.

4. Simulate expected defect reduction after changes.

5. Provide QC monitoring checklist.
``````
`Output format: PDF defect analysis + Excel root cause tracker.`

`Input Files & Code Section:`
````

1. QC defect logs (Excel).

2.Production shift reports.

3. Machine maintenance history."
````
## Prompt 6 — Automating Production Line Reporting

`Backstory: You currently rely on manual reports from supervisors, which causes delays and data entry errors. You want AI to automate daily production reporting.`

`Goal: Create a daily production report automatically from machine data and shift logs.`

`Prompt:`

`"You are an AI Production Reporting Assistant. Generate daily production performance reports by consolidating shift logs and IoT sensor data.`

``````
Your task:


1. Extract production counts, downtime, and defect numbers.

2. Compare daily output to target production volumes.

3. Highlight underperforming shifts or machines.

4. Suggest corrective actions for any deviations.

5. Provide an automated template that can be reused daily.
``````
`Output format: PDF daily report + Excel raw data table.`

`Input Files & Code Section:`
````

1. Shift production logs (CSV).

2. IoT machine data export (JSON).

3. Target production KPI sheet."
````
## Prompt 7 — Workforce Shift Optimization

`Backstory: Labor costs are rising, and you want to optimize worker shift schedules without overworking employees.`

`Goal: Build an AI-generated shift allocation plan to maximize productivity.`

`Prompt:`

`"You are an AI Workforce Scheduling Expert. Optimize worker shifts for the next month to reduce overtime costs while meeting production targets.`

``````
Your task:


1. Analyze worker skills, machine compatibility, and attendance records.

2. Minimize overtime while ensuring coverage.

3. Ensure compliance with labor laws.

4. Balance workload across shifts.

5. Export in Excel for HR integration.
``````
`Output format: Excel shift roster + PDF scheduling policy.`

`Input Files & Code Section:`
````
1. Worker skills database (Excel).

2. Attendance logs (CSV).

3. Labor law compliance checklist."
````
## Prompt 8 — Cycle Time Reduction Plan

`Backstory: The average cycle time for your main product is longer than industry benchmarks.`

`Goal: Reduce cycle time without affecting product quality.`

`Prompt:`

`"You are an AI Industrial Process Engineer. Create a cycle time reduction strategy for my [product name] production line.`

``````
Your task:


1. Map current process steps with time durations.

2. Identify non-value-added steps.

3. Suggest lean manufacturing improvements.

4. Estimate cycle time savings for each change.

5. Provide a before/after comparison chart.
``````
`Output format: PDF process improvement plan + Excel cycle time analysis.`

`Input Files & Code Section:`
```

1. Process time study report.

2. Production flow diagrams.
```
`Industry benchmark data."`

## Prompt 9 — Real-Time Production Monitoring Dashboard

`Backstory: You want a live dashboard that shows production KPIs in real-time.`

`Goal: Build an AI-generated Power BI or Tableau dashboard template.`

`Prompt:`

`"You are an AI Manufacturing Data Visualization Expert. Create a real-time dashboard showing production output, downtime, and quality metrics.`

``````
Your task:


1. Pull data from IoT sensors and ERP.

2. Update every 10 minutes.

3. Display KPIs with green/yellow/red status indicators.

4. Allow filtering by machine, product, and shift.

5. Provide setup instructions for my IT team.
``````
`Output format: Power BI or Tableau file + setup guide.`

`Input Files & Code Section:`
````

1. Machine data API access.

2. ERP database schema.

3. KPI definition sheet."
````
## Prompt 10 — Lean Six Sigma Implementation Plan

`Backstory: Your plant wants to adopt Lean Six Sigma to cut waste and defects.`

`Goal: Create a step-by-step Lean Six Sigma deployment plan.`

`Prompt:`

`"You are an AI Lean Six Sigma Consultant. Develop a 6-month Lean Six Sigma implementation roadmap for my plant.`

``````
Your task:


1. Identify key waste areas using the 7 wastes framework.

2. Recommend Kaizen events.

3. Suggest training plans for staff.

4. Define measurable KPIs.

5. Include ROI forecast.
``````
`Output format: PDF roadmap + Excel KPI tracker.`

`Input Files & Code Section:`
```

1. Waste audit report.

2. Current process maps.
```
`Employee training records."`

## Prompt 11 — Supplier Lead Time Optimization

`Backstory: Raw material delays are slowing production.`

`Goal: Reduce supplier lead times using AI-driven forecasting and negotiation.`

`Prompt:`

`"You are an AI Supply Chain Strategist. Analyze supplier performance and suggest ways to reduce lead time.`

``````
Your task:


1. Identify suppliers with frequent delays.

2. Recommend alternate suppliers or dual sourcing.

3. Suggest buffer stock levels.

4. Provide negotiation strategies based on performance.

5. Forecast potential savings from changes.
``````
`Output format: Excel supplier scorecard + PDF strategy report.`

`Input Files & Code Section:`
```

1. Supplier delivery logs.

2. Purchase order records.
```
`Historical lead time data."`

## Prompt 12 — Changeover Time Reduction Plan

`Backstory: Changing production from one product to another takes too long.`

`Goal: Reduce changeover time between product batches.`

`Prompt:`

`"You are an AI SMED (Single-Minute Exchange of Die) Specialist. Develop a plan to reduce product changeover time.`

``````
Your task:


1. Map current changeover steps.

2. Classify steps as internal or external.

3. Suggest modifications to parallelize work.

4. Recommend tool storage improvements.

5. Simulate expected time savings.
``````
`Output format: PDF changeover plan + Excel time tracker.`

`Input Files & Code Section:`
````

1.Changeover time logs.

2.Equipment setup checklists.

3. Operator interviews."
````
## Prompt 13 — Defining Digital Twin for Production Line

`Backstory: You want to create a digital twin of your production line for simulation purposes.`

`Goal: Build an AI prompt for designing a production digital twin model.`

`Prompt:`

`"You are an AI Digital Twin Designer. Create a simulation-ready digital twin of my production line.`

``````
Your task:


1. Map equipment and material flows.

2. Include operational parameters.

3. Enable scenario testing for speed and downtime.

4. Integrate with IoT sensor data feeds.

5. Provide step-by-step deployment guide.
``````
`Output format: Simulation software project file + PDF user manual.`

`Input Files & Code Section:`
```

1. Production layout CAD file.

2. Machine operating specs.
```
`Sensor data mapping."`

## Prompt 14 — Optimising Packaging Line Efficiency

`Backstory: Your packaging line is a bottleneck in your FMCG plant.`

`Goal: Improve packaging speed and reduce material waste.`

`Prompt:`

`"You are an AI Packaging Line Optimization Expert. Improve speed and reduce waste in my packaging process.`

``````
Your task:


1. Analyze current packaging throughput.

2. Recommend equipment adjustments.

3. Suggest alternative packaging materials.

4. Simulate effect of automated labeling.

5. Provide ROI analysis for changes.
``````
`Output format: PDF efficiency plan + Excel ROI sheet.`

`Input Files & Code Section:`
```

1. Packaging speed logs.

2. Material waste records.

3. Equipment maintenance history."
```
## Prompt 15 — Automating Quality Control Image Analysis

`Backstory: Your QC team inspects products manually, which is slow and inconsistent.`

`Goal: Use AI vision models for defect detection.`

`Prompt:`

`"You are an AI Quality Vision System Designer. Analyze product images to detect defects automatically.`

``````
Your task:


1. Train AI on provided defect images.

2. Classify defects with confidence scores.

3. Provide heatmaps showing defect locations.

4. Export results to QC dashboard.

5. Suggest improvements to inspection process.
``````
`Output format: AI model files + PDF accuracy report.`

`Input Files & Code Section:`
````

1. Labeled defect images.

2.QC inspection criteria.

3.Current defect logs."
````
## Prompt 16 — Implementing Kanban for Production Flow

`Backstory: Your factory floor suffers from work-in-progress (WIP) pile-ups, leading to inefficiency and missed delivery dates.`

`Goal: Implement a Kanban system for smoother production flow.`

`Prompt:`

`"You are an AI Kanban Workflow Designer. Create a Kanban implementation plan for my [industry] production facility.`

``````
Your task:


1. Define WIP limits for each stage.

2. Design visual boards for physical and digital use.

3. Suggest card color-coding for task priorities.

4. Recommend daily stand-up meeting structure.

5. Provide metrics to track success over time.
``````
`Output format: PDF Kanban playbook + Excel WIP tracker.`


`Input Files & Code Section:`
````

1. Current process workflow diagrams.

2. List of production stages.

3.Historical WIP inventory data."
````
## Prompt 17 — Inventory Location Optimization

`Backstory: Materials are stored in inefficient locations, causing delays when retrieving them for production.`

`Goal: Reorganize inventory for faster material access.`

`Prompt:`

`"You are an AI Warehouse Layout Planner. Optimize the location of materials in my warehouse to reduce retrieval time.`

``````
Your task:


1. Analyze retrieval frequency and material weight.

2. Position high-frequency items closer to production line.

3. Minimize worker travel distance.

4. Suggest shelf height adjustments for ergonomics.

5. Provide new layout blueprint.
``````
`Output format: CAD warehouse layout + PDF efficiency report.`

`Input Files & Code Section:`
````

1. Warehouse blueprint file.

2. Material retrieval logs.

3. Worker safety guidelines."
````
## Prompt 18 — Seasonal Production Planning

`Backstory: Demand for your products changes drastically based on seasons, but your plant struggles to adjust schedules accordingly.`

`Goal: Build a seasonal production forecast plan.`

`Prompt:`

`"You are an AI Seasonal Demand Planner. Create a 12-month production schedule aligned with seasonal demand patterns.`

``````
Your task:


1. Identify high and low demand periods.

2. Adjust production levels to avoid overstocking.

3. Suggest seasonal product variations if needed.

4. Plan raw material procurement in advance.

5. Create a contingency plan for unexpected spikes.
``````
`Output format: Excel seasonal forecast + PDF action plan.`

`Input Files & Code Section:`
````

1.Sales history (3+ years).

2.Market demand reports.

3.Supplier lead time data."
````
## Prompt 19 — Scrap Reduction Strategy

`Backstory: Your production process generates a high amount of scrap material, increasing costs.`

`Goal: Create a scrap reduction strategy.`

`Prompt:`

`"You are an AI Waste Minimization Consultant. Analyze scrap data and recommend strategies to reduce waste.`

``````
Your task:


1. Identify the most common scrap types.

2. Suggest process changes or material substitutions.

3. Explore opportunities for recycling or reusing scrap.

4. Calculate cost savings potential.

5. Provide implementation roadmap.
``````
`Output format: PDF waste reduction plan + Excel savings tracker.`

`Input Files & Code Section:`
```

1. Scrap material logs.

2. Production process maps.
```
`Material supplier specifications."`

## Prompt 20 — Automated Compliance Documentation

`Backstory: Your industry requires regular safety and compliance documentation, but it’s currently a time-consuming manual process.`

`Goal: Automate compliance reporting.`

`Prompt:`

`"You are an AI Compliance Documentation Specialist. Generate safety and compliance reports automatically from production data.`

``````
Your task:


1. Extract relevant metrics from IoT and QC logs.

2. Format reports according to [industry] regulations.

3. Include visual compliance dashboards.

4. Flag non-compliance areas with corrective actions.

5. Archive reports in PDF and Word formats.
``````
`Output format: PDF compliance report + Word editable file.`

`Input Files & Code Section:`
````

1. Industry compliance checklist.

2. QC inspection logs.

3.IoT machine data export."
````
## Prompt 21 — AI-Driven Production Cost Reduction Plan

`Backstory: Management has tasked you to reduce operational costs by 15% without reducing output.`

`Goal: Identify cost-cutting opportunities in the production process.`

`Prompt:`

`"You are an AI Cost Optimization Analyst. Analyze my production process and recommend ways to cut costs by 15% or more.`

``````
Your task:


1. Break down costs into labor, materials, and energy.

2. Identify inefficiencies in each category.

3. Suggest supplier renegotiations or material alternatives.

4. Highlight automation opportunities.

5. Provide ROI forecast for each recommendation.
``````
`Output format: PDF cost reduction plan + Excel savings model.`

`Input Files & Code Section:`
````

1. Production cost breakdown (Excel).

2. Energy bills.

3. Supplier contract terms."
````
## Prompt 22 — Employee Training Plan for Process Efficiency

`Backstory: Inconsistent worker skills are slowing production and causing errors.`

`Goal: Build a structured training program to improve process efficiency.`

`Prompt:`

`"You are an AI Workforce Training Designer. Create a 3-month training plan for my production staff focused on efficiency and quality.`

``````
Your task:


1. Assess skill gaps from recent QC and performance data.

2. Recommend training modules for each gap.

3. Include on-the-job and classroom sessions.

4. Provide training materials and quizzes.

5. Suggest KPIs to measure improvement.
``````
`Output format: PDF training plan + PowerPoint training slides.`

`Input Files & Code Section:`
````

1. QC performance reports.

2.Employee skill assessment survey.

3.Industry training manuals."
````
## Prompt 23 — AI-Driven Equipment Upgrade Recommendations

`Backstory: Your machinery is outdated and slowing production, but you’re unsure which upgrades to prioritize.`

`Goal: Recommend high-ROI equipment upgrades.`

`Prompt:`

`"You are an AI Equipment Investment Advisor. Analyze my machinery and suggest upgrades that offer the best ROI.`

``````
Your task:


1. Compare current machine performance to industry benchmarks.

2. Estimate time and cost savings for each upgrade.

3. Consider compatibility with existing processes.

4. Provide financing or leasing recommendations.

5. Rank upgrades by ROI and urgency.
``````
`Output format: PDF investment proposal + Excel ROI model.`

`Input Files & Code Section:`
````

1. Machine performance logs.

2.Industry benchmark database.

3. Equipment supplier quotes."
````
## Prompt 24 — Multi-Plant Production Coordination

`Backstory: Your company operates multiple plants, but production scheduling between them is inefficient.`

`Goal: Create a coordinated multi-plant production plan.`

`Prompt:`

`"You are an AI Multi-Plant Scheduling Expert. Develop a synchronized production plan for my 3 manufacturing plants.`

``````
Your task:


1. Assign products to plants based on capacity and specialization.

2. Optimize inter-plant transportation.

3. Adjust schedules to avoid bottlenecks.

4. Share resources (machines, manpower) where possible.

5. Provide contingency plans for plant downtime.
``````
`Output format: Excel master schedule + PDF coordination report.`

`Input Files & Code Section:`
````

1. Plant capacity and specialization list.

2. Transportation cost matrix.

3. Product demand forecast."
````
## Prompt 25 — AI-Powered Kaizen Suggestion System

`Backstory: You want to involve employees in continuous improvement but need a structured system for capturing ideas.`

`Goal: Build an AI-enhanced Kaizen suggestion workflow.`

`Prompt:`

`"You are an AI Continuous Improvement Coordinator. Create a Kaizen idea capture and evaluation system for my plant.`

``````
Your task:


1. Provide an idea submission form for employees.

2. Categorize ideas by process area and potential impact.

3. Score ideas based on cost, feasibility, and ROI.

4. Generate monthly improvement reports.

5. Reward employees for implemented ideas.
``````
`Output format: Excel idea tracker + PDF monthly report.`

`Input Files & Code Section:`
````

1.Employee list and roles.

2.Past improvement logs.

3.ROI calculation template."
````

`Quality Control & Inspection Protocols`

## Prompt 1 — AI-Assisted Defect Classification System

`Backstory: Your factory produces thousands of units daily, but manual defect classification is inconsistent and slow. Management wants a consistent, automated approach.`

`Goal: Build an AI model that can classify defects accurately based on images.`

`Prompt:`

`"You are an AI Quality Inspection Specialist. Analyze product images and classify defects according to severity and category.`

``````
Your task:


1. Use my provided defect image dataset to train the model.

2. Classify each defect as Minor, Major, or Critical.

3. Provide visual heatmaps highlighting defect locations.

4. Suggest potential root causes based on defect patterns.

5. Export results to an Excel QC dashboard.
``````
`Output format: Model prediction results (Excel) + annotated defect images.`

`Input Files & Code Section:`
```

1. Labeled defect image dataset.

2. QC category definitions (Excel).
```
`Root cause mapping guide."`

## Prompt 2 — Automated Incoming Material Inspection

`Backstory: Suppliers sometimes send substandard raw materials, causing production defects. Your QC team needs a faster way to screen incoming shipments.`

`Goal: Automate incoming raw material quality checks using AI.`

`Prompt:`

`"You are an AI Material Inspection Analyst. Evaluate incoming material data and flag shipments that fail quality standards.`

``````
Your task:


1. Compare incoming batch data to quality thresholds.

2. Highlight deviations in moisture content, density, or dimensions.

3. Generate acceptance/rejection decisions.

4. Recommend suppliers with best historical quality performance.

5. Archive all inspection results for compliance purposes.
``````
`Output format: PDF acceptance/rejection report + Excel QC log.`

`Input Files & Code Section:`
````

1. Supplier shipment data (CSV).

2.Quality parameter thresholds.

3.Historical supplier performance data."
````
## Prompt 3 — Real-Time Production Line Quality Monitoring

`Backstory: Currently, QC checks are only done at the end of production, which means defects are detected too late.`

`Goal: Create a real-time monitoring system to catch defects as they occur.`

`Prompt:`

`"You are an AI Real-Time Quality Monitor. Continuously scan production line data to detect quality deviations early.`

``````
Your task:


1. Monitor dimensions, weight, and finish quality.

2. Detect anomalies using AI thresholding models.

3. Send instant alerts to supervisors when deviations occur.

4. Track defect trends over time.

5. Integrate with production dashboard.
``````
`Output format: Live dashboard + PDF monthly QC summary.`

`Input Files & Code Section:`
````

1. Live sensor feed access.

2.Quality standards document.

3.Historical QC reports."
````
## Prompt 4 — End-of-Line Inspection Automation

`Backstory: End-of-line product inspection is slow, causing a packaging backlog.`

`Goal: Use AI to automate the final inspection process.`

`Prompt:`

`"You are an AI End-of-Line Inspection Engineer. Automate final product inspection to speed up throughput.`

``````
Your task:


1. Analyze product images and sensor data to verify dimensions and finish.

2. Flag units that fail visual or functional tests.

3. Generate a pass/fail label for each unit.

4. Log rejected units for rework.

5. Provide rejection reason statistics.
``````
`Output format: Excel inspection log + automated labeling file.`

`Input Files & Code Section:`
````

1. Product specification sheet.

2.End-of-line camera feed or images.

3.Rejection code list."
````
## Prompt 5 — ISO 9001 Audit Preparation

`Backstory: Your company is preparing for ISO 9001 certification, but documentation and processes are scattered.`

`Goal: Create a structured ISO 9001 audit preparation plan.`

`Prompt:`

`"You are an AI ISO 9001 Audit Consultant. Organize all quality processes and documents to prepare for certification.`

``````
Your task:


1. Review existing QC processes against ISO 9001 standards.

2. Identify missing documentation.

3. Recommend corrective actions.

4. Create an audit checklist.

5. Provide training material for staff on audit readiness.
``````
`Output format: PDF audit readiness plan + Excel checklist.`

`Input Files & Code Section:`
````

1. Current QC SOPs.

2.ISO 9001 standard document.

3.Past audit reports."
````
## Prompt 6 — Root Cause Analysis for Defect Patterns

`Backstory: Your defect rate is rising, but you’re unsure whether the problem is with raw materials, machinery, or operators.`

`Goal: Use AI to analyze defect logs and pinpoint root causes.`

`Prompt:`

`"You are an AI Root Cause Investigator. Analyze my QC defect logs to determine the primary sources of defects.`

``````
Your task:


1. Categorize defects by type, machine, operator, and shift.

2. Identify recurring defect trends.

3. Map defects to potential root causes using historical data.

4. Suggest corrective measures for top 3 causes.

5. Predict defect rate reduction after implementation.
``````
`Output format: PDF root cause analysis report + Excel defect tracker.`

`Input Files & Code Section:`
````

1. QC defect log (Excel).

2.Machine maintenance history.

3.Production shift records."
````
## Prompt 7 — Automated QC Report Generation

`Backstory: QC reporting is currently manual and takes several hours every week.`

`Goal: Automate the generation of QC reports from raw inspection data.`

`Prompt:`

`"You are an AI QC Reporting Assistant. Convert my raw QC inspection data into formatted weekly reports automatically.`

``````
Your task:


1. Consolidate data from multiple shifts.

2. Summarize defect rates and compliance scores.

3. Highlight the worst-performing production lines.

4. Include visual charts for management review.

5. Archive reports in PDF and Excel formats.
``````
`Output format: PDF report + Excel summary table.`

`Input Files & Code Section:`
````

1. Raw QC data (CSV).

2.Report template.

3.Production line ID mapping."
````
## Prompt 8 — Supplier Quality Scorecard

`Backstory: Some suppliers have consistently higher defect rates, but you lack a clear performance tracking system.`

`Goal: Build an AI-generated supplier quality scorecard.`

`Prompt:`

`"You are an AI Supplier Performance Analyst. Evaluate my suppliers’ quality performance over the past year.`

``````
Your task:


1. Calculate defect rates for each supplier.

2. Score suppliers on quality, consistency, and delivery timeliness.

3. Rank suppliers from best to worst.

4. Suggest contract renegotiations or replacements for low performers.

5. Provide visual comparison charts.
``````
`Output format: Excel scorecard + PDF supplier evaluation report.`

`Input Files & Code Section:`
````

1. Supplier delivery data (Excel).

2.QC inspection results.

3.Supplier contract terms."
````
## Prompt 9 — First Article Inspection (FAI) Automation

`Backstory: When introducing a new product, first article inspections take too long and delay mass production.`

`Goal: Automate FAI documentation and reporting.`

`Prompt:`

`"You are an AI First Article Inspection Coordinator. Create automated FAI reports from my measurement and QC data.`

``````
Your task:


1. Compare FAI measurements to product specifications.

2. Highlight any deviations with tolerance indicators.

3. Generate a pass/fail decision for each dimension.

4. Store results for traceability.

5. Create a dashboard for multiple FAI reports.
``````
`Output format: PDF FAI report + Excel dimension table.`

`Input Files & Code Section:`
````

1.FAI measurement data.

2.Product specification sheet.

3.Tolerance limits file."
````
## Prompt 10 — Calibration Scheduling for Inspection Tools

`Backstory: QC tools and equipment need regular calibration, but the schedule is often missed.`

`Goal: Build an AI-driven calibration calendar.`

`Prompt:`

`"You are an AI Calibration Scheduler. Create a calibration plan for all my inspection tools.`

``````
Your task:


1. List all tools with last calibration dates.

2. Calculate next due dates based on standards.

3. Send reminders before deadlines.

4. Track overdue calibrations.

5. Export schedule for QC department use.
``````
`Output format: Excel calibration calendar + PDF reminder log.`

`Input Files & Code Section:`
````

1. Tool inventory list.

2.Calibration frequency standards.

3.Past calibration records."
````
## Prompt 11 — Real-Time QC Alert System

`Backstory: QC teams often learn about defects only after an entire batch is produced.`

`Goal: Create a real-time defect alert system.`

`Prompt:`

`"You are an AI QC Alert Manager. Monitor production in real-time and send alerts when defects exceed threshold.`

``````
Your task:


1. Define defect thresholds for each product type.

2. Connect to live sensor and vision system data.

3. Trigger SMS/Email alerts to supervisors.

4. Log each alert with timestamp and cause.

5. Provide monthly alert trend analysis.
```````
`Output format: PDF alert trend report + Excel alert log.`

`Input Files & Code Section:`
```

1. QC threshold list.

2.Sensor/vision system feed.
```
`Supervisor contact list."`

## Prompt 12 — SPC (Statistical Process Control) Chart Generation

`Backstory: QC relies on SPC charts, but creating them manually is tedious.`

`Goal: Automate SPC chart generation from inspection data.`

`Prompt:`

`"You are an AI SPC Chart Creator. Generate control charts for my production processes automatically.`

``````
Your task:


1. Create X-bar, R, and P charts from inspection data.

2. Highlight out-of-control points.

3. Recommend process adjustments.

4. Allow filtering by product type.

5. Export charts as PDF and Excel.
``````
`Output format: SPC chart PDF + Excel source file.`

`Input Files & Code Section:`
````

1. QC inspection data (CSV).

2.Control limits document.

3. Product code mapping."
````
## Prompt 13 — QC Data Cleaning & Standardization

`Backstory: Your QC data is inconsistent due to multiple operators using different formats.`

`Goal: Standardize QC data for better analysis.`

`Prompt:`

`"You are an AI QC Data Cleaner. Standardize and clean my QC inspection data.`

``````
Your task:


1. Identify missing or inconsistent entries.

2. Correct unit mismatches.

3. Convert text-based data into numeric values where possible.

4. Remove duplicates.

5. Provide a clean, analysis-ready file.
``````
`Output format: Excel cleaned dataset + data quality report.`

`Input Files & Code Section:`
````

1. Raw QC data file.

2.Approved QC data format guide.

3.Unit conversion sheet."
````
## Prompt 14 — Rework Tracking System

`Backstory: Reworked items are not being tracked efficiently, leading to repeated issues.`

`Goal: Implement an AI-based rework tracking system.`

`Prompt:`

`"You are an AI Rework Tracker. Monitor and log all reworked products with detailed reasons.`

``````
Your task:


1. Record the reason for each rework.

2. Track time and cost spent on rework.

3. Identify patterns and recurring issues.

4. Suggest preventive measures.

5. Create monthly rework cost analysis.
``````
`Output format: Excel rework log + PDF cost analysis.`

`Input Files & Code Section:`
````

1. QC rework logs.

2. Production cost data.

3.Defect category guide."
````
## Prompt 15 — QC Workforce Efficiency Analysis

`Backstory: You want to know which QC inspectors are most efficient without compromising quality.`

`Goal: Evaluate inspector performance using AI analytics.`

`Prompt:`

`"You are an AI QC Workforce Analyst. Evaluate my QC staff efficiency and accuracy.`

``````
Your task:


1. Compare inspection speed and defect detection rates.

2. Highlight top performers.

3. Identify training needs for low performers.

4. Suggest workload redistribution.

5. Generate performance scorecards.
``````
`Output format: Excel performance scorecard + PDF analysis.`

`Input Files & Code Section:`
````

1. QC inspector logs.

2.Inspection accuracy records.

3.Shift allocation schedule."
````
## Prompt 16 — AI-Driven Visual Inspection for Paint & Surface Finish

`Backstory: Your factory produces metal components with painted surfaces, but human inspectors often miss minor finish issues.`

`Goal: Use AI to detect paint and surface finish defects with high accuracy.`

`Prompt:`

`"You are an AI Surface Finish Inspector. Analyze product images to detect paint inconsistencies, scratches, dents, or uneven coating.`

``````
Your task:


1. Train AI using my historical defect image dataset.

2. Identify defects smaller than 1mm with high-resolution image analysis.

3. Classify defects as cosmetic or functional.

4. Provide a percentage defect severity score.

5. Store images and results in an inspection database.
``````
`Output format: Annotated defect images + PDF inspection report.`

`Input Files & Code Section:`
````

1. High-resolution defect image dataset.

2.Defect classification guide.

3.Surface quality tolerance chart."
````
## Prompt 17 — AI-Enhanced 3D Measurement Verification

`Backstory: Your components need precise 3D measurements, but manual verification is time-consuming.`

`Goal: Automate 3D measurement verification using AI.`

`Prompt:`

`"You are an AI Dimensional Accuracy Verifier. Compare 3D scan measurements of my product with CAD design files.`

``````
Your task:


1. Import my CAD file and 3D scan data.

2. Overlay both models to identify deviations.

3. Highlight out-of-tolerance areas with color coding.

4. Generate pass/fail results for each dimension.

5. Create a deviation heatmap for manufacturing feedback.
``````
`Output format: 3D deviation map + PDF dimensional accuracy report.`

`Input Files & Code Section:`
````

1.CAD design file (.STEP/.IGES).

2.3D scan data (.STL/.OBJ).

3.Tolerance specification document."
````
## Prompt 18 — Automated Packaging QC

`Backstory: Customers have complained about damaged products due to poor packaging, and you want to ensure every package meets quality standards.`

`Goal: Build an AI system to inspect packaging quality.`

`Prompt:`

`"You are an AI Packaging Quality Inspector. Evaluate product packaging for compliance with quality standards.`

``````
Your task:


1. Check dimensions, sealing integrity, and label accuracy.

2. Detect tears, dents, or improper sealing.

3. Flag any packaging that doesn’t meet safety standards.

4. Log inspection results with images.

5. Recommend improvements for recurring packaging issues.
``````
`Output format: PDF packaging QC report + Excel defect log.`

`Input Files & Code Section:`
````

1.Packaging quality checklist.

2.Packaging images/video.

3.Shipping damage reports."
````
## Prompt 19 — Environmental & Safety Compliance QC

`Backstory: Your factory must follow strict environmental and safety QC checks to avoid penalties.`

`Goal: Automate environmental and safety compliance checks.`

`Prompt:`

`"You are an AI Compliance QC Officer. Monitor and document environmental and safety compliance in my manufacturing unit.`

``````
Your task:


1. Check emissions, noise levels, and waste disposal logs.

2. Compare results to legal standards.

3. Flag violations and recommend corrective actions.

4. Generate compliance certificates.

5. Maintain an audit-ready compliance history.
``````
`Output format: PDF compliance checklist + Excel monitoring log.`

`Input Files & Code Section:`
````

1. Environmental monitoring logs.

2. Safety inspection records.

3.Legal compliance standards."
````
Prompt 20 — Customer Return QC Analysis

Backstory: Returned products often reveal QC issues that went undetected during production.

Goal: Analyze customer return data to identify missed defects.

Prompt:

"You are an AI Customer Return Analyst. Analyze customer return data to find QC process gaps.

Your task:


1. Categorize returns by defect type.

2. Link each defect to the production batch.

3. Identify which QC stage failed to detect it.

4. Recommend changes to catch similar defects earlier.

5. Provide estimated savings from improvements.

Output format: PDF return analysis report + Excel defect mapping.

Input Files & Code Section:


- Customer return logs.

- Production batch records.

- QC inspection history."

Prompt 21 — AI-Generated QC Training Simulations

Backstory: Your QC inspectors need better training, but live product defects are rare to demonstrate.

Goal: Create AI-generated defect simulations for training purposes.

Prompt:

"You are an AI QC Training Simulator. Generate defect simulation images and datasets for QC inspector training.

Your task:


1. Create realistic defect images based on historical data.

2. Vary lighting, angles, and defect severity.

3. Develop quizzes for trainees to classify defects.

4. Track trainee accuracy over time.

5. Export training materials for LMS (Learning Management System).

Output format: Image dataset + Excel trainee performance tracker.

Input Files & Code Section:


- Historical defect dataset.

- QC classification guide.

- LMS compatibility format guide."

Prompt 22 — AI-Driven Product Life-Cycle Quality Tracking

Backstory: You want to monitor product quality not just during manufacturing but throughout its life cycle.

Goal: Build a long-term product quality tracking system.

Prompt:

"You are an AI Life-Cycle Quality Analyst. Track and analyze product performance after sale to improve QC processes.

Your task:


1. Collect post-sale defect reports and warranty claims.

2. Identify patterns in early vs. late defects.

3. Link recurring issues to production batches.

4. Suggest preventive design or manufacturing changes.

5. Forecast warranty claim reduction potential.

Output format: PDF life-cycle QC report + Excel warranty analysis.

Input Files & Code Section:


- Warranty claim data.

- Customer complaint logs.

- Production batch records."

Prompt 23 — AI-Assisted QC Policy Review

Backstory: QC policies haven’t been updated in years, and you suspect they may be outdated for modern manufacturing.

Goal: Review and modernize QC policies with AI assistance.

Prompt:

"You are an AI QC Policy Consultant. Review my QC policies and suggest updates for efficiency and compliance.

Your task:


1. Compare policies against current industry standards.

2. Identify gaps and outdated practices.

3. Recommend lean QC process changes.

4. Ensure compliance with ISO and regulatory bodies.

5. Draft updated policy documents.

Output format: PDF policy review + Word editable SOP draft.

Input Files & Code Section:


- Current QC policy documents.

- Industry standard guidelines.

- ISO QC requirements."

Prompt 24 — AI-Powered QC Cost Analysis

Backstory: QC is essential but expensive, and management wants a breakdown of costs to optimize spending.

Goal: Analyze QC-related costs and find savings opportunities.

Prompt:

"You are an AI QC Cost Analyst. Break down my QC costs and recommend ways to optimize them.

Your task:


1. Categorize QC costs (labor, equipment, rework, etc.).

2. Identify high-cost areas with low impact.

3. Recommend automation or process changes for cost reduction.

4. Provide projected savings per change.

5. Present findings in a management-friendly format.

Output format: PDF cost breakdown report + Excel cost model.

Input Files & Code Section:


- QC expense records.

- Equipment maintenance costs.

Rework logs."

Prompt 25 — AI-Integrated QC Dashboard Creation

Backstory: QC data is spread across multiple files and systems, making it hard to get a real-time overview.

Goal: Create a unified AI-powered QC dashboard.

Prompt:

"You are an AI QC Dashboard Developer. Create a live dashboard integrating all QC metrics in one place.

Your task:


1. Pull data from inspection logs, IoT devices, and ERP systems.

2. Display defect rates, rework stats, compliance scores, and cost metrics.

3. Add drill-down capability for batch or product-level details.

4. Provide predictive defect trends.

5. Make dashboard accessible via web and mobile.

Output format: Power BI/Tableau dashboard + PDF user guide.

Input Files & Code Section:


- QC data sources and credentials.

- ERP integration API details.

- Dashboard design preferences."


CAD/CAE Design Assistance

Prompt 1 — AI-Assisted 3D CAD Part Design from Specifications

Backstory: You have a product concept with detailed specifications but no CAD model yet. Normally, creating it from scratch takes days.

Goal: Use AI to generate a fully functional CAD part design from provided dimensions and requirements.

Prompt:

"You are an AI CAD Design Engineer. Using the provided product specifications, create a 3D CAD model ready for manufacturing.

Your task:


1. Interpret my dimension sheet and functional requirements.

2. Select the most suitable material based on usage and stress analysis.

3. Generate a parametric CAD model (compatible with SolidWorks, AutoCAD, or Fusion 360).

4. Export the design in .STEP and .IGES formats.

5. Provide a technical drawing with tolerances.

Output format: CAD file (.STEP & .IGES) + 2D technical drawing (PDF).

Input Files & Code Section:


- Dimension sheet (Excel).

- Product usage description.

- Material preference or constraints."

Prompt 2 — Convert 2D Drawings into 3D CAD Models

Backstory: Many suppliers still provide 2D blueprints, but you need 3D CAD files for simulation and CAM programming.

Goal: Convert old 2D drawings into 3D CAD models.

Prompt:

"You are an AI CAD Converter. Transform my 2D technical drawings into accurate 3D CAD models.

Your task:


1. Interpret all views (top, front, side) from the 2D file.

2. Ensure dimensions match original design intent.

3. Include material properties in the CAD file.

4. Create assembly-ready files if the part has multiple components.

5. Provide a 3D render for visual review.

Output format: 3D CAD file (.STEP & .IGES) + rendered image (PNG/JPEG).

Input Files & Code Section:


- 2D technical drawings (PDF/DWG).

- Material specification sheet.

- Assembly notes if applicable."

Prompt 3 — Parametric CAD Model Optimization for Weight Reduction

Backstory: Your current CAD design meets all functional requirements but is unnecessarily heavy, increasing production costs.

Goal: Optimize the model to reduce weight while maintaining strength.

Prompt:

"You are an AI CAD Optimization Specialist. Modify my parametric CAD model to minimize weight without compromising safety or performance.

Your task:


1. Import my existing CAD file.

2. Perform topology optimization for weight reduction.

3. Maintain structural integrity based on load data.

4. Suggest alternative materials if beneficial.

5. Provide a side-by-side comparison of weight, strength, and cost before and after optimization.

Output format: Optimized CAD file + weight reduction analysis (PDF).

Input Files & Code Section:


- Original CAD file.

- Load & stress data.

- Material database (optional)."

Prompt 4 — CAD Assembly Design from Individual Components

Backstory: You have separate CAD models for parts but no complete assembly model to visualize fit and function.

Goal: Build a fully functional CAD assembly from individual part files.

Prompt:

"You are an AI CAD Assembly Engineer. Create a full assembly from my provided part CAD files.

Your task:


1. Import individual part CAD files.

2. Apply correct mating and alignment constraints.

3. Detect any interference or collisions.

4. Suggest tolerance adjustments for better fit.

5. Provide an exploded assembly view for manufacturing reference.

Output format: CAD assembly file (.ASM/.STEP) + exploded view PDF.

Input Files & Code Section:


- Individual part CAD files.

- Assembly instructions (if available).

- Tolerance and fit specifications."

Prompt 5 — Reverse Engineering from 3D Scan Data

Backstory: You have a physical product but no CAD model. Using 3D scanning, you want to recreate its design.

Goal: Reverse engineer a CAD model from scan data.

Prompt:

"You are an AI Reverse Engineering Specialist. Generate a fully editable CAD model from my 3D scan data.

Your task:


1. Import 3D scan file (.STL/.OBJ).

2. Clean up mesh and remove noise.

3. Convert mesh to parametric CAD surfaces.

4. Match original dimensions and tolerances.

5. Export final model for manufacturing use.

Output format: Parametric CAD file (.STEP) + cleaned mesh file (.STL).

Input Files & Code Section:


- 3D scan file.

- Original part specifications (if available).

- Material details."

Prompt 6 — CAE Simulation Setup for Stress Analysis

Backstory: You’ve designed a part but need to verify its ability to withstand real-world loads before manufacturing.

Goal: Set up a CAE (Computer-Aided Engineering) simulation for stress analysis.

Prompt:

"You are an AI CAE Simulation Expert. Prepare and run a structural stress analysis on my CAD model.

Your task:


1. Import my CAD file and material properties.

2. Apply specified loads, constraints, and boundary conditions.

3. Run Finite Element Analysis (FEA) to find stress distribution.

4. Highlight areas exceeding allowable limits.

5. Recommend design changes to improve strength.

Output format: Stress analysis PDF report + color-coded CAD model.

Input Files & Code Section:


- CAD file (.STEP).

- Material property sheet.

- Load & constraint specifications."

Prompt 7 — Fluid Flow Simulation for Product Optimization

Backstory: Your product involves fluid movement (like a pump or pipe) and needs flow optimization.

Goal: Run a CFD (Computational Fluid Dynamics) simulation to optimize fluid flow.

Prompt:

"You are an AI CFD Simulation Specialist. Simulate and analyze fluid flow in my CAD model.

Your task:


1. Import my CAD file and fluid properties.

2. Apply inlet and outlet flow conditions.

3. Identify turbulence, pressure drops, and flow inefficiencies.

4. Suggest design improvements for optimal flow.

5. Provide side-by-side pre- and post-optimization results.

Output format: CFD report (PDF) + annotated CAD flow visualization.

Input Files & Code Section:


- CAD file (.STEP).

- Fluid property data.

Flow rate and pressure conditions."

Prompt 8 — Thermal Simulation for Heat Management

Backstory: The component you designed experiences high temperatures and you want to ensure it doesn’t overheat.

Goal: Run a thermal analysis to identify heat concentration areas.

Prompt:

"You are an AI Thermal Analysis Engineer. Evaluate and optimize my product for heat dissipation.

Your task:


1. Import CAD model and material thermal properties.

2. Apply heat sources and cooling boundaries.

3. Identify high-temperature zones.

4. Suggest material or design modifications for better cooling.

5. Provide a visual heat map.

Output format: Thermal simulation PDF + CAD heat map.

Input Files & Code Section:


- CAD file (.STEP).

- Heat source specifications.

- Cooling method details."

Prompt 9 — Motion Simulation for Moving Assemblies

Backstory: Your assembly involves moving parts, and you want to ensure smooth operation without collisions.

Goal: Simulate motion and identify mechanical interference.

Prompt:

"You are an AI Motion Simulation Specialist. Test my CAD assembly for motion efficiency.

Your task:


1. Import the CAD assembly.

2. Define motion paths and constraints.

3. Detect interference or collisions.

4. Optimize movement for reduced wear.

5. Provide a motion animation video.

Output format: Motion simulation video + PDF report.

Input Files & Code Section:


- CAD assembly file.

- Motion constraint details.

- Performance requirements."

Prompt 10 — Design for Manufacturing (DFM) Review

Backstory: Your design is ready, but you want to ensure it can be manufactured cost-effectively.

Goal: Review CAD model for manufacturing feasibility.

Prompt:

"You are an AI DFM Specialist. Review my CAD design for manufacturability issues.

Your task:


1. Check tolerances and complexity for CNC machining or 3D printing.

2. Identify features that increase production cost.

3. Suggest geometry simplifications.

4. Recommend optimal manufacturing processes.

5. Provide estimated cost savings from changes.

Output format: DFM analysis PDF + annotated CAD file.

Input Files & Code Section:


- CAD file.

- Preferred manufacturing method.

- Material constraints."

Prompt 11 — CAD File Format Conversion

Backstory: Your supplier uses different CAD software, and file formats aren’t compatible.

Goal: Convert files without losing design integrity.

Prompt:

"You are an AI CAD Converter. Convert my CAD files into the required format while preserving features.

Your task:


1. Import existing CAD file.

2. Maintain parametric features during conversion.

3. Ensure assembly constraints remain intact.

4. Check for geometry errors post-conversion.

5. Provide final files in requested formats.

Output format: Converted CAD file + integrity check report.

Input Files & Code Section:


- Original CAD file.

- Target software format requirements.

- Assembly reference files (if any)."

Prompt 12 — Design Variants for Product Customization

Backstory: You want to offer multiple versions of a product with slight design variations.

Goal: Generate design variants from a base CAD model.

Prompt:

"You are an AI CAD Variant Generator. Create multiple product variants from my base design.

Your task:


1. Modify dimensions, features, and materials as per requirements.

2. Maintain overall functionality across variants.

3. Provide clear labeling for each version.

4. Generate renders for marketing use.

5. Package all CAD files in one folder.

Output format: Multiple CAD files + labeled renders.

Input Files & Code Section:


- Base CAD file.

- Variant specification list.

- Material options."

Prompt 13 — CAD Rendering for Marketing & Visualization

Backstory: You need realistic images of your design for client presentations and marketing materials.

Goal: Create high-quality renders from CAD models.

Prompt:

"You are an AI CAD Renderer. Produce photorealistic images from my CAD model.

Your task:


1. Apply realistic materials and textures.

2. Add environment lighting for accurate visuals.

3. Provide multiple view angles.

4. Export images in high resolution.

5. Provide layered PSD for further editing.

Output format: High-res PNG/JPEG images + PSD file.

Input Files & Code Section:


- CAD file.

- Material and color preferences.

- Branding guidelines."

Prompt 14 — CAE Optimization for Energy Efficiency

Backstory: Your product consumes energy in operation, and you want to make it more efficient.

Goal: Run simulations to reduce energy consumption.

Prompt:

"You are an AI Energy Efficiency Optimizer. Analyze my CAD/CAE model for energy-saving opportunities.

Your task:


1. Simulate operating conditions.

2. Identify design elements causing energy loss.

3. Suggest geometry or material changes.

4. Re-run simulation to compare improvements.

5. Provide projected energy savings.

Output format: Energy optimization report (PDF) + updated CAD file.

Input Files & Code Section:


- CAD model.

- Operational load data.

- Energy consumption logs."

Prompt 15 — CAD Automation for Batch Design Generation

Backstory: You produce similar designs with small variations for different clients.

Goal: Automate batch CAD model generation.

Prompt:

"You are an AI CAD Automation Developer. Create multiple design variations automatically from a base model.

Your task:


1. Import base CAD file.

2. Apply parameter changes from Excel/CSV.

3. Export each variation as a separate CAD file.

4. Generate a render for each version.

5. Package files for delivery.

Output format: Multiple CAD files + render images.

Input Files & Code Section:


- Base CAD file.

- Excel/CSV with parameter changes.

- Rendering preferences."

Prompt 16 — AI-Assisted GD&T (Geometric Dimensioning & Tolerancing) Application

Backstory: Your design is ready, but you need to apply proper GD&T symbols for manufacturing and inspection accuracy.

Goal: Add GD&T to your CAD drawings based on functional requirements.

Prompt:

"You are an AI GD&T Expert. Apply accurate GD&T annotations to my CAD drawing.

Your task:


1. Analyze part functionality and assembly requirements.

2. Determine appropriate datum references.

3. Apply feature control frames for size, form, orientation, and location tolerances.

4. Ensure compliance with ASME Y14.5 or ISO standards.

5. Provide a training sheet explaining the applied GD&T.

Output format: Updated CAD drawing (PDF/DWG) + GD&T explanation guide.

Input Files & Code Section:


- CAD drawing file.

- Functional and assembly requirements.

- Applicable standard (ASME/ISO)."

Prompt 17 — Lightweight CAD Model for VR/AR Applications

Backstory: Your detailed CAD models are too heavy for VR/AR use, making them slow to load.

Goal: Optimize CAD models for lightweight AR/VR deployment.

Prompt:

"You are an AI CAD Model Optimizer. Simplify my CAD model for VR/AR applications without losing essential details.

Your task:


1. Reduce polygon count while preserving critical geometry.

2. Compress textures and materials for real-time rendering.

3. Export in VR/AR-friendly formats (.FBX, .GLTF).

4. Test for performance on common AR/VR devices.

5. Provide a performance improvement summary.

Output format: Lightweight CAD file (.FBX/.GLTF) + optimization report.

Input Files & Code Section:


- Original CAD file.

- VR/AR platform details.

- Performance targets."

Prompt 18 — AI-Generated Fixture & Jig Design

Backstory: You need custom jigs and fixtures for production but lack time for detailed design work.

Goal: Create CAD designs for jigs and fixtures based on part geometry.

Prompt:

"You are an AI Fixture Design Engineer. Design jigs and fixtures for my part to assist in manufacturing or inspection.

Your task:


1. Import my part CAD file.

2. Determine holding and clamping requirements.

3. Design fixture geometry for optimal stability.

4. Ensure compatibility with CNC/assembly stations.

5. Provide technical drawings for fabrication.

Output format: CAD fixture file (.STEP) + 2D technical drawings (PDF).

Input Files & Code Section:


- Part CAD file.

- Fixture usage purpose.

- Machine/tool dimensions."

Prompt 19 — Assembly Animation for Client Presentation

Backstory: You want to impress a client by showing how your product is assembled step-by-step.

Goal: Create a realistic assembly animation from CAD files.

Prompt:

"You are an AI CAD Animator. Produce an assembly sequence animation for my product.

Your task:


1. Import CAD assembly files.

2. Animate each step of the assembly process.

3. Add labels for key components.

4. Export in MP4 and GIF formats.

5. Provide a script for voiceover narration.

Output format: Assembly animation video (MP4/GIF) + narration script (Word).

Input Files & Code Section:


- CAD assembly files.

- Assembly instructions.

- Branding/logo assets."

Prompt 20 — AI-Driven Bill of Materials (BOM) Extraction

Backstory: You have a CAD assembly but no detailed BOM for procurement.

Goal: Generate a full BOM from CAD data.

Prompt:

"You are an AI BOM Generator. Extract a complete Bill of Materials from my CAD assembly.

Your task:


1. Identify all components in the assembly.

2. List part numbers, materials, and quantities.

3. Group items into assemblies and sub-assemblies.

4. Flag any missing data.

5. Export in Excel and PDF formats.

Output format: BOM (Excel/PDF) + missing data report.

Input Files & Code Section:


- CAD assembly file.

- Material database (if available).

- Part numbering system."

Prompt 21 — AI-Based Ergonomic Design Review

Backstory: Your product interacts with human users, so ergonomic design is critical.

Goal: Review and optimize design for ergonomics.

Prompt:

"You are an AI Ergonomic Design Specialist. Evaluate my CAD design for ergonomic efficiency.

Your task:


1. Simulate human interaction using anthropometric data.

2. Identify areas causing discomfort or strain.

3. Suggest modifications for better usability.

4. Provide compliance check with ergonomic standards.

5. Supply before-and-after renders.

Output format: Ergonomic analysis PDF + updated CAD model.

Input Files & Code Section:


- CAD file.

- Target user profile data.

- Ergonomic standard references."

Prompt 22 — AI-Assisted Tolerance Stack-Up Analysis

Backstory: You want to ensure that manufacturing tolerances won’t cause assembly issues.

Goal: Perform tolerance stack-up analysis on assembly.

Prompt:

"You are an AI Tolerance Analysis Expert. Conduct a stack-up analysis for my CAD assembly.

Your task:


1. Import CAD assembly and tolerance data.

2. Simulate worst-case and statistical scenarios.

3. Highlight risk areas causing interference or looseness.

4. Suggest tolerance adjustments.

5. Provide updated drawings.

Output format: Tolerance stack-up report (PDF) + revised CAD file.

Input Files & Code Section:


- CAD assembly file.

- Tolerance table.

- Manufacturing process capabilities."

Prompt 23 — 3D Printing-Ready CAD Preparation

Backstory: You want to produce a prototype via 3D printing but need to prepare the CAD file.

Goal: Make CAD model ready for 3D printing.

Prompt:

"You are an AI 3D Printing Prep Engineer. Prepare my CAD design for successful 3D printing.

Your task:


1. Check wall thickness and overhangs.

2. Add necessary supports.

3. Repair geometry errors.

4. Slice the model with optimal settings.

5. Provide STL and G-code files.

Output format: Printable STL + G-code + PDF prep report.

Input Files & Code Section:


- CAD file.

- Printer specifications.

- Material choice."

Prompt 24 — AI-Powered Design Compliance Check

Backstory: Your design must meet industry-specific compliance standards.

Goal: Verify CAD design against compliance requirements.

Prompt:

"You are an AI Compliance Engineer. Review my CAD design for compliance with industry standards.

Your task:


1. Compare design with provided regulations.

2. Identify non-compliance areas.

3. Suggest corrective changes.

4. Provide a compliance certificate draft.

5. Highlight benefits of compliance for market approval.

Output format: Compliance review report (PDF) + annotated CAD file.

Input Files & Code Section:


- CAD file.

- Compliance standard documents.

- Product application details."

Prompt 25 — AI-Driven Concept-to-Prototype Workflow

Backstory: You have an idea but need to go from concept sketches to a prototype quickly.

Goal: Complete concept-to-prototype CAD workflow.

Prompt:

"You are an AI Concept-to-Prototype Designer. Turn my idea into a working CAD model ready for prototyping.

Your task:


1. Interpret my sketches and design notes.

2. Create a parametric CAD model.

3. Run basic CAE checks.

4. Prepare model for CNC or 3D printing.

5. Provide cost and time estimation for prototype.

Output format: CAD file (.STEP), STL for printing, PDF prototype cost sheet.

Input Files & Code Section:


- Sketches/images.

- Material preferences.

- Prototype method choice."


# Safety & Compliance Documentation

Prompt 1 — Create OSHA-Compliant Safety Manual for Manufacturing Plant

Backstory: Your manufacturing facility needs a safety manual that complies with OSHA (Occupational Safety and Health Administration) standards to ensure worker safety and legal compliance.

Goal: Generate a complete safety manual covering equipment operation, PPE (Personal Protective Equipment), and emergency procedures.

Prompt:

"You are a Manufacturing Safety Compliance Officer. Create a comprehensive OSHA-compliant safety manual for my facility.

Your task:


1. Include sections for PPE requirements, equipment operation safety, emergency evacuation procedures, and hazard reporting.

2. Align guidelines with OSHA manufacturing industry standards.

3. Provide visual safety signage recommendations.

4. Create both a long-form PDF manual and a 1-page quick-reference guide.

5. Include an inspection checklist for managers.

Output format: PDF Safety Manual + Quick Reference Sheet + Inspection Checklist (Excel).

Input Files & Code Section:


- Factory equipment list.

- Plant layout diagram.

Current safety policies (if any)."

Prompt 2 — Fire Safety & Evacuation Plan According to NFPA Standards

Backstory: You want to ensure your manufacturing plant has a fire safety plan that meets NFPA (National Fire Protection Association) requirements.

Goal: Develop a plant-specific fire safety plan with evacuation routes.

Prompt:

"You are a Fire Safety Compliance Expert. Create an NFPA-compliant fire safety and evacuation plan for my manufacturing facility.

Your task:


1. Map emergency exits and fire extinguisher locations.

2. Specify fire alarm and sprinkler system maintenance schedules.

3. Include employee fire drill procedures.

4. Provide a floor plan diagram with marked evacuation routes.

5. Recommend training modules for staff.

Output format: Fire Safety Plan (PDF) + Evacuation Route Map (PNG) + Drill Checklist.

Input Files & Code Section:


- Plant floor plan (CAD/PDF).

- Current fire safety equipment list.

Building occupancy capacity."

Prompt 3 — Hazardous Materials Handling Protocol (HAZMAT)

Backstory: Your facility uses chemicals and other hazardous materials, requiring safe storage, handling, and disposal guidelines.

Goal: Develop a HAZMAT safety protocol aligned with GHS (Globally Harmonized System) and local laws.

Prompt:

"You are a Hazardous Materials Safety Officer. Develop a hazardous materials handling protocol for my manufacturing unit.

Your task:


1. Categorize materials by hazard class (flammable, corrosive, toxic).

2. Specify labeling requirements according to GHS.

3. Provide safe handling and storage guidelines.

4. Outline emergency spill cleanup procedures.

5. Include disposal methods that meet environmental regulations.

Output format: HAZMAT Protocol Document (PDF) + Safety Labels Template (PNG).

Input Files & Code Section:


- List of hazardous materials used.

- Current storage arrangements.

- Local disposal regulations."

Prompt 4 — Machine-Specific Lockout/Tagout (LOTO) Procedures

Backstory: Your facility operates heavy machinery that must be locked out during maintenance to prevent accidents.

Goal: Create machine-specific LOTO procedures in compliance with OSHA standard 1910.147.

Prompt:

"You are a LOTO Procedure Specialist. Create lockout/tagout instructions for each machine in my facility.

Your task:


1. Document step-by-step shutdown procedures for each machine.

2. Specify the lockout devices required.

3. Include visual diagrams for lockout points.

4. Provide employee training checklist.

5. Align procedures with OSHA 1910.147 standard.

Output format: Machine-specific LOTO PDF Sheets + Training Checklist.

Input Files & Code Section:


- Machine inventory list.

- Manufacturer manuals.

- Maintenance schedule."

Prompt 5 — Workplace Safety Audit Template

Backstory: You want to regularly assess safety compliance in your facility without hiring external auditors each time.

Goal: Create a self-audit checklist for safety compliance.

Prompt:

"You are a Workplace Safety Auditor. Design a safety audit template for my manufacturing facility.

Your task:


1. Include checks for PPE usage, machine guards, fire safety, HAZMAT storage, and first aid availability.

2. Use a scoring system to highlight high-risk areas.

3. Align the audit with OSHA, NFPA, and local labor laws.

4. Make it usable for both digital and paper formats.

5. Provide guidelines for corrective action follow-up.

Output format: Safety Audit Checklist (Excel/PDF) + Corrective Action Template.

Input Files & Code Section:


- Existing safety policies.

- Factory layout diagram.

- Regulatory compliance list."

Prompt 6 — Personal Protective Equipment (PPE) Compliance Tracker

Backstory: Ensuring that all workers use the correct PPE daily can be challenging without a tracking system.

Goal: Develop a PPE compliance tracking and reporting system.

Prompt:

"You are a PPE Compliance Officer. Create a PPE compliance tracking document for my manufacturing facility.

Your task:


1. Define PPE requirements for each job role.

2. Create a daily compliance log for supervisors.

3. Include fields for PPE condition checks.

4. Develop a monthly compliance summary report.

5. Recommend signage for PPE zones.

Output format: PPE Compliance Tracker (Excel) + Signage Templates (PNG).

Input Files & Code Section:


- Job role descriptions.

- Current PPE inventory.

- PPE brand/model details."

Prompt 7 — Incident Reporting & Investigation Template

Backstory: A proper incident reporting system ensures every workplace accident is documented and investigated.

Goal: Create a standardized incident reporting and investigation process.

Prompt:

"You are a Workplace Incident Investigator. Develop an incident reporting and root cause analysis template.

Your task:


1. Include sections for incident description, witnesses, and immediate actions taken.

2. Add root cause analysis tools (5 Whys, Fishbone Diagram).

3. Suggest preventive measures to avoid recurrence.

4. Align with OSHA and ISO 45001 requirements.

5. Provide both a printable and fillable PDF version.

Output format: Incident Report Form (PDF) + Root Cause Analysis Sheet (Excel).

Input Files & Code Section:


- List of common workplace incidents.

- Previous accident records (if available).

- Applicable safety standards."

Prompt 8 — ISO 45001 Health & Safety Management System Documentation

Backstory: Your company wants ISO 45001 certification for occupational health and safety.

Goal: Develop the documentation required for ISO 45001 compliance.

Prompt:

"You are an ISO 45001 Documentation Specialist. Prepare the necessary documents for my manufacturing unit.

Your task:


1. Create the OHS (Occupational Health & Safety) policy.

2. Document risk assessment and control measures.

3. Define safety objectives and performance indicators.

4. Include internal audit checklist.

5. Provide a certification readiness roadmap.

Output format: ISO 45001 Documentation Pack (Word/PDF) + Audit Checklist (Excel).

Input Files & Code Section:


- Company profile.

- Existing safety procedures.

Risk assessment reports."

Prompt 9 — Chemical Safety Data Sheet (SDS) Creation

Backstory: You need Safety Data Sheets for all chemicals used, as per GHS standards.

Goal: Create compliant SDS for chemicals in use.

Prompt:

"You are a Chemical Safety Documentation Expert. Prepare GHS-compliant Safety Data Sheets for my chemicals.

Your task:


1. Include sections for identification, hazards, composition, and handling.

2. Specify first aid measures for exposure.

3. Include storage and disposal guidelines.

4. Align with GHS and OSHA HazCom standards.

5. Create a digital SDS library for easy access.

Output format: SDS Documents (PDF) + Digital SDS Library (Excel).

Input Files & Code Section:


- List of chemicals with MSDS (if available).

- Supplier safety data.

- Workplace usage details."

Prompt 10 — Workplace Noise Compliance Report

Backstory: Your facility is noisy, and you must comply with occupational noise exposure limits.

Goal: Assess workplace noise and create compliance reports.

Prompt:

"You are a Noise Compliance Engineer. Prepare a workplace noise compliance assessment report.

Your task:


1. Identify high-noise areas and equipment.

2. Compare decibel levels with OSHA and ISO 9612 limits.

3. Recommend noise control measures.

4. Provide hearing conservation program guidelines.

5. Include pre/post-control measurement results.

Output format: Noise Compliance Report (PDF) + Noise Map Diagram (PNG).

Input Files & Code Section:


- Noise measurement data.

- Plant layout.

Equipment list."

Prompt 11 — Electrical Safety Compliance Checklist

Backstory: Electrical hazards can cause severe accidents; you want to ensure compliance with standards.

Goal: Create an electrical safety audit checklist.

Prompt:

"You are an Electrical Safety Auditor. Design a compliance checklist for my manufacturing plant.

Your task:


1. Include checks for grounding, insulation, and circuit protection.

2. Add inspection frequency guidelines.

3. Align with NFPA 70E and OSHA requirements.

4. Provide hazard labeling recommendations.

5. Include a corrective action section.

Output format: Electrical Safety Audit Checklist (Excel/PDF) + Label Templates (PNG).

Input Files & Code Section:


- Electrical layout.

- Equipment list.

Safety inspection history."

Prompt 12 — First Aid & Emergency Medical Response Plan

Backstory: Your facility needs a ready-to-use emergency medical plan for workplace accidents.

Goal: Create a first aid and emergency medical response plan.

Prompt:

"You are a First Aid Response Planner. Develop a medical response plan for my factory.

Your task:


1. Define emergency response team roles.

2. Include treatment steps for common workplace injuries.

3. List local hospitals and emergency contacts.

4. Provide training schedule for first aid drills.

5. Include a first aid kit inventory checklist.

Output format: Emergency Medical Plan (PDF) + First Aid Kit Checklist (Excel).

Input Files & Code Section:


- Workplace injury history.

- Employee roster.

- Local hospital contact list."

Prompt 13 — Safety Signage Design for Manufacturing Facility

Backstory: You want consistent, standard-compliant safety signs across your plant.

Goal: Design safety signage according to ISO 7010 standards.

Prompt:

"You are a Safety Signage Designer. Create standard-compliant safety signs for my factory.

Your task:


1. Identify signage needs (mandatory, prohibition, hazard, emergency).

2. Use ISO 7010 color codes and symbols.

3. Provide printable vector files.

4. Include placement guide for each sign.

5. Provide a digital library for reuse.

Output format: Safety Signage Pack (SVG/PDF) + Placement Guide (Word).

Input Files & Code Section:


- Plant layout.

- List of hazards.

- Brand color guidelines (if any)."

Prompt 14 — Contractor Safety Compliance Agreement

Backstory: Contractors working at your site must follow your safety rules.

Goal: Develop a contractor safety agreement document.

Prompt:

"You are a Contractor Safety Compliance Manager. Draft a safety compliance agreement for contractors.

Your task:


1. Include safety obligations and PPE requirements.

2. Specify training and orientation rules.

3. Outline penalty clauses for violations.

4. Include acknowledgment and signature sections.

5. Make it bilingual (English + Hindi).

Output format: Contractor Safety Agreement (Word/PDF) + Orientation Checklist (Excel).

Input Files & Code Section:


- List of contractor roles.

- Current site safety policies.

- Legal requirements."

Prompt 15 — Daily Safety Briefing Template

Backstory: You want supervisors to conduct daily safety briefings to reinforce safety culture.

Goal: Create a structured safety briefing format.

Prompt:

"You are a Safety Communication Specialist. Create a daily safety briefing template for my supervisors.

Your task:


1. Include a section for incident updates.

2. Provide daily hazard reminders.

3. Include a worker Q&A segment.

4. Add motivational safety quotes.

5. Make it printable and mobile-friendly.

Output format: Safety Briefing Template (Word/PDF) + Mobile Version (HTML).

Input Files & Code Section:


- Common hazards list.

- Past incident summaries.

- Company branding guidelines."

Prompt 16 — Workplace Hazard Risk Assessment Report

Backstory: Your factory must regularly identify, assess, and rank potential hazards to prevent incidents.

Goal: Create a hazard risk assessment report aligned with ISO 31000.

Prompt:

"You are a Risk Assessment Specialist. Prepare a workplace hazard risk assessment report for my manufacturing facility.

Your task:


1. Identify physical, chemical, biological, and ergonomic hazards.

2. Rank them using a probability–impact risk matrix.

3. Suggest control measures following the hierarchy of controls.

4. Include monitoring and review schedules.

5. Provide an executive summary for management.

Output format: Risk Assessment Report (PDF) + Risk Matrix Chart (PNG).

Input Files & Code Section:


- Plant layout.

- List of machinery and processes.

- Past incident records."

Prompt 17 — Safety Compliance Digital Dashboard Design

Backstory: You want a centralized digital platform to monitor all safety compliance activities in real time.

Goal: Design a safety compliance dashboard layout.

Prompt:

"You are a Safety Data Visualization Expert. Create a real-time safety compliance dashboard design.

Your task:


1. Include PPE compliance rate, incident trends, and inspection schedules.

2. Add visual indicators for overdue safety tasks.

3. Integrate data from Excel/ERP systems.

4. Provide mobile-friendly mockups.

5. Suggest KPIs for continuous improvement.

Output format: Dashboard Mockup (Figma/PNG) + KPI List (Excel).

Input Files & Code Section:


- Sample compliance data.

- Company branding guidelines.

- Safety performance KPIs."

Prompt 18 — Annual Safety Training Program Plan

Backstory: Your company must train employees on safety throughout the year, covering multiple topics.

Goal: Develop a year-round safety training calendar.

Prompt:

"You are a Safety Training Coordinator. Create an annual safety training program plan for my factory.

Your task:


1. Define monthly training themes (fire safety, PPE, first aid, ergonomics, etc.).

2. Include both theoretical and practical sessions.

3. Suggest trainers and resources.

4. Include evaluation and feedback forms.

5. Provide both English and Hindi versions.

Output format: Training Program Calendar (Excel/PDF) + Feedback Form (Word).

Input Files & Code Section:


- List of training topics.

- Employee count and job roles.

- Available training budget."

Prompt 19 — Factory Emergency Response Simulation Plan

Backstory: You want to test your plant’s readiness for emergencies through realistic drills.

Goal: Create a simulation plan for various emergency scenarios.

Prompt:

"You are an Emergency Drill Planner. Develop a plant-specific emergency response simulation plan.

Your task:


1. Include fire, chemical spill, and equipment failure scenarios.

2. Define roles and responsibilities for each participant.

3. Create timing and sequence flowcharts.

4. Provide post-drill evaluation templates.

5. Suggest improvement strategies based on drill results.

Output format: Simulation Plan (PDF) + Drill Evaluation Sheet (Excel).

Input Files & Code Section:


- Plant floor plan.

- Emergency contact list.

- List of past emergency incidents."

Prompt 20 — Workplace Health Monitoring Program

Backstory: Workers in certain areas are exposed to dust, noise, or chemicals, requiring regular health checks.

Goal: Design a workplace health monitoring program.

Prompt:

"You are a Workplace Health Specialist. Create a health monitoring plan for my manufacturing unit.

Your task:


1. Identify health risks by department.

2. Define medical tests required for each job role.

3. Schedule periodic check-ups.

4. Maintain confidential medical records.

5. Include a wellness program for preventive care.

Output format: Health Monitoring Plan (Word/PDF) + Medical Test Tracker (Excel).

Input Files & Code Section:


- Job role descriptions.

- Health risk assessment data.

- Local health regulations."

Prompt 21 — Safety Incentive & Rewards Program

Backstory: You want to encourage employees to follow safety rules through incentives.

Goal: Create a structured safety rewards program.

Prompt:

"You are a Safety Engagement Consultant. Design a safety incentive program for my workers.

Your task:


1. Define measurable safety behaviors.

2. Create a points-based reward system.

3. Suggest both monetary and non-monetary rewards.

4. Include monthly recognition events.

5. Align the program with safety KPIs.

Output format: Rewards Program Guide (PDF) + Tracking Sheet (Excel).

Input Files & Code Section:


- Employee list.

- Current safety KPIs.

- Available reward budget."

Prompt 22 — Accident Claim Documentation Kit

Backstory: After workplace accidents, proper documentation helps in insurance and legal claims.

Goal: Prepare an accident claim documentation kit.

Prompt:

"You are a Workplace Accident Claims Advisor. Create a documentation kit for accident claims.

Your task:


1. Include accident report forms.

2. Provide medical certification templates.

3. Add photo and witness statement logs.

4. Align with labor insurance claim requirements.

5. Provide a checklist for claim submission.

Output format: Claims Documentation Kit (Word/PDF) + Checklist (Excel).

Input Files & Code Section:


- Local labor insurance policy details.

- Past claim examples.

- HR guidelines."

Prompt 23 — Legal Compliance Calendar for Safety Regulations

Backstory: Missing safety-related legal deadlines can result in penalties.

Goal: Create a compliance calendar with all mandatory safety deadlines.

Prompt:

"You are a Safety Compliance Scheduler. Prepare a legal compliance calendar for my manufacturing unit.

Your task:


1. List all legal safety obligations (audits, inspections, certifications).

2. Add due dates and renewal periods.

3. Include responsible person/department for each task.

4. Provide both yearly and monthly views.

5. Make it Excel and Google Calendar compatible.

Output format: Compliance Calendar (Excel) + Google Calendar Import File (.ics).

Input Files & Code Section:


- Applicable laws and regulations.

- Current compliance records.

- Safety department contact list."

Prompt 24 — AI-Powered Safety Violation Detection Guide

Backstory: You want to use AI and cameras to detect safety violations in real-time.

Goal: Create a guide for setting up AI-based safety monitoring.

Prompt:

"You are an AI Safety Tech Advisor. Prepare a guide for deploying AI-based safety violation detection.

Your task:


1. Define use cases (PPE detection, unsafe behavior).

2. Suggest hardware and camera placement.

3. Recommend AI software or APIs.

4. Provide integration plan with existing systems.

5. Include legal considerations for surveillance.

Output format: AI Safety Detection Guide (PDF) + Equipment List (Excel).

Input Files & Code Section:


- Factory layout.

- Current surveillance setup.

- IT infrastructure details."

Prompt 25 — Multi-Language Safety Documentation Pack

Backstory: Workers in your facility speak different languages, requiring multilingual safety documents.

Goal: Create a multilingual safety documentation kit.

Prompt:

"You are a Safety Communication Specialist. Translate and adapt safety documents into multiple languages for my workforce.

Your task:


1. Translate into Hindi, English, and regional languages (as required).

2. Ensure cultural appropriateness of visuals and examples.

3. Provide both print and audio versions.

4. Create QR codes linking to audio safety instructions.

5. Maintain a master version for updates.

Output format: Multilingual Safety Pack (PDF/MP3) + QR Code Directory (Excel).

Input Files & Code Section:


- Existing safety manuals.

- List of required languages.

- Workforce demographics."


# Supply Chain Coordination

Prompt 1 — End-to-End Supply Chain Visibility Dashboard

Backstory: Your manufacturing company faces delays due to a lack of real-time visibility into supply chain operations.

Goal: Build a dashboard that tracks raw materials, production stages, shipping status, and delivery timelines in real-time.

Prompt:

"You are a Supply Chain Data Analyst. Create a blueprint for an end-to-end supply chain visibility dashboard.

Your task:


1. Integrate procurement, warehouse, and shipping data sources.

2. Display KPIs like lead time, on-time delivery rate, and inventory turnover.

3. Add alerts for potential bottlenecks and delays.

4. Include both desktop and mobile-friendly versions.

5. Suggest the tech stack (BI tools, APIs, databases) for implementation.

Output format: Dashboard Wireframe (Figma/PNG) + Data Integration Plan (Excel).

Input Files & Code Section:


Sample order and shipment data.

Current ERP/Inventory system details.

Supplier contact list."

Prompt 2 — Supplier Performance Evaluation System

Backstory: Your production suffers from inconsistent supplier quality and late deliveries.

Goal: Create a supplier evaluation and ranking system to improve procurement decisions.

Prompt:

"You are a Supplier Relationship Manager. Develop a supplier performance evaluation model for my manufacturing unit.

Your task:


1. Define evaluation metrics (quality score, on-time delivery rate, cost competitiveness).

2. Create a scoring formula to rank suppliers.

3. Suggest methods for continuous supplier improvement.

4. Include a quarterly performance report template.

5. Align the process with ISO 9001 requirements.

Output format: Supplier Evaluation Template (Excel) + Performance Report (PDF).

Input Files & Code Section:


Supplier list with past order data.

Quality inspection reports.

Procurement policy."

Prompt 3 — Just-in-Time (JIT) Inventory Planning

Backstory: Excess inventory is tying up capital, while shortages sometimes halt production.

Goal: Implement a Just-in-Time (JIT) inventory strategy to balance efficiency and availability.

Prompt:

"You are an Inventory Optimization Expert. Create a JIT inventory plan for my manufacturing plant.

Your task:


1. Analyze historical demand and lead times.

2. Define minimum stock levels and reorder points.

3. Create supplier coordination guidelines for JIT deliveries.

4. Suggest inventory tracking tools (IoT, RFID).

5. Provide a contingency plan for supply disruptions.

Output format: JIT Inventory Plan (Excel/PDF) + Supplier Coordination Guide (Word).

Input Files & Code Section:


Sales and production data.

Supplier lead times.

Current inventory levels."

Prompt 4 — AI-Driven Demand Forecasting Model

Backstory: Inaccurate demand forecasts are causing overproduction and stockouts.

Goal: Develop an AI-based demand forecasting system using historical data and market trends.

Prompt:

"You are a Demand Planning Data Scientist. Create an AI-powered demand forecasting plan for my supply chain.

Your task:


1. Use machine learning to analyze sales, seasonality, and market trends.

2. Include external data like economic indicators and competitor activity.

3. Provide daily, weekly, and monthly forecast outputs.

4. Include confidence intervals for predictions.

5. Recommend a deployment strategy for ongoing updates.

Output format: Forecast Model Documentation (Word) + Model Output Sample (Excel).

Input Files & Code Section:


Historical sales data.

Market trend reports.

Economic indicator data."

Prompt 5 — Multi-Modal Transport Optimization Plan

Backstory: Your company ships goods via multiple transportation modes but lacks an optimized routing strategy.

Goal: Create a cost-efficient, time-optimized multi-modal transportation plan.

Prompt:

"You are a Transport Logistics Planner. Develop a multi-modal transport optimization strategy for my supply chain.

Your task:


1. Map existing transport routes (road, rail, air, sea).

2. Optimize based on cost, delivery speed, and environmental impact.

3. Suggest partnerships with logistics providers.

4. Include seasonal and weather-based adjustments.

5. Provide a risk management strategy for delays.

Output format: Transport Optimization Report (PDF) + Route Map (PNG).

Input Files & Code Section:


Current transportation routes and costs.

Delivery timelines.

Seasonal demand patterns."

Prompt 6 — Supplier Collaboration Portal Blueprint

Backstory: You want a centralized online platform for real-time supplier collaboration to reduce communication delays.

Goal: Design the layout and workflow for a supplier collaboration portal.

Prompt:

"You are a Supplier Collaboration Architect. Create a blueprint for a cloud-based supplier collaboration portal.

Your task:


1. Include modules for purchase orders, shipment tracking, and quality issue reporting.

2. Enable document sharing (contracts, certifications).

3. Add a supplier feedback and dispute resolution section.

4. Provide mobile app integration.

5. Suggest secure login and role-based access.

Output format: Portal Wireframe (Figma/PNG) + Functional Specification Document (Word).

Input Files & Code Section:


List of supplier interactions.

Existing procurement system details.

Security compliance requirements."

Prompt 7 — Inventory Reconciliation Automation Script

Backstory: Manual inventory reconciliation is slow and error-prone.

Goal: Create an automated process to reconcile physical and digital inventory records.

Prompt:

"You are an Inventory Automation Specialist. Develop a script or workflow to automate inventory reconciliation.

Your task:


1. Compare warehouse counts with ERP records.

2. Highlight discrepancies and auto-generate correction tasks.

3. Integrate barcode/RFID scanning data.

4. Schedule automatic reconciliation runs.

5. Provide audit logs for compliance.

Output format: Automation Script (Python/Excel Macro) + Reconciliation Report Template (Excel).

Input Files & Code Section:


Sample ERP inventory data.

Physical stock count file.

Warehouse location mapping."

Prompt 8 — Reverse Logistics Management Plan

Backstory: Your company needs a structured process for handling returns, repairs, and recycling.

Goal: Create an efficient reverse logistics process.

Prompt:

"You are a Reverse Logistics Planner. Develop a reverse logistics process for returned or defective goods.

Your task:


1. Classify returned items (repair, resale, recycle, disposal).

2. Design return shipment procedures.

3. Partner with recycling vendors.

4. Track return rates and causes.

5. Suggest ways to minimize returns in the first place.

Output format: Reverse Logistics SOP (Word/PDF) + Vendor List (Excel).

Input Files & Code Section:


List of returnable products.

Historical return data.

Vendor capabilities."

Prompt 9 — Emergency Supply Chain Contingency Plan

Backstory: A sudden raw material shortage can halt your operations.

Goal: Create a contingency plan for supply chain disruptions.

Prompt:

"You are a Supply Chain Risk Manager. Create a contingency plan for raw material shortages.

Your task:


1. Identify critical materials and alternate suppliers.

2. Develop emergency procurement procedures.

3. Include safety stock guidelines.

4. Provide a communication plan for stakeholders.

5. Add a rapid decision-making escalation chart.

Output format: Contingency Plan Document (Word/PDF) + Alternate Supplier Directory (Excel).

Input Files & Code Section:


List of critical materials.

Supplier database.

Risk assessment data."

Prompt 10 — Procurement Cost Optimization Strategy

Backstory: Procurement costs are eating into profit margins.

Goal: Identify cost-saving opportunities in procurement.

Prompt:

"You are a Procurement Strategy Consultant. Create a cost optimization strategy for my manufacturing supply chain.

Your task:


1. Analyze historical purchasing data.

2. Identify high-cost materials and suppliers.

3. Suggest bulk purchase and long-term contract savings.

4. Explore group buying with other companies.

5. Include vendor negotiation tactics.

Output format: Cost Optimization Report (PDF) + Supplier Negotiation Checklist (Word).

Input Files & Code Section:


Purchase history.

Supplier pricing lists.

Demand forecasts."

Prompt 11 — Blockchain-Based Supply Chain Transparency Plan

Backstory: Customers want proof of ethical sourcing and authenticity.

Goal: Create a blockchain integration plan for supply chain transparency.

Prompt:

"You are a Blockchain Supply Chain Expert. Design a blockchain system for transparent supply tracking.

Your task:


1. Define data points to be recorded at each stage.

2. Suggest blockchain platforms (Hyperledger, Ethereum, etc.).

3. Ensure traceability from raw material to finished product.

4. Include consumer-facing verification options (QR codes).

5. Provide a cost-benefit analysis.

Output format: Blockchain Integration Plan (PDF) + Data Flow Diagram (PNG).

Input Files & Code Section:


Supply chain process map.

Product certification requirements.

IT infrastructure details."

Prompt 12 — Supplier Onboarding Kit

Backstory: New suppliers often take weeks to align with your standards.

Goal: Create a standardized onboarding kit for suppliers.

Prompt:

"You are a Supplier Enablement Specialist. Prepare an onboarding kit to train suppliers quickly.

Your task:


1. Include company policies and quality requirements.

2. Provide EDI/API integration guidelines.

3. Add product packaging and labeling instructions.

4. Include contact directory for support.

5. Make it downloadable and printable.

Output format: Supplier Onboarding Pack (PDF) + API Integration Guide (Word).

Input Files & Code Section:


Company policies.

API documentation.

Quality standards manual."

Prompt 13 — Seasonal Demand Supply Alignment Plan

Backstory: Demand fluctuations cause overstock in off-season and shortages in peak season.

Goal: Align production and supply with seasonal demand.

Prompt:

"You are a Seasonal Supply Chain Planner. Create a seasonal alignment plan for production and distribution.

Your task:


1. Forecast seasonal demand for each product.

2. Adjust procurement and production schedules accordingly.

3. Plan warehouse space utilization.

4. Arrange temporary logistics contracts.

5. Include post-season stock clearance strategies.

Output format: Seasonal Supply Plan (Excel) + Post-Season Strategy Report (PDF).

Input Files & Code Section:


Seasonal sales data.

Warehouse capacity details.

Supplier lead times."

Prompt 14 — Automated Purchase Order (PO) System Blueprint

Backstory: Manual purchase orders slow down procurement.

Goal: Automate the PO process from request to approval.

Prompt:

"You are a Procurement Process Automation Expert. Create a blueprint for an automated purchase order system.

Your task:


1. Define workflow from requisition to payment.

2. Add approval hierarchy.

3. Integrate with ERP and supplier systems.

4. Include fraud detection mechanisms.

5. Make it mobile-accessible.

Output format: PO Automation Workflow Diagram (PNG) + System Requirement Document (Word).

Input Files & Code Section:


Current PO forms.

ERP system details.

Approval matrix."

Prompt 15 — Green Supply Chain Strategy

Backstory: Your company wants to reduce carbon footprint in the supply chain.

Goal: Develop an environmentally sustainable supply chain plan.

Prompt:

"You are a Sustainable Logistics Consultant. Create a green supply chain strategy for my manufacturing operations.

Your task:


1. Optimize routes for fuel efficiency.

2. Switch to eco-friendly packaging.

3. Partner with green-certified suppliers.

4. Track carbon emissions.

5. Provide annual sustainability reports.

Output format: Green Supply Chain Plan (Word) + Carbon Tracking Sheet (Excel).

Input Files & Code Section:


Supplier environmental certifications.

Transportation data.

Packaging material specs."

Prompt 16 — Cross-Border Trade Compliance Manual

Backstory: Your company is expanding to international markets, but customs clearance delays are costing time and money. Many suppliers and internal teams are unfamiliar with export-import documentation, tariffs, and compliance procedures for different countries. Without a clear manual, mistakes in paperwork or classification codes can lead to shipments being held at ports for weeks.

Goal: Develop a detailed cross-border trade compliance manual tailored to your industry.

Prompt:

"You are an International Trade Compliance Specialist. Create a comprehensive manual for managing cross-border trade for my manufacturing business.

Your task:


1. Outline required export-import documentation (invoice, packing list, bill of lading, certificate of origin, etc.).

2. Include HS code classification rules for my product category.

3. Explain duties, tariffs, and free trade agreements that apply to my target markets.

4. Provide a checklist for customs clearance in India and top export countries.

5. Suggest internal SOPs to ensure compliance across procurement, production, and logistics.

Output format: Cross-Border Trade Manual (PDF) + Country-wise Customs Checklist (Excel).

Input Files & Code Section:


Product descriptions and specs.

List of countries we ship to.

Past customs clearance issues."

Prompt 17 — AI-Based Supplier Risk Scoring Model

Backstory: Some suppliers are financially unstable or have inconsistent quality, which poses a risk to production continuity. Your current supplier selection process doesn’t factor in long-term risk indicators like financial health, geopolitical stability, or compliance history.

Goal: Build an AI-driven scoring model to proactively identify high-risk suppliers.

Prompt:

"You are a Supply Chain Risk Data Scientist. Develop an AI model to score suppliers based on risk factors.

Your task:


1. Identify key risk indicators (financial stability, delivery performance, compliance record, geopolitical location risk).

2. Assign weightages to each risk factor.

3. Train a scoring algorithm using historical supplier performance data.

4. Generate an automated risk score for each supplier.

5. Provide recommendations for mitigating high-risk partnerships.

Output format: Risk Scoring Model Documentation (Word) + Supplier Risk Dashboard (Excel/Tableau).

Input Files & Code Section:


Historical supplier data.

Public financial and compliance reports.

Country risk index dataset."

Prompt 18 — Vendor-Managed Inventory (VMI) Agreement Framework

Backstory: Your suppliers often deliver late or in excess because they don’t have accurate visibility of your stock levels. This leads to either production halts or overstocking. Vendor-Managed Inventory allows suppliers to monitor and replenish stock themselves — but it requires a clear agreement.

Goal: Create a legally compliant and operationally clear VMI framework.

Prompt:

"You are a VMI Implementation Consultant. Create a vendor-managed inventory (VMI) agreement framework for my business.

Your task:


1. Define VMI roles and responsibilities for both buyer and supplier.

2. Outline data sharing requirements (inventory levels, sales trends).

3. Set performance metrics (fill rate, stockout frequency).

4. Include dispute resolution and penalty clauses.

5. Provide templates for weekly replenishment schedules.

Output format: VMI Agreement Template (Word) + Replenishment Tracker (Excel).

Input Files & Code Section:


Current supplier list.

Inventory turnover reports.

ERP integration capabilities."

Prompt 19 — Supply Chain Crisis Communication Protocol

Backstory: When a shipment delay or raw material shortage happens, your team scrambles to inform customers, suppliers, and internal departments. The lack of a structured communication protocol causes confusion and customer dissatisfaction.

Goal: Develop a step-by-step crisis communication plan for supply chain disruptions.

Prompt:

"You are a Crisis Communication Strategist. Create a supply chain disruption communication protocol for my manufacturing business.

Your task:


1. Define who is responsible for communication at each stage of a crisis.

2. Create templates for supplier updates, customer notifications, and internal alerts.

3. Suggest channels for urgent communication (email, WhatsApp, SMS, ERP alerts).

4. Include a timeline for escalation and resolution updates.

5. Provide a feedback mechanism to improve future responses.

Output format: Crisis Communication SOP (PDF) + Notification Templates (Word).

Input Files & Code Section:


List of key customers and suppliers.

Sample past incident reports.

Existing communication tools in use."

Prompt 20 — AI Route Optimization for Deliveries

Backstory: Your transport fleet wastes fuel and time due to inefficient routing, especially for multi-stop deliveries. Changing demand patterns make manual planning ineffective.

Goal: Use AI to optimize delivery routes for cost, time, and sustainability.

Prompt:

"You are a Transport Optimization AI Engineer. Design an AI-powered route optimization solution for my delivery fleet.

Your task:


1. Analyze current delivery routes and travel times.

2. Incorporate live traffic data, road restrictions, and delivery time windows.

3. Optimize for minimal fuel consumption and maximum on-time deliveries.

4. Suggest hardware/software requirements for implementation.

5. Provide a KPI dashboard to monitor improvement.

Output format: Route Optimization Plan (Word) + Sample AI Algorithm Code (Python).

Input Files & Code Section:


Current delivery routes (Excel/CSV).

Fleet capacity details.

Delivery location data."

Prompt 21 — Supplier Diversity & Inclusion Policy

Backstory: Your company wants to work with a broader range of suppliers, including women-owned, minority-owned, and small enterprises, to meet corporate social responsibility goals.

Goal: Create a supplier diversity and inclusion policy.

Prompt:

"You are a CSR Supply Chain Consultant. Develop a supplier diversity and inclusion policy for my manufacturing supply chain.

Your task:


1. Define eligibility and certification requirements for diverse suppliers.

2. Set annual diversity spend targets.

3. Include outreach strategies to attract diverse suppliers.

4. Create reporting templates for tracking progress.

5. Align with global CSR frameworks (UN SDGs, ISO 26000).

Output format: Supplier Diversity Policy (PDF) + Reporting Template (Excel).

Input Files & Code Section:


Current supplier demographic data.

CSR annual report.

Procurement guidelines."

Prompt 22 — Collaborative Planning, Forecasting & Replenishment (CPFR) Framework

Backstory: Your supply chain operates in silos, with suppliers, distributors, and your company forecasting independently, leading to mismatches.

Goal: Build a CPFR framework to synchronize the entire supply network.

Prompt:

"You are a Supply Chain Collaboration Specialist. Create a CPFR framework for my manufacturing business.

Your task:


1. Define shared forecasting methods.

2. Create a joint replenishment process with suppliers and distributors.

3. Specify shared KPIs (forecast accuracy, service level).

4. Suggest collaboration tools for real-time updates.

5. Include governance rules for data sharing.

Output format: CPFR Guide (Word) + Collaboration Workflow Diagram (PNG).

Input Files & Code Section:


Historical sales data.

Supplier and distributor contact list.

Current forecasting method details."

Prompt 23 — Supply Chain Cybersecurity Audit Plan

Backstory: Your ERP, supplier portals, and logistics software are all connected, but you haven’t audited their cybersecurity in years. This makes your supply chain vulnerable to ransomware or data theft.

Goal: Create a cybersecurity audit plan for the supply chain.

Prompt:

"You are a Supply Chain Cybersecurity Auditor. Develop a cybersecurity audit plan for all digital systems used in procurement, inventory, and logistics.

Your task:


1. Identify all systems and third-party connections.

2. Assess risks like phishing, ransomware, and unauthorized data access.

3. Suggest encryption and access control policies.

4. Include compliance with relevant data protection laws (GDPR, India DPDP Act).

5. Provide a yearly audit schedule.

Output format: Cybersecurity Audit Plan (PDF) + Risk Register (Excel).

Input Files & Code Section:


List of all supply chain software and integrations.

IT security policy.

Incident history."

Prompt 24 — AI-Powered Supply Chain Simulation Tool Plan

Backstory: You want to test “what-if” scenarios in your supply chain, like a 20% demand surge or a supplier shutdown, without disrupting operations.

Goal: Create a plan for an AI simulation tool that models different supply chain scenarios.

Prompt:

"You are a Supply Chain Simulation Expert. Design a plan for an AI-based simulation tool.

Your task:


1. Define the key variables (lead times, capacity, demand, costs).

2. Include scenario testing (supplier loss, demand spike, transportation delay).

3. Suggest AI/ML algorithms for predictive analytics.

4. Provide dashboard design for visualization.

5. Include integration with ERP and BI systems.

Output format: Simulation Tool Plan (Word) + Sample Dashboard Layout (PNG).

Input Files & Code Section:


Current supply chain data.

Historical disruption records.

ERP integration capabilities."

Prompt 25 — Carbon Footprint Tracking in Supply Chain

Backstory: Customers and regulators are pushing for sustainability reporting, and you want to measure the carbon footprint of every stage of your supply chain.

Goal: Create a carbon tracking system for supply chain activities.

Prompt:

"You are a Sustainable Supply Chain Analyst. Create a carbon footprint tracking plan for my manufacturing supply chain.

Your task:


1. Map CO₂ emissions from raw material sourcing to final delivery.

2. Include emissions from transport, packaging, and warehousing.

3. Suggest emission calculation methods and tools.

4. Provide a quarterly carbon reduction target plan.

5. Align reporting with GHG Protocol standards.

Output format: Carbon Tracking Plan (PDF) + CO₂ Emission Calculator (Excel).

Input Files & Code Section:


Transport and energy consumption data.

Supplier sustainability reports.

Product packaging details."



