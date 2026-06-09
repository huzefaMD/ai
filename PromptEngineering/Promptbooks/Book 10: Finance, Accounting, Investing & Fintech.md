# Bookkeeping & reconciliation

## Prompt 1 — Monthly Expense Categorization for Small Businesses

`Backstory:`

`You have a 31-year-old entrepreneur running a boutique in Jaipur who uses UPI, bank transfers, and occasional cash payments for business transactions. They struggle to track and categorize monthly expenses, especially distinguishing between personal and business spending. They want a clean breakdown for GST filing and internal tracking.`

`Goal:`

`Generate a categorized monthly expense report ready for accounting and compliance.`

`Prompt:`

`"You are a professional accountant. Create a categorized monthly expense report for a small business in India.`

`For each transaction: `
```
1. Categorize it as operational, marketing, utilities, payroll, or personal.

2. Add payment method (cash, UPI, bank transfer, cheque). 

3. Flag potential tax-deductible expenses. 

4. Summarize total spend per category in INR.
```
`Output should be a clean, table-formatted report ready for GST filing."`

`Inputs Required:`
```
1. List of all transactions with date, amount, and payment method 

2. Business nature and industry 

3. GST applicability (yes/no) 

4. List of known recurring expenses
```
## Prompt 2 — Bank Statement Reconciliation

`Backstory:`

`A 27-year-old freelancer from Bengaluru earns from multiple sources — Upwork, Fiverr, and direct clients. Payments come in via PayPal, bank transfers, and UPI. At month-end, they need to reconcile their bank statement with project invoices to ensure all payments are received and recorded.`

`Goal:`

`Generate a reconciled statement showing matched and unmatched transactions.`

`Prompt:`

`"You are a certified bookkeeper. Reconcile the given bank statement with the provided invoice list.`

`Steps:`
```
1. Match each payment in the bank statement to a specific invoice.

2. Highlight unmatched entries and flag them for follow-up.

3. Identify duplicate or erroneous transactions.

4. Provide a summary of total matched, pending, and disputed amounts."
```
`Inputs Required:`
```
1. Bank statement (CSV, PDF, or Excel)

2. Invoice list with invoice numbers, amounts, and client names

3. Payment dates tolerance range (e.g., ±3 days)

4. Currency conversion rate if foreign payments exist
```
## Prompt 3 — Petty Cash Tracking for Retail Stores

`Backstory:`

`A family-owned stationery shop in Lucknow uses petty cash for small daily expenses — tea for staff, packaging materials, and urgent stock buys. The store owner often forgets to record cash withdrawals and wants a transparent petty cash ledger to monitor leakage.`

`Goal:`

`Create a daily petty cash log with balances updated after every transaction.`

`Prompt:`

`"You are a retail accounting specialist. Create a petty cash log for one month.`

`Include:`
```
1. Date of transaction

2. Description of expense or deposit

3. Amount withdrawn or added

4. Running balance after each entry

5. Weekly summary of total spent vs replenished cash"
```
`Inputs Required:`
```
1. Starting petty cash amount

2. List of daily petty cash transactions

3. Cash replenishment dates and amounts

4. Expense categories (e.g., supplies, refreshments, maintenance)
```
## Prompt 4 — Automating UPI Payment Reconciliation

`Backstory:`

`A café owner in Pune uses multiple UPI handles (GPay, PhonePe, Paytm) to accept payments. End-of-month reconciliation is messy because transaction IDs differ in the café’s billing software and bank passbook. They want an automated way to match UPI payments to daily sales.`

`Goal:`

`Match UPI transaction data with daily sales data to confirm no payments are missing.`

`Prompt:`

`"You are a fintech reconciliation expert. Match the UPI transaction log with the daily sales records for the month.`

`Steps:`
```
1. Standardize date/time format for both datasets.

2. Match transactions based on amount and nearest timestamp.

3. Highlight sales with no corresponding payment and vice versa.
```
`Output a reconciliation report with unmatched entries for review."`

`Inputs Required:`
```
1. UPI transaction log (CSV/Excel)

2. Daily sales report from POS/billing system

3. Tolerance for time mismatch (minutes)

4. Any known discount or refund data
```
## Prompt 5 — Annual Ledger Cleanup

`Backstory:`

`A 35-year-old manufacturing SME in Coimbatore has an annual ledger cluttered with duplicate entries, misspelled vendor names, and inconsistent expense categories. Before the annual audit, they need the ledger cleaned and standardized.`

`Goal:`

`Prepare a clean, consistent ledger for the fiscal year.`

`Prompt:`

`"You are an accounting data cleanup specialist. Review and clean the provided ledger for FY 2024–25.`

`Tasks:`
```
1. Remove duplicate entries.

2. Standardize vendor and client names.

3. Correct inconsistent category labels.

4. Flag unusual or suspicious transactions.

5. Provide a before-and-after summary showing corrections made."
```
## Prompt 6 — Vendor Payment Tracking

`Backstory:`

`A 29-year-old procurement manager at a small catering business in Delhi handles 12–15 vendors supplying everything from vegetables to packaging. Payments are made partly in advance and partly after delivery. She needs a monthly vendor payment tracker to ensure no supplier is overpaid or missed.`

`Goal:`

`Maintain a clear vendor payment status sheet for the month.`

`Prompt:`

`"You are an accounts payable specialist. Create a vendor payment tracker for the given month.`

`Include:`
```
1. Vendor name and contact

2. Invoice number and date

3. Payment due date

4. Amount invoiced, paid, and pending

5. Payment mode
```
`Highlight overdue payments in red."`

`Inputs Required:`
```
1. List of vendor invoices with amounts and due dates

2. Payment history for each vendor

3. Agreed payment terms (e.g., 50% advance, 50% on delivery)

4. Contact details for follow-up
```
## Prompt 7 — Client Receivables Aging Report

`Backstory:`

`A freelance graphic designer in Mumbai works with multiple clients, some paying late. She wants to know how long payments have been pending so she can follow up professionally without losing clients.`

`Goal:`

`Generate a receivables aging report categorizing clients by overdue days.`

`Prompt:`

`"You are an accounts receivable analyst. Create an aging report for all unpaid client invoices.`

`Break down by:`
```
1. Current (0–30 days)

2. 31–60 days overdue

3. 61–90 days overdue

4. 90+ days overdue
```
`Show total outstanding in each category and list top overdue accounts separately."`

`Inputs Required:`
```
1. Client invoice list with issue dates and amounts

2. Record of payments received

3. Follow-up notes (if any)

4. Credit terms with each client
```
## Prompt 8 — GST Input-Output Reconciliation

`Backstory:`

`A boutique clothing brand in Surat needs to reconcile GST input tax credit from supplier invoices with GST output liability from sales invoices to prepare for monthly filing.`

`Goal:`

`Reconcile GST input vs. output with discrepancies flagged.`

`Prompt:`

`"You are a GST compliance specialist. Match supplier GSTIN invoices against sales invoices to reconcile input and output GST.`

`Tasks: `
```
1. Match GSTIN and invoice numbers 

2. Calculate total GST payable vs credit 

3. Flag mismatches or missing GST details 

4. Provide final net GST liability for filing"
```
`Inputs Required:` 
```
1. Purchase invoices with GST details 

2. Sales invoices with GST details 

3. GST rate applicable to goods/services 

4. Filing frequency (monthly/quarterly)
```
## Prompt 9 — Foreign Currency Transaction Reconciliation

`Backstory:`

`A startup in Hyderabad exports software services and receives payments in USD and EUR. Exchange rates fluctuate, and the finance head needs a monthly reconciliation showing INR equivalents and forex gain/loss.`

`Goal:`

`Reconcile foreign currency inflows with correct INR conversions.`

`Prompt:`

`"You are a forex accounting specialist. Reconcile foreign currency receipts with invoice amounts and bank credits.`

`Steps:`
```
1. Convert each payment to INR at the applicable bank rate on the credit date

2. Show any forex gain/loss compared to invoice rate

3. Summarize totals per currency"
```
`Inputs Required:`
```
1. Invoice list with currency and rates used

2. Bank credit statement with INR amounts

3. Official daily exchange rate source

4. Forex charges/fees
```
## Prompt 10 — Loan Payment Tracking

`Backstory:`

`A manufacturing unit in Ludhiana has 3 active business loans with different banks. The owner struggles to track EMI dates, amounts, and interest components.`

`Goal:`

`Maintain a monthly loan payment tracker with due dates and outstanding balances.`

`Prompt:`

`"You are a business finance tracker. Create a loan repayment schedule for all active loans.`

`Include:`
```
1. Bank name and loan account number

2. EMI amount split into principal and interest

3. Due dates

4. Outstanding principal after each payment"
```
`Inputs Required:`
```
1. Loan sanction letters or repayment schedules

2. Payment history till date

3. Interest rate for each loan
```
## Prompt 11 — Annual Cash Flow Summary

`Backstory:`

`A home bakery in Kochi accepts online and cash payments and spends on ingredients, packaging, and marketing. At year-end, they want a summary showing total inflows vs. outflows.`

`Goal:`

`Create a visual annual cash flow report.`

`Prompt:`

`"You are a financial analyst. Summarize annual cash inflows and outflows for the given year.`

`Include:`
```
1. Total sales receipts

2. Major expense categories

3. Monthly inflow/outflow chart

4. Net cash position per month"
```
`Inputs Required:`
```
1. List of all transactions

2. Expense category mapping

3. Bank and cash data combined
```
## Prompt 12 — Duplicate Payment Audit

`Backstory:`

`An NGO in Kolkata suspects that a few suppliers have been accidentally paid twice for the same invoice. They want a review of last year’s transactions to confirm.`

`Goal:`

`Identify and flag duplicate payments.`

`Prompt:`

`"You are an audit specialist. Review all supplier payments for possible duplicates.`

`Criteria:`
```
1. Same vendor name and invoice number

2. Same amount within ±₹5

3. Payment dates within 15 days"
```
`Inputs Required:`
```
1. Supplier payment register

2. Vendor master list

3. Duplicate detection criteria
```
## Prompt 13 — Expense Approval Workflow

`Backstory:`

`A digital marketing agency in Gurgaon reimburses employee expenses for client work. The accounts team wants a simple approval tracker to avoid delays.`

`Goal:`

`Track expense approval status for each claim.`

`Prompt:`

`"You are a process documentation specialist. Create an expense claim tracker.`

`Fields:`
```
1. Employee name and ID

2. Claim date and amount

3. Approver name and status

4. Payment date if approved"
```
`Inputs Required:`
```
1. List of claims

2. Approval rules

3. Employee department list
```
## Prompt 14 — POS Sales vs Bank Credit Reconciliation

`Backstory:`

`A grocery store in Indore uses a POS machine for card transactions but sees delays before money reflects in the bank account. They want to match POS receipts to bank credits.`

`Goal:`

`Reconcile POS daily sales to bank deposits.`

`Prompt:`

`"You are a POS reconciliation expert. Match POS transaction list with bank statement credits.`

`Highlight:`
```
1. Transactions missing in bank credit 

2. Bank credits without matching POS entry"
```
`Inputs Required:`
```
1. POS transaction report 

2. Bank statement 

3. Settlement time lag in days
```
## Prompt 15 — E-commerce Payment Gateway Reconciliation

`Backstory:`

`A seller on Amazon and Flipkart from Ahmedabad gets payouts via Razorpay. They want to ensure every order shipped is paid for after deductions.`

`Goal:`

`Match order IDs to payment gateway payouts.`

`Prompt:`

`"You are an e-commerce finance specialist. Match shipped orders to payment gateway deposits.`

`Include:`
```
1. Order ID 

2. Gross order value 

3. Platform commission deducted 

4. Final payout amount"
```
`Inputs Required:` 
```
1. Order shipment report 

2. Payment gateway settlement report 

3. Commission rate per platform
```
## Prompt 16 — Subscription Payment Tracking

`Backstory:`

`A SaaS startup in Noida charges monthly subscriptions but struggles to track renewals and failed payments.`

`Goal:`

`Track subscription renewals and failed transactions.`

`Prompt:`

`"You are a subscription finance tracker. Create a subscription payment log with:`
```
1. Customer name

2. Subscription start/end date

3. Payment status (paid/failed)

4. Renewal reminders"
```
`Inputs Required:`
```
1. Customer subscription database

2. Payment processor logs

3. Subscription plan pricing
```
## Prompt 17 — Credit Card Expense Reconciliation

`Backstory:`

`A consultancy in Hyderabad uses a corporate credit card for travel and entertainment expenses. The finance team needs to reconcile card statements with receipts.`

`Goal:`

`Match card statement entries to receipts for expense verification.`

`Prompt:`

`"You are a corporate expense auditor. Reconcile credit card transactions to provided receipts.`

`Flag:`
```
1. Missing receipts

2. Amount mismatches

3. Unauthorized transactions"
```
`Inputs Required:`
```
1. Credit card statement

2. Digital/paper receipts scanned

3. Expense category mapping
```
## Prompt 18 — Advance Payment Settlement

`Backstory:`

`A wedding planner in Chandigarh takes advance payments from clients and vendors but struggles to match them to final invoices.`

`Goal:`

`Track advance payments and settlement status.`

`Prompt:`

`"You are a project finance tracker. Create a log for advances taken and settled.`

`Include:`
```
1. Client/vendor name

2. Advance amount and date

3. Final invoice amount

4. Settlement balance"
```
`Inputs Required:`
```
1. List of all advances taken

2. Final invoices issued

3. Payment history
```
## Prompt 19 — Payroll Reconciliation

`Backstory:`

`A mid-sized school in Patna processes monthly salaries but finds mismatches between payroll register and bank transfers.`

`Goal:`

`Reconcile payroll payouts to bank credits.`

`Prompt:`

`"You are a payroll reconciliation specialist. Match payroll register entries with bank transfer statements.`

`Flag:`
```
1. Missing payments

2. Extra payments

3. Amount mismatches"
```
`Inputs Required:`
```
1. Payroll register

2. Bank transfer statement

3. Pay period
```
## Prompt 20 — Cheque Clearing Tracker

`Backstory:`

`A construction company in Nagpur receives large payments via cheques. They want to track clearing status and bounced cheques.`

`Goal:`

`Track cheque deposits and clearance.`

`Prompt:`

`"You are a cheque processing tracker. Create a report showing:`
```
1. Cheque number

2. Bank

3. Deposit date

4. Clearance date or bounce reason"
```
`Inputs Required:`
```
1. List of cheques received

2. Bank deposit slips

3. Clearance status updates
```
## Prompt 21 — Year-End Trial Balance Preparation

`Backstory:`

`An NGO in Bhopal needs a trial balance ready for audit but their accounts are scattered across bank statements, receipts, and Excel sheets.`

`Goal:`

`Prepare a complete trial balance.`

`Prompt:`

`"You are an accountant. Prepare a trial balance from provided data.`

`Include:`
```
1. Ledger accounts with debit/credit balances

2. Totals matching

3. Highlight accounts needing clarification"
```
`Inputs Required:`
```
1. Ledger data

2. Journal entries

3. Bank reconciliations
```
## Prompt 22 — Fixed Asset Register Reconciliation

`Backstory:`

`A factory in Rajkot maintains a fixed asset register but hasn’t updated disposals and new purchases this year.`

`Goal:`

`Reconcile fixed asset register with actual purchases/disposals.`

`Prompt:`

`"You are an asset accountant. Update the fixed asset register by:`
```
1. Adding new assets purchased

2. Removing disposed assets

3. Updating depreciation till date"
```
`Inputs Required:`
```
1. Current asset register

2. Purchase invoices

3. Disposal records
```
## Prompt 23 — Internal Fund Transfer Reconciliation

`Backstory:`

`A company with multiple bank accounts transfers funds internally. They want to match debits in one account with credits in another.`

`Goal:`

`Match internal transfers across accounts.`

`Prompt:`

`"You are a treasury reconciliation specialist. Match all internal transfers between bank accounts by date and amount.`

`Flag unmatched entries"`

`Inputs Required:`
```
1. Statements for all accounts

2. Date tolerance (±1 day)
```
## Prompt 24 — Prepaid Expense Amortization

`Backstory:`

`A firm in Chennai has prepaid annual insurance and software subscriptions. They want monthly amortization entries for accurate books.`

`Goal:`

`Create monthly expense recognition for prepaids.`

`Prompt:`

`"You are an accountant. Amortize prepaid expenses across relevant months.`

`Show:` 
```
1. Original amount 

2. Monthly amortization amount 

3. Remaining balance"
```
`Inputs Required:` 
```
1. List of prepaid expenses with start/end dates 

2. Expense category
```
## Prompt 25 — Partner Capital Account Reconciliation

`Backstory:`

`A partnership firm in Jaipur needs to reconcile partner capital accounts after profit distribution and withdrawals.`

`Goal:`

`Prepare final partner capital balances.`

`Prompt:`

`"You are a partnership accounts specialist. Reconcile capital accounts showing:`
```
1. Opening balance

2. Profit share credited

3. Withdrawals

4. Closing balance"
```
`Inputs Required:`
```
1. Partner agreement terms

2. Profit allocation ratio

3. Withdrawal records
```

# Investment portfolio analysis

## Prompt 1 — Diversification Review for a Young Investor

`Backstory:`

`You are assisting a 29-year-old IT professional from Pune who started investing 5 years ago. His portfolio includes a mix of Indian equities, mutual funds, and a small allocation to gold ETFs. With the recent market volatility, he’s unsure if his investments are well-diversified or too concentrated in certain sectors like tech and banking. He wants a clear analysis of his holdings to check if he’s managing risk effectively and how he can rebalance for stability.`

`Goal:`

`Evaluate the diversification of the portfolio and provide sector/asset allocation recommendations.`

`Prompt:`

`"You are a SEBI-registered investment advisor. Review the investor’s portfolio for diversification across asset classes, sectors, and geographies.`

`For the given portfolio:`
```
1. Show % allocation by asset class (equity, debt, gold, etc.)

2. Show % allocation by sector within equities

3. Identify over-concentration risks

4. Recommend rebalancing moves with target % for each category

5. Suggest 2–3 new investment options to improve diversification"
```
`Inputs Required:`
```
1. List of current holdings with quantities and purchase prices

2. Current market values of holdings

3. Risk tolerance (low, medium, high)

4. Investment horizon (years)
```
## Prompt 2 — Mutual Fund Performance Tracker

`Backstory:`

`You are working with a 32-year-old marketing professional from Delhi who has invested in 8 different mutual funds over the past 3 years. She regularly adds SIP contributions but has never compared their performance against benchmarks or peers. With inflation rising, she wants to know which funds are underperforming and if she should stop or switch her SIPs.`

`Goal:`

`Analyze mutual fund performance and recommend corrective actions.`

`Prompt:`

`"You are a mutual fund analyst. Review the investor’s mutual fund portfolio.`

`For each fund:`
```
1. Compare 1-year, 3-year, and 5-year CAGR against benchmark indices 

2. Check consistency of returns (rolling returns analysis) 

3. Flag underperforming funds 

4. Recommend whether to hold, switch, or stop SIPs"
```
`Inputs Required:` 
```
1. Fund names and codes 

2. Number of units and current NAV 

3. SIP amount and start date for each fund 

4. Benchmark index for each fund
```
## Prompt 3 — Risk-Return Analysis of Stock Portfolio

`Backstory:`

`A 26-year-old engineer from Bengaluru started direct stock investing during the pandemic and now holds 15 Indian stocks, mostly in mid-cap companies. His returns look impressive, but he suspects the portfolio is riskier than he can handle, especially as he plans to use the money for a home down payment in 4 years. He wants a clear view of the portfolio’s volatility and whether his returns justify the risks.`

`Goal:`

`Calculate and interpret portfolio risk and return metrics.`

`Prompt:`

`"You are an equity research analyst. Analyze the stock portfolio’s historical performance.`

`Tasks:` 
```
1. Calculate annualized return for the portfolio 

2. Compute standard deviation and beta (volatility and market risk) 

3. Compare portfolio returns against Nifty 50 

4. Suggest adjustments to align with a moderate risk profile"
```
`Inputs Required:` 
```
1. Stock holdings with purchase dates and prices 

2. Current stock prices 

3. Historical price data (last 3–5 years) 

4. Risk tolerance
```
## Prompt 4 — Portfolio Stress Test Under Market Crash

`Backstory:`

`You’re working with a 30-year-old business analyst in Hyderabad who has a ₹15 lakh portfolio split between equity mutual funds, large-cap stocks, and REITs. After hearing about the 2020 COVID market crash, he’s anxious about how his portfolio would perform in a sudden 25–30% market fall. He wants to see simulated outcomes and understand if he needs more defensive assets to protect his capital.`

`Goal:`

`Simulate a portfolio’s performance during a sharp market downturn.`

`Prompt:`

`"You are a financial risk analyst. Perform a stress test on the portfolio to model a 30% equity market drop.`

`For the given holdings:`
```
1. Apply simulated price drops based on asset correlation to equities

2. Show projected portfolio value post-crash

3. Estimate time to recover based on historical recovery patterns

4. Recommend defensive reallocations (debt, gold, cash) to reduce drawdown"
```
`Inputs Required:`
```
1. Current holdings with market values

2. Asset correlation data

3. Historical market crash data for relevant indices

4. Risk tolerance level
```
## Prompt 5 — SIP Portfolio Future Value Projection

`Backstory:`

`A 28-year-old software developer from Pune invests ₹15,000 monthly via SIPs in equity mutual funds and wants to see how much she could accumulate in 15 years. She also wants to check how different return assumptions (8%, 10%, 12%) change the final amount.`

`Goal:`

`Project future value of an SIP portfolio under multiple return scenarios.`

`Prompt:`

`"You are a personal finance planner. Calculate future value of the SIP portfolio under 3 return scenarios (8%, 10%, 12%).`

`For each scenario:`
```
1. Show corpus at year 5, 10, and 15

2. Display total invested vs. total returns

3. Provide a chart showing growth over time"
```
`Inputs Required:`
```
1. Monthly SIP amount

2. Number of years for projection

3. Assumed annual return rates

4. Frequency of compounding
```
## Prompt 6 — ESG Portfolio Assessment

`Backstory:`

`A 31-year-old HR manager in Mumbai wants her investments to be environmentally and socially responsible. She has a mix of Indian mutual funds, foreign ETFs, and some direct stocks, but isn’t sure how ESG-friendly they are. She wants an evaluation of her portfolio based on ESG scores.`

`Goal:`

`Assess portfolio for ESG compliance and suggest improvements.`

`Prompt:`

`"You are an ESG investment analyst. Review the portfolio holdings and assign ESG ratings (high, medium, low) using available data.`

`For each holding:`
```
1. Show ESG score

2. Highlight major ESG risks (if any)

3. Recommend replacement or additional ESG-friendly investments"
```
`Inputs Required:`
```
1. List of holdings with ticker/codes

2. Source for ESG ratings

3. Minimum ESG score threshold desired
```
## Prompt 7 — Portfolio Overlap Analysis

`Backstory:`

`A 25-year-old content creator from Jaipur has invested in 6 mutual funds and suspects they might be holding the same stocks. This could lead to over-concentration in certain companies and reduce diversification benefits. She wants to know the degree of portfolio overlap.`

`Goal:`

`Identify duplicate stock holdings across multiple funds.`

`Prompt:`

`"You are a mutual fund data analyst. Perform an overlap analysis across all holdings.`

```
Tasks:

1. List all unique stocks held across funds

2. Calculate % of portfolio invested in each stock

3. Highlight any stock with >10% cumulative exposure

4. Recommend alternative funds to reduce duplication"
```
`Inputs Required:`
```
1. List of mutual funds in portfolio

2. Latest fund factsheets or holdings data
```
## Prompt 8 — Sector Rotation Strategy Review

`Backstory:`

`A 33-year-old entrepreneur from Delhi actively rotates sectors based on market trends (IT, banking, FMCG). He wants a review of his last 3 years’ performance versus simply staying invested in a broad index.`

`Goal:`

`Evaluate effectiveness of past sector rotation strategy.`

`Prompt:`

`"You are an equity strategist. Compare past sector allocation returns against Nifty 50.`

`For each year:`
```
1. Show returns from the chosen sectors

2. Show index returns for the same period

3. Calculate alpha generated or lost

4. Suggest whether to continue or adjust sector rotation approach"
```
`Inputs Required:`
```
1. Historical sector allocation data

2. Index benchmark data

3. Transaction dates for each rotation
```
## Prompt 9 — Asset Allocation Rebalancing Plan

`Backstory:`

`A 29-year-old finance manager in Bengaluru targets 70% equity, 20% debt, and 10% gold allocation. After 2 years of market rallies, his equity allocation has grown to 82%, creating excess exposure to market volatility. He wants a plan to rebalance without triggering large tax liabilities.`

`Goal:`

`Create a tax-efficient rebalancing plan to restore target allocation.`

`Prompt:`

`"You are a portfolio rebalancing advisor. Suggest steps to move from current allocation to target 70/20/10 mix.`

`Include:`
```
1. Amounts to be shifted between asset classes

2. Priority order for selling assets to minimize tax impact

3. Suggest STP/SWP options if gradual rebalancing is better"
```
`Inputs Required:`
```
1. Current portfolio value by asset class

2. Target allocation percentages

3. Tax holding period status for each asset
```
## Prompt 10 — Real Estate vs. Equity Portfolio Contribution

`Backstory:`

`A 34-year-old architect in Ahmedabad has both a rental property and an equity portfolio. He wants to know which investment has contributed more to his net worth over the last 5 years, factoring in rental income, price appreciation, dividends, and capital gains.`

`Goal:`

`Compare performance of real estate and equity holdings.`

`Prompt:`

`"You are a wealth analyst. Calculate and compare total returns from real estate and equity investments over the given period.`

`Include:`
```
1. Rental income + property appreciation

2. Dividends + capital gains from equities

3. Annualized return % for each asset type"
```
`Inputs Required:`
```
1. Purchase price and date for property

2. Rental income records

3. Equity portfolio transaction history
```
## Prompt 11 — Dividend Income Forecast

`Backstory:`

`A 28-year-old marketing executive from Chennai has gradually built a portfolio of dividend-paying stocks and REITs worth ₹8 lakhs. She enjoys receiving passive income but has no clear estimate of how much she can expect over the next 12 months. She wants a forecast that accounts for past dividend trends, announced payouts, and possible changes due to market conditions.`

`Goal:`

`Project the expected annual dividend income and payout schedule.`

`Prompt:`

`"You are an equity income analyst. Forecast dividend income for the portfolio.`

`Include:`
```
1. Estimated annual payout for each holding based on historical yield and declared dividends

2. Expected payout dates

3. Total annual dividend income in INR

4. Dividend yield of the entire portfolio"
```
`Inputs Required:`
```
1. List of holdings with quantities

2. Historical dividend data for each holding

3. Corporate announcements of upcoming dividends
```
## Prompt 12 — Inflation-Adjusted Return Analysis

`Backstory:`

`A 31-year-old product manager in Noida is proud of his portfolio returns but realizes inflation might be eroding real gains. Over the last 5 years, his equity and debt investments have earned an average of 9% annually, but inflation averaged around 6%. He wants to see his real returns to evaluate true wealth growth.`

`Goal:`

`Calculate portfolio returns adjusted for inflation.`

`Prompt:`

`"You are a financial analyst. Calculate the portfolio’s real annualized return over the given period.`

`Steps:`
```
1. Calculate nominal returns

2. Subtract average annual inflation to get real returns

3. Show real vs. nominal return graph over time"
```
`Inputs Required:`
```
1. Historical portfolio value by year

2. Inflation rate per year (CPI)

3. Investment start and end dates
```
## Prompt 13 — Portfolio Liquidity Assessment

`Backstory:`

`A 25-year-old MBA student in Mumbai holds a mix of PPF, EPF, equity mutual funds, and NPS. She plans to start her own business in 3 years and needs to know how quickly she can liquidate her investments if required.`

`Goal:`

`Evaluate liquidity of each investment in the portfolio.`

`Prompt:`

`"You are a wealth planner. Assess liquidity for each portfolio component.`

`For each holding:`
```
1. Indicate lock-in period (if any)

2. Estimate time to convert to cash

3. Highlight any penalties for early withdrawal"
```
`Inputs Required:`
```
1. Full list of investments with start dates

2. Applicable lock-in rules

3. Withdrawal penalties or restrictions
```
## Prompt 14 — SIP Step-Up Impact Analysis

`Backstory:`

`A 27-year-old banker in Kolkata invests ₹10,000/month in SIPs and plans to increase contributions by 10% each year as his salary grows. He wants to know the impact of this step-up strategy over 20 years compared to keeping SIP amounts fixed.`

`Goal:`

`Project future value of step-up SIP strategy.`

`Prompt:`

`"You are a mutual fund planner. Compare corpus from a fixed SIP vs. 10% annual step-up SIP over 20 years.`

`Show:`
```
1. Year-wise contribution and total corpus for both methods

2. Additional returns generated by step-up strategy

3. Chart comparing growth curves"
```
`Inputs Required:`
```
1. Base SIP amount

2. Step-up percentage per year

3. Investment duration

4. Expected return rate
```
## Prompt 15 — Currency Risk Analysis for Global Investments

`Backstory:`

`A 34-year-old fashion designer from Delhi has invested in US ETFs and global mutual funds. She’s concerned about the effect of INR depreciation on her returns, especially as she plans to use the funds in India.`

`Goal:`

`Assess portfolio’s currency risk exposure.`

`Prompt:`

`"You are a forex investment analyst. Analyze currency risk for global holdings.`

`Include:`
```
1. Historical INR vs. USD exchange rate trends

2. Effect of currency changes on returns

3. Hedging strategies to reduce risk"
```
`Inputs Required:`
```
1. List of global holdings with currencies

2. Purchase and current values in foreign currency

3. Historical exchange rate data
```
## Prompt 16 — Tax Efficiency Analysis

`Backstory:`

`A 30-year-old chartered accountant in Ahmedabad has investments in equities, debt funds, and FDs. He wants to understand how much tax he is paying on his returns and whether he can improve post-tax gains through tax-efficient instruments.`

`Goal:`

`Analyze portfolio for tax efficiency and suggest improvements.`

`Prompt:`

`"You are a tax-focused investment advisor. Review portfolio returns and tax impact.`

```
Tasks:

1. Calculate post-tax returns for each asset

2. Identify tax-inefficient holdings

3. Suggest alternative instruments with better after-tax yields"
```
`Inputs Required:`
```
1. Investment type, holding period, returns

2. Applicable tax rates for each asset

3. Tax-saving preferences (ELSS, PPF, etc.)
```
## Prompt 17 — Historical Drawdown Analysis

`Backstory:`

`A 26-year-old civil engineer from Nagpur wants to see how much his portfolio value could drop in extreme market conditions, based on historical price movements of his holdings over the last 10 years.`

`Goal:`

`Identify maximum historical drawdowns and recovery times.`

`Prompt:`

`"You are a market risk analyst. Calculate max drawdown for the portfolio over last 10 years.`

`Include:`
```
1. Largest peak-to-trough decline (%)

2. Recovery duration

3. Chart showing drawdown periods"
```
`Inputs Required:`
```
1. Historical price data for holdings

2. Portfolio allocation history
```
## Prompt 18 — Portfolio Alignment with Goals

`Backstory:`

`A 32-year-old lawyer from Lucknow has 3 major goals — buying a house in 5 years, child’s education in 15 years, and retirement in 30 years. She wants to know if her current portfolio allocation supports these timelines.`

`Goal:`

`Match investments to specific life goals.`

`Prompt:`

`"You are a goal-based financial planner. Align portfolio with stated financial goals.`

`For each goal:`
```
1. Estimate required corpus

2. Map suitable investments from current portfolio

3. Identify shortfall and suggest new investments"
```
`Inputs Required:`
```
1. Current portfolio details

2. Goal timelines and estimated costs

3. Inflation assumption
```
## Prompt 19 — Portfolio Cost Analysis

`Backstory:`

`A 28-year-old entrepreneur from Jaipur suspects that high expense ratio mutual funds and frequent stock trades are eating into his returns. He wants to quantify total annual portfolio costs.`

`Goal:`

`Calculate and summarize portfolio costs.`

`Prompt:`

`"You are a cost-efficiency analyst. Review portfolio for annual costs.`

`Include:`
```
1. Expense ratios for mutual funds

2. Brokerage and transaction fees for stocks

3. Total costs as % of portfolio value"
```
`Inputs Required:`
```
1. List of mutual funds and expense ratios

2. Stock trade history with brokerage rates
```
## Prompt 20 — Portfolio Concentration Risk Report

`Backstory:`

`A 30-year-old mechanical engineer from Chennai holds 70% of his equity investments in just 3 companies. He wants to understand the risk of such concentration and its effect on volatility.`

`Goal:`

`Assess and visualize portfolio concentration risk.`

`Prompt:`

`"You are a portfolio risk analyst. Create a report showing % allocation to top holdings.`

`Highlight:`
```
1. Any single holding >10% of portfolio

2. Impact of 20% drop in top holdings"
```
`Inputs Required:`
```
1. Portfolio holdings and values

2. Risk tolerance level
```
## Prompt 21 — Factor-Based Portfolio Analysis

`Backstory:`

`A 34-year-old fund enthusiast in Bengaluru follows factor investing (value, momentum, low volatility) but isn’t sure which factors his portfolio is tilted towards.`

`Goal:`

`Identify factor exposure of the portfolio.`

`Prompt:`

`"You are a quant analyst. Map portfolio to factor exposures.`

`Include:`
```
1. % tilt towards each factor

2. Compare returns to factor indices

3. Suggest rebalancing for desired factor mix"
```
`Inputs Required:`
```
1. List of stocks and weights

2. Factor score database
```
## Prompt 22 — Retirement Corpus Projection

`Backstory:`

`A 29-year-old architect from Kochi wants to retire at 55. She invests in mutual funds and EPF, but isn’t sure if her current pace will meet her desired lifestyle.`

`Goal:`

`Project retirement corpus and identify gaps.`

`Prompt:`

`"You are a retirement planner. Project corpus at retirement age based on current portfolio and contributions.`

`Show:`
```
1. Total projected corpus

2. Required corpus for desired lifestyle

3. Additional investment needed"
```
`Inputs Required:`
```
1. Current portfolio value

2. Monthly investment amount

3. Expected annual return

4. Inflation rate
```
## Prompt 23 — Reinvestment Strategy for Maturity Proceeds

`Backstory:`

`A 31-year-old dentist in Hyderabad has an FD maturing next month and wants to reinvest the amount to improve returns without taking excessive risk.`

`Goal:`

`Suggest reinvestment options based on risk profile.`

`Prompt:`

`"You are a personal investment consultant. Recommend reinvestment options for maturity proceeds.`

`Include:`
```
1. At least 3 options with risk/return profile

2. Tax implications

3. Liquidity considerations"
```
`Inputs Required:`
```
1. Maturity amount

2. Risk tolerance

3. Investment horizon
```
## Prompt 24 — Goal-Based SIP Allocation

`Backstory:`

`A 25-year-old fresher in Mumbai wants to start 3 SIPs for different goals — a bike purchase in 3 years, a master’s degree in 5 years, and a house down payment in 10 years.`

`Goal:`

`Allocate SIP amounts to each goal for optimal growth.`

`Prompt:`

`"You are a SIP allocation planner. Suggest fund types and amounts for each goal.`

`For each goal:`
```
1. Recommended asset class/fund category

2. Monthly contribution required

3. Expected return and maturity value"
```
`Inputs Required:`
```
1. Goal timelines and cost estimates

2. Risk appetite

3. Total monthly budget for SIPs
```
## Prompt 25 — Annual Portfolio Review Report

`Backstory:`

`A 33-year-old finance professional in Delhi does ad-hoc investments but never a full portfolio review. He wants an annual summary that covers performance, asset allocation, risks, and recommendations.`

`Goal:`

`Create a comprehensive annual portfolio review.`

`Prompt:`

`"You are a portfolio manager. Prepare a full-year review of the portfolio.`

`Include:`
```
1. Annual returns vs benchmark

2. Asset allocation chart

3. Major risks and recommendations

4. Action plan for next year"
```
`Inputs Required:`
```
1. Portfolio holdings with purchase data

2. Benchmark indices

3. Annual transaction history
```

# Tax planning & GST compliance

## Prompt 1 — Annual Tax Saving Plan for Salaried Employee

`Backstory:`

`You are working with a 29-year-old software engineer from Bengaluru earning ₹14 LPA. His salary structure includes HRA, special allowance, and performance bonuses. While he has an EPF contribution, he has not fully utilized deductions under Section 80C, 80D, or other available exemptions. He wants a complete annual tax-saving plan that minimizes his liability without risky investments.`

`Goal:`

`Prepare a personalized tax-saving plan using legal deductions and exemptions.`

`Prompt:`

`"You are a tax consultant. Design a 12-month tax-saving plan for a salaried professional.`

`For the given salary structure:`
```
1. Identify applicable deductions (80C, 80D, 80G, etc.)

2. Suggest investment options to fully utilize exemptions

3. Show estimated taxable income after deductions

4. Provide month-by-month investment schedule"
```
`Inputs Required:`
```
1. Salary breakup with allowances

2. Current investments and insurance premiums

3. Medical expenses and dependent details

4. Preferred risk level for investments
```
## Prompt 2 — GST Return Filing Checklist

`Backstory:`

`A 32-year-old small business owner in Jaipur runs a boutique selling clothes both offline and through Instagram. She is GST registered and files monthly returns but often misses claiming input tax credit because invoices aren’t matched in GSTR-2B. She needs a clear pre-filing checklist to avoid errors.`

`Goal:`

`Create a step-by-step GST return filing checklist.`

`Prompt:`

`"You are a GST compliance expert. Create a checklist for accurate monthly GST return filing.`

`Include:`
```
1. Verifying sales invoices and GSTIN

2. Matching purchase invoices for ITC claims

3. Reconciling GSTR-1, GSTR-2B, and books of accounts

4. Reviewing late fees and interest applicability"
```
`Inputs Required:`
```
1. GSTIN of the business

2. Sales and purchase invoice lists

3. GST filing frequency (monthly/quarterly)

4. Accounting software used
```
## Prompt 3 — Advance Tax Calculation for Freelancers

`Backstory:`

`A 27-year-old freelance content writer from Pune earns income from Indian clients via UPI/bank transfers and foreign clients via PayPal. Her income is irregular, and she often forgets to pay advance tax, leading to penalties. She wants a quarterly advance tax calculation plan based on estimated earnings.`

`Goal:`

`Prepare an advance tax schedule with payment amounts and due dates.`

`Prompt:`

`"You are a tax advisor. Calculate quarterly advance tax amounts for a freelancer based on projected income.`

`For each quarter: `
```
1. Show estimated tax liability 

2. Deduct TDS already paid by clients 

3. Provide payment challan details and due dates"
```
`Inputs Required: `
```
1. Estimated annual income split by quarter 

2. Applicable deductions under 80C/80D 

3. TDS certificates received 

4. Previous year’s tax rate slab
```
## Prompt 4 — Comparing Old vs. New Tax Regime

`Backstory:`

`A 30-year-old corporate lawyer in Delhi earns ₹22 LPA and has investments in ELSS, NPS, and life insurance. With the government’s introduction of the new tax regime, she is unsure which structure would save her more money. She wants a side-by-side comparison of her tax liability under both regimes, considering all exemptions and deductions she is eligible for.`

`Goal:`

`Help choose between old and new tax regimes for maximum savings.`

`Prompt:`

`"You are a tax planner. Compare the old and new tax regimes for the given income and deductions.`

`Include: `
```
1. Gross taxable income under each regime 

2. Deductions allowed 

3. Final tax payable under both 

4. Clear recommendation with reason"
```
`Inputs Required: `
```
1. Salary breakup and other income sources 

2. List of deductions claimed (80C, 80D, 80G, HRA, etc.) 

3. Age and residential status 

4. Expected annual income for the year
```
## Prompt 5 — GST Input Tax Credit Maximization Plan

`Backstory:`

`A 28-year-old e-commerce seller from Surat is GST registered but claims less ITC than possible because many supplier invoices are missing or not GST compliant. She wants a system to track and maximize ITC every month.`

`Goal:`

`Create a process to ensure maximum GST ITC claim.`

`Prompt:`

`"You are a GST specialist. Create a monthly ITC maximization plan.`

`Include:`
```
1. Checking supplier GST compliance

2. Matching GSTR-2B with purchase register

3. Following up on missing invoices

4. Avoiding blocked credit categories"
```
`Inputs Required:`
```
1. Supplier list with GSTINs

2. Purchase register

3. Current ITC claimed vs. eligible ITC
```
## Prompt 6 — HRA Exemption Calculator

`Backstory:`

`A 27-year-old IT professional in Bengaluru pays ₹25,000/month in rent but is unsure if she is claiming the correct HRA exemption. She wants an accurate exemption calculation considering her basic salary, DA, and metro city status.`

`Goal:`

`Calculate maximum allowable HRA exemption.`

`Prompt:`

`"You are a payroll tax expert. Calculate HRA exemption as per Section 10(13A).`

`Consider:`
```
1. Actual HRA received

2. Rent paid – 10% of basic + DA

3. 50% of basic + DA (metro city)"
```
`Inputs Required:`
```
1. Monthly basic salary and DA

2. Monthly rent paid

3. City type (metro/non-metro)

4. Actual HRA received per month
```
## Prompt 7 — Late GST Filing Penalty Estimator

`Backstory:`

`A 33-year-old small business owner in Kolkata missed filing GSTR-3B for two months due to personal emergencies. She wants to know the exact late fee and interest payable before filing.`

`Goal:`

`Calculate GST late fee and interest charges.`

`Prompt:`

`"You are a GST compliance calculator. Estimate late fees and interest for delayed GSTR-3B filing.`

`Include:`
```
1. Late fee per day (CGST + SGST)

2. Interest on net tax liability

3. Total payable amount"
```
`Inputs Required:`
```
1. Filing frequency (monthly/quarterly)

2. Number of days delayed

3. Net tax liability for each month
```
## Prompt 8 — Freelance Income Tax Filing Template

`Backstory:`

`A 26-year-old freelance videographer in Mumbai earns from both Indian and international clients. She needs a simple, pre-filled Excel template to record her earnings, expenses, TDS, and foreign remittances to make ITR filing easier.`

`Goal:`
`Create a ready-to-use income tax filing template for freelancers.`

`Prompt:`

`"You are a tax documentation expert. Create an Excel template for freelance income tax filing.`

`Include:`
```
1. Client name and country

2. Invoice amount and payment date

3. TDS deducted

4. Expenses with category

5. Net taxable income"
```
`Inputs Required:`
```
1. Nature of freelance work

2. Usual expense categories

3. Average number of invoices per month
```
## Prompt 9 — GST E-invoice Implementation Guide

`Backstory:`

`A 30-year-old wholesale distributor in Ahmedabad has crossed the ₹5 crore turnover threshold and is now required to issue GST e-invoices. He has no idea how to integrate the system with his current billing software.`

`Goal:`

`Provide a step-by-step e-invoice implementation guide.`

`Prompt:`

`"You are a GST technology consultant. Create a step-by-step process to implement e-invoicing.`

`Include:`
```
1. Registration on GST e-invoice portal

2. API integration with billing software

3. Invoice data format requirements

4. Troubleshooting common errors"
```
`Inputs Required:`
```
1. Billing software details

2. Turnover for last financial year

3. Existing invoice format
```
## Prompt 10 — Advance Tax Reminder System

`Backstory:`

`A 34-year-old self-employed interior designer in Delhi often forgets to pay advance tax on time, leading to penalties. She wants a system that sends her reminders and pre-calculates each installment based on updated income estimates.`

`Goal:`

`Set up an automated advance tax reminder and calculation plan.`

`Prompt:`

`"You are a financial automation consultant. Design a reminder system for advance tax payments. `

`Include:`
```
1. Due dates for each quarter

2. Estimated payment amounts

3. Method to adjust for income fluctuations"
```
`Inputs Required:`
```
1. Estimated annual income pattern

2. Previous year’s advance tax paid

3. Current quarter’s income data
```
## Prompt 11 — Section 80D Health Insurance Tax Benefit Calculator

`Backstory:`

`A 28-year-old teacher from Pune has purchased health insurance for herself and her parents but is unsure how much tax benefit she can claim under Section 80D.`

`Goal:`

`Calculate maximum deduction under Section 80D.`

`Prompt:`

`"You are a personal tax planner. Calculate deduction under Section 80D for self and family.`

`Include:`
```
1. Premium paid for self/spouse/children

2. Premium paid for parents (senior/non-senior)

3. Preventive health check-up limit"
```
`Inputs Required:`
```
1. Premium amounts and insured persons

2. Age of each insured person
```
## Prompt 12 — GST Annual Return Preparation Plan

`Backstory:`

`A 32-year-old GST-registered trader in Jaipur needs to prepare GSTR-9 for the first time. He wants a clear plan to gather all documents and reconcile data before filing.`

`Goal:`

`Create a preparation checklist for GSTR-9.`

`Prompt:`

`"You are a GST return expert. Create a step-by-step GSTR-9 preparation checklist.`

`Include: `
```
1. Reconciling GSTR-1, GSTR-3B, and books 

2. Checking ITC claimed vs. available 

3. Reviewing HSN summary"
```
`Inputs Required:`
```
1. GST returns filed during the year 

2. Purchase and sales registers 

3. ITC ledger
```
## Prompt 13 — Capital Gains Tax Calculator

`Backstory:`

`A 27-year-old equity investor in Mumbai has booked profits in stocks, mutual funds, and one real estate property this year. She wants to know her short-term and long-term capital gains tax liability.`

`Goal:`

`Calculate total capital gains tax payable.`

`Prompt:`

`"You are a capital gains tax expert. Calculate STCG and LTCG for all assets sold.`

`Include: `
```
1. Indexed cost for property 

2. Separate calculation for equity and debt funds 

3. Applicable tax rates"
```
`Inputs Required: `
```
1. Purchase and sale details for each asset 

2. Holding period 

3. CII (Cost Inflation Index) for relevant years
```
## Prompt 14 — GST Reverse Charge Mechanism Compliance

`Backstory:`

`A 30-year-old event manager in Bengaluru hires foreign artists for shows in India. She wants to ensure proper GST payment under the reverse charge mechanism (RCM).`

`Goal:`

`Create a compliance guide for GST RCM payments.`

`Prompt:`

`"You are a GST compliance trainer. Prepare an RCM payment guide for services from foreign suppliers.`

`Include:`
```
1. Identifying RCM applicability

2. GST payment process under RCM

3. Reporting in GSTR-3B"
```
`Inputs Required:`
```
1. Nature of imported service

2. Contract/payment details

3. GST registration type
```
## Prompt 15 — Professional Tax Calculation

`Backstory:`

`A 25-year-old designer in Mumbai works for a private firm and earns ₹45,000/month. She wants to know her monthly professional tax deduction and annual liability.`

`Goal:`

`Calculate professional tax payable.`

`Prompt:`

`"You are a payroll tax advisor. Calculate monthly and annual professional tax for Maharashtra.`

`Include:`
```
1. Applicable slab rate

2. Annual total payable"
```
`Inputs Required:`
```
1. Monthly salary

2. State of employment
```
## Prompt 16 — Tax Planning for First-Time Home Buyer

`Backstory:`

`A 30-year-old banking professional from Hyderabad has just booked her first apartment worth ₹55 lakhs, with a home loan sanctioned for 80% of the value. She is aware that there are multiple tax benefits under Section 24(b) for interest payment and Section 80C for principal repayment, but she’s unsure how to maximize these in the first year since her EMIs start mid-year. She wants a clear, optimized plan to ensure no eligible deduction is missed.`

`Goal:`

`Prepare a year-wise tax benefit plan for a first-time home buyer.`

`Prompt:`

`"You are a housing loan tax specialist. For the given home loan details, prepare a plan to maximize deductions in the current and following years.`

`Include:`
```
1. Deduction under Section 80C for principal repayment

2. Deduction under Section 24(b) for interest paid

3. First-time buyer benefits under Section 80EEA (if eligible)

4. Tips to align EMI start date and pre-EMI interest for better deductions"
```
`Inputs Required:`
```
1. Home loan sanction letter with EMI start date

2. Loan amount, tenure, and interest rate

3. Date of possession/registration

4. Annual income and tax regime
```
## Prompt 17 — NRI Tax Compliance Checklist

`Backstory:`

`A 33-year-old software engineer from Bengaluru is currently working in Singapore but has investments in Indian FDs, mutual funds, and an apartment rented out in India. She files her taxes from abroad but often misses details about DTAA benefits, repatriation rules, and rental income TDS compliance. She needs a consolidated annual checklist to ensure she meets all NRI tax obligations without penalties.`

`Goal:`

`Create a comprehensive tax compliance checklist for NRIs with Indian income.`

`Prompt:`

`"You are an NRI taxation consultant. Prepare a checklist for annual tax compliance for an NRI with Indian investments.`

`Include:`
```
1. DTAA applicability and claiming benefits

2. Reporting and paying tax on rental income

3. Capital gains tax on Indian asset sales

4. Repatriation and FEMA compliance"
```
`Inputs Required:`
```
1. Country of residence

2. List of Indian income sources

3. Details of property ownership and tenants

4. Any recent asset sales
```
## Prompt 18 — GST Compliance Calendar for Startups

`Backstory:`

`A 26-year-old founder of a D2C skincare startup in Mumbai is newly GST-registered and unsure about filing timelines, advance tax due dates, and annual compliance requirements. She needs a startup-friendly GST + tax compliance calendar that her team can follow to avoid missing deadlines.`

`Goal:`

`Create a GST and tax compliance calendar tailored for startups.`

`Prompt:`

`"You are a business compliance advisor. Prepare a full-year GST and income tax compliance calendar for a newly registered startup.`

`Include: `
```
1. Monthly/quarterly GST filing dates 

2. Advance tax payment dates 

3. Annual return filing deadlines 

4. Audit requirements if turnover exceeds limits"
```
`Inputs Required: `
```
1. GST registration type (monthly/quarterly) 

2. Startup turnover projection 

3. Company incorporation date
```
## Prompt 19 —  Capital Gains Exemption Planning (54/54F)

`Backstory:`

`A 32-year-old doctor in Pune recently sold a piece of inherited land and made a long-term capital gain of ₹35 lakhs. She wants to invest the amount in a new residential property but is confused about which section — 54 or 54F — will give her maximum exemption. She also wants guidance on timelines and documentation to avoid losing the exemption claim.`

`Goal:`

`Advise on the best exemption strategy for reinvesting capital gains.`

`Prompt:`

`"You are a capital gains tax planner. Recommend the best section (54/54F) for claiming exemption on sale of property.`

`Include:`
```
1. Eligibility criteria for each section

2. Maximum exemption available

3. Investment timelines and conditions

4. Documentation required"
```
`Inputs Required:`
```
1. Sale deed details (date, amount)

2. Type of asset sold

3. Current property ownership status

4. Planned investment details
```
## Prompt 20 — GST Composition Scheme Evaluation

`Backstory:`

`A 27-year-old cafe owner in Jaipur has an annual turnover of ₹65 lakhs and is considering switching from the regular GST scheme to the composition scheme to simplify compliance. However, he’s unsure if it will be financially beneficial, especially since he won’t be able to claim ITC.`

`Goal:`

`Compare regular GST vs. composition scheme and suggest the best choice.`

`Prompt:`

`"You are a GST advisor. Evaluate whether the composition scheme is beneficial for the business.`

`Include: `
```
1. Tax liability under both schemes 

2. Compliance requirements for each 

3. Pros and cons based on business nature and supplier type"
```
`Inputs Required: `
```
1. Annual turnover 

2. Percentage of purchases with GST 

3. Industry type (goods/services)
```
## Prompt 21 — Section 80G Donation Deduction Planner

`Backstory:`

`A 25-year-old corporate employee in Gurgaon regularly donates to NGOs but is unaware of the deduction limits under Section 80G. She wants to know how much of her donations are eligible for a 50% or 100% deduction and how to structure her donations for maximum tax benefit.`

`Goal:`

`Optimize donation amounts for maximum 80G tax deduction.`

`Prompt:`

`"You are a charitable tax benefit consultant. For the given donations, calculate total eligible deduction under Section 80G.`

`Include:`
```
1. Classification of donations (50%/100% with/without restriction)

2. Maximum claimable deduction based on gross total income

3. Suggested donation structuring for next year"
```
`Inputs Required:`
```
1. List of donations with NGO name, amount, and registration status

2. Annual gross total income
```
## Prompt 22 — GST ITC Reconciliation with GSTR-2B

`Backstory:`

`A 29-year-old electronics retailer in Delhi files GST returns monthly but often faces ITC mismatches because suppliers upload invoices late. She wants an automated process to reconcile ITC claimed in her books with ITC available in GSTR-2B.`

`Goal:`

`Create a monthly GST ITC reconciliation workflow.`

`Prompt:`

`"You are a GST reconciliation expert. Develop a monthly process to match ITC in purchase register with GSTR-2B data.`

`Include:`
```
1. Identifying mismatched invoices

2. Communicating with suppliers for corrections

3. Updating ITC claims before filing GSTR-3B"
```
`Inputs Required:`
```
1. Purchase register for the month

2. GSTR-2B download from portal

3. Supplier list and contact details
```
## Prompt 23 — Salary Structure Optimization for Tax Savings

`Backstory:`

`A 30-year-old sales manager in Bengaluru receives a fixed CTC but can request changes to salary components during annual appraisal. He wants to restructure his salary to reduce taxable income — possibly adding meal vouchers, LTA, or higher HRA — without reducing in-hand pay.`

`Goal:`

`Design a tax-optimized salary structure.`

`Prompt:`

`"You are a payroll tax planner. Suggest changes to salary components to reduce taxable income without lowering net pay.`

`Include: `
```
1. Allowances and reimbursements with tax benefits 

2. Revised gross and taxable salary comparison 

3. Justification for each change"
```
`Inputs Required: `
```
1. Current salary structure with components 

2. Living city (metro/non-metro) 

3. Eligible reimbursements from employer policy
```
## Prompt 24 — GST Refund Claim for Exporters

`Backstory:`

`A 28-year-old handicraft exporter in Jaipur ships products to Europe and the US. She pays GST on raw material purchases but exports goods without charging GST (zero-rated supplies). She wants to claim a refund of accumulated ITC quickly and without errors.`

`Goal:`

`Guide through GST refund claim for exporters.`

`Prompt:`

`"You are a GST export compliance advisor. Create a step-by-step guide to claim refund of unutilized ITC for exports.`

`Include: `
```
1. Preparing required documentation 

2. Filing refund application on GST portal 

3. Common mistakes to avoid"
```
`Inputs Required: `
```
1. Purchase invoices with GST paid 

2. Export invoices and shipping bills 

3. Bank realization certificates
```
## Prompt 25 — Pre-Filing Personal Tax Health Check

`Backstory:`

`A 33-year-old HR manager in Pune files her taxes every July but often scrambles last minute to collect documents, leading to missed deductions. She wants a “tax health check” 3 months before filing to prepare everything in advance.`

`Goal:`

`Create a pre-filing personal tax readiness checklist.`

`Prompt:`

`"You are a personal tax consultant. Prepare a pre-filing tax readiness checklist for salaried individuals.`

`Include:`
```
1. Collecting Form 16, 26AS, and AIS

2. Reviewing investment proofs

3. Listing all deduction documents

4. Cross-checking income sources"
```
`Inputs Required:`
```
1. Salary structure

2. List of deductions claimed

3. Investment and insurance documents
```

# Financial reporting templates

## Prompt 1 — Monthly Profit & Loss Report for Startup

`Backstory:`

`A 27-year-old founder in Bengaluru runs a food delivery cloud kitchen. She receives payments from Swiggy, Zomato, and direct orders, while paying for rent, salaries, raw materials, and delivery partners. At month-end, she struggles to put together a P&L because income comes in different formats and expenses are logged inconsistently. She wants a standardized monthly P&L report to track growth and investor readiness.`

`Goal:`

`Create a clean, standardized monthly profit and loss report for a small business.`

`Prompt:`

`"You are a startup finance analyst. Prepare a monthly P&L report in Excel format.`

`Include:`
```
1. Revenue split by channel (Swiggy, Zomato, direct orders)

2. COGS calculation (raw materials, packaging)

3. Operating expenses (rent, salaries, utilities)

4. Net profit/loss calculation

5. Month-over-month percentage change"
```
`Inputs Required:`
```
1. Monthly sales data by channel

2. List of expenses with amounts

3. Previous month’s P&L for comparison

4. GST-inclusive or exclusive figures
```
## Prompt 2 — Cash Flow Statement for Freelancers

`Backstory:`

`A 29-year-old freelance UI/UX designer in Pune receives payments from clients in India and abroad, often months apart. She sometimes faces cash shortages because her expense planning isn’t aligned with irregular income. She wants a monthly cash flow statement showing inflows, outflows, and projected balances to plan better.`

`Goal:`

`Prepare a monthly cash flow statement with projections.`

`Prompt:`

`"You are a personal finance tracker. Prepare a cash flow statement for the freelancer.`

`Include:`
```
1. Total cash inflows by source

2. Total cash outflows by category (software subscriptions, rent, marketing)

3. Net cash flow (surplus/deficit)

4. Projected cash position for next 3 months"
```
`Inputs Required:`
```
1. Monthly income by source

2. Monthly expenses by category

3. Outstanding client invoices with due dates

4. Expected large future expenses
```
## Prompt 3 — Quarterly Investor Update Report

`Backstory:`

`A 30-year-old co-founder of a SaaS startup in Hyderabad has seed investors who require quarterly performance updates. They expect financial KPIs, revenue growth, expense ratios, and future plans in a professional, visually appealing format. The founders have raw numbers but no structured presentation.`

`Goal:`

`Create a polished quarterly investor update report with financial metrics.`

`Prompt:`

`"You are a startup reporting specialist. Create a quarterly investor update with:`
```
1. Revenue growth % (QoQ)

2. Gross and net profit margins

3. Burn rate and runway analysis

4. Customer acquisition cost and lifetime value

5. Graphs showing financial trends"
```
`Inputs Required:`
```
1. Quarterly financial statements

2. Operational KPIs

3. Investor reporting preferences (Excel, PDF, Slides)
```
## Prompt 4 — Annual Budget vs. Actual Report

`Backstory:`

`A 32-year-old operations head at a digital marketing agency in Delhi prepared an annual budget at the start of the year. Now, management wants to compare actuals with the budget to identify overspending areas and better plan next year’s targets.`

`Goal:`

`Prepare a detailed budget vs. actual variance report.`

`Prompt:`

`"You are a budgeting analyst. Prepare an annual budget vs. actual report.`

`Include:`
```
1. Budgeted vs. actual revenue and expense figures

2. Variance amount and % for each line item

3. Color-coded highlights for >10% deviations

4. Notes explaining key variances"
```
`Inputs Required:`
```
1. Original annual budget

2. Actual financial results

3. Variance threshold for highlighting
```
## Prompt 5 — KPI Dashboard for E-commerce Store

`Backstory:`

`A 25-year-old online store owner in Mumbai sells fashion accessories on Shopify. She wants a financial KPI dashboard showing sales trends, gross margins, and ad spend ROI so she can decide whether to increase marketing budgets.`

`Goal:`

`Create a visual KPI dashboard linking sales, expenses, and profitability.`

`Prompt:`

`"You are an e-commerce analytics expert. Create a KPI dashboard in Excel/Google Sheets.`

`Include:`
```
1. Daily/weekly/monthly sales chart

2. Gross profit margin %

3. Ad spend vs. revenue generated

4. Customer acquisition cost

5. Return rate analysis"
```
`Inputs Required:`
```
1. Sales data by day/month

2. Ad spend records

3. Product cost data
```
Prompt 6 — Department-Wise Expense Report

Backstory:

A 31-year-old finance manager at a mid-sized IT company in Noida needs to present a quarterly expense breakdown by department (HR, Marketing, IT, Operations) to the CEO. Currently, all expenses are in one lump sum, making it hard to see which department is overspending. The CEO wants an easy-to-read report with color-coded variance indicators.

Goal:

Prepare a quarterly department-wise expense report with variance analysis.

Prompt:

"You are a corporate finance analyst. Prepare a department-wise expense report for the quarter.

Include:

1. Total spend per department

2. Budgeted vs. actual spend

3. Variance in ₹ and %

4. Highlight overspending in red and underspending in green"

Inputs Required:

1. Expense data categorized by department

2. Quarterly budgets for each department

3. Variance threshold for highlighting

Prompt 7 — GST Collection & Payment Summary

Backstory:

A 28-year-old owner of a small electronics store in Surat wants a monthly GST report summarizing total GST collected from customers and GST paid to suppliers, along with net payable or refundable amounts. This helps him prepare for GST return filing without last-minute stress.

Goal:

Create a GST collection and payment summary for the month.

Prompt:

"You are a GST accountant. Prepare a monthly GST summary report.

Include: 

1. Total GST collected on sales 

2. Total GST paid on purchases 

3. Net GST payable or refundable 

4. Invoice count for sales and purchases"

Inputs Required: 

1. Sales invoice list with GST amounts 

2. Purchase invoice list with GST amounts 

3. GST rate applicable

Prompt 8 — Project-Based Profitability Report

Backstory:

A 30-year-old project manager in a construction company in Pune handles multiple client projects. Management wants to know which projects are most profitable by comparing revenue generated with direct costs and allocated overheads.

Goal:

Prepare a profitability report for each active project.

Prompt:

"You are a project finance analyst. Create a profitability report for all projects.

Include:

1. Revenue earned

2. Direct costs (materials, labor)

3. Overhead allocation

4. Net profit and profit margin % per project"

Inputs Required:

1. Project revenue and cost data

2. Overhead allocation method

3. Project timelines

Prompt 9 — Sales Performance Report by Region

Backstory:

A 25-year-old sales analyst at a consumer goods company in Kolkata needs to prepare a monthly report showing sales performance across North, South, East, and West India. The company uses this to adjust regional marketing budgets.

Goal:

Create a region-wise sales performance report.

Prompt:

"You are a sales reporting specialist. Prepare a monthly regional sales report.

Include:

1. Total sales per region

2. Growth rate vs. last month

3. Contribution % of each region to total sales

4. Top-selling products per region"

Inputs Required:

1. Monthly sales data by region

2. Previous month’s sales data

3. Product category mapping

Prompt 10 — Startup Burn Rate & Runway Report

Backstory:

A 27-year-old startup founder in Bengaluru needs to present the company’s financial health to potential investors. She wants a burn rate (monthly net cash outflow) and runway (months before funds run out) calculation based on current expenses and bank balance.

Goal:

Create a burn rate and runway report for a startup.

Prompt:

"You are a startup finance analyst. Prepare a burn rate and runway calculation.

Include:

1. Average monthly operating expense

2. Current bank balance

3. Estimated months of runway

4. Scenario analysis for reduced or increased spending"

Inputs Required:

1. Last 6 months’ expense data

2. Current cash reserves

3. Any expected large future expenses

Prompt 11 — Balance Sheet Template for MSMEs

Backstory:

A 32-year-old owner of a small textile manufacturing unit in Tiruppur needs a professional balance sheet format for bank loan applications. His current records are handwritten and lack standard accounting presentation.

Goal:

Provide a clean, MSME-friendly balance sheet template.

Prompt:

"You are an accounting documentation expert. Create a balance sheet template for MSMEs.

Include:

1. Assets (current, non-current)

2. Liabilities (short-term, long-term)

3. Equity section

4. Automated total calculation formulas"

Inputs Required:

1. Asset and liability lists with values

2. Preferred reporting currency

3. Reporting date

Prompt 12 — Expense Claim Reimbursement Report

Backstory:

A 26-year-old HR coordinator in Delhi needs to submit a monthly reimbursement report for employee travel, meals, and office purchases. The finance department requires itemized claims with approval status.

Goal:

Prepare an expense claim reimbursement report.

Prompt:

"You are a corporate HR accountant. Create a monthly employee expense reimbursement report.

Include:

1. Employee name and ID

2. Expense date and category

3. Amount claimed vs. approved

4. Approval status"

Inputs Required:

1. Employee expense claim data

2. Approval records

3. Company expense categories

Prompt 13 — Inventory Valuation Report

Backstory:

A 29-year-old warehouse manager in Ahmedabad needs a quarterly inventory valuation for the finance team using the weighted average cost method. This helps determine accurate COGS and year-end stock value for reporting.

Goal:

Prepare a weighted average cost inventory valuation report.

Prompt:

"You are a supply chain finance specialist. Create a quarterly inventory valuation report.

Include:

1. Item name and code

2. Quantity on hand

3. Weighted average unit cost

4. Total inventory value"

Inputs Required:

1. Purchase and sales records

2. Opening inventory quantity and value

3. Valuation method

Prompt 14 — Loan Repayment Schedule Report

Backstory:

A 30-year-old business owner in Jaipur has taken multiple loans for equipment purchases. The bank requires a detailed loan repayment schedule showing principal, interest, and outstanding balance each month.

Goal:

Prepare a loan repayment schedule report.

Prompt:

"You are a loan accounting expert. Create a loan repayment schedule.

Include:

1. EMI amount split into principal and interest

2. Outstanding balance after each payment

3. Payment due dates"

Inputs Required:

1. Loan amount, tenure, and interest rate

2. EMI start date

3. Prepayment details (if any)

Prompt 15 — Profitability Report by Product Line

Backstory:

A 28-year-old FMCG entrepreneur in Lucknow sells snacks, beverages, and condiments. She wants to see which product line has the highest gross and net profitability so she can focus marketing efforts accordingly.

Goal:

Prepare a product-line profitability report.

Prompt:

"You are a product finance analyst. Prepare a profitability report for each product line.

Include:

1. Revenue per product line

2. Direct cost and gross margin %

3. Overhead allocation

4. Net profit"

Inputs Required:

1. Sales data by product line

2. Direct cost details

3. Overhead allocation rules

Prompt 16 — Monthly Management Report for SMEs

Backstory:

A 33-year-old owner of a 50-employee packaging company in Indore wants a monthly management report that summarizes the company’s performance in a way that’s easy to discuss with his leadership team. He wants a mix of financial and operational KPIs, such as revenue, expenses, production volumes, and order fulfillment rates, in a single document that is clear enough for non-finance managers to understand.

Goal:

Create a monthly management report combining financial and operational KPIs.

Prompt:

"You are an SME performance analyst. Prepare a monthly management report.

Include:

1. Revenue and expense summary

2. Gross and net profit margins

3. Key operational KPIs (units produced, order fulfillment %)

4. Commentary on performance trends

5. Action points for management"

Inputs Required:

1. Monthly sales and expense data

2. Operational KPI data

3. Previous month’s report for comparison

Prompt 17 — Fund Utilization Report for Grant-Funded Projects

Backstory:

A 29-year-old project coordinator in a Delhi-based NGO has received a ₹25 lakh grant for a year-long education project. The donor requires quarterly fund utilization reports showing how much money was spent, in which categories, and how much remains unspent. The format must be transparent and audit-friendly.

Goal:

Prepare a quarterly fund utilization report for a grant project.

Prompt:

"You are an NGO finance officer. Create a quarterly fund utilization report.

Include:

1. Grant amount received and opening balance

2. Category-wise expenditure (training, materials, staff salaries)

3. Closing balance at quarter-end

4. % of funds utilized vs. planned"

Inputs Required:

1. Grant agreement details

2. Expenditure records by category

3. Project timelines

Prompt 18 — Year-End Financial Summary for Investors

Backstory:

A 31-year-old founder of an agri-tech startup in Hyderabad needs to send an annual financial summary to existing investors. The report should show key numbers, growth vs. last year, and future projections, while maintaining a clean, professional look for investor confidence.

Goal:

Create a year-end financial performance summary.

Prompt:

"You are a startup investor relations analyst. Prepare an annual financial summary.

Include:

1. Yearly revenue, expenses, and profit/loss

2. Growth % vs. previous year

3. Major cost drivers and savings achieved

4. Forecast for next year"

Inputs Required:

1. Annual P&L

2. Previous year’s financials

3. Growth projection figures

Prompt 19 — Break-Even Analysis Report

Backstory:

A 25-year-old entrepreneur from Surat is launching a handcrafted jewelry line. She needs a break-even analysis to know how many units she must sell to cover fixed and variable costs. This will guide pricing and marketing spend decisions.

Goal:

Calculate break-even point in units and revenue.

Prompt:

"You are a business finance analyst. Prepare a break-even analysis report.

Include:

1. Fixed costs total

2. Variable cost per unit

3. Selling price per unit

4. Break-even point in units and ₹

5. Visual chart of cost vs. revenue"

Inputs Required:

1. Fixed cost details

2. Variable cost per product

3. Selling price per product

Prompt 20 — Comparative Financial Statements

Backstory:

A 34-year-old finance head at a chain of gyms in Mumbai wants side-by-side P&L statements for the last three years to show financial trends during the annual board meeting. The focus is on identifying cost control areas and revenue growth opportunities.

Goal:

Create comparative P&L statements for three years.

Prompt:

"You are a corporate reporting analyst. Prepare comparative P&L statements for 3 years.

Include:

1. Year-wise side-by-side format

2. % change year-on-year for each line item

3. Commentary on major shifts"

Inputs Required:

1. P&L statements for the last 3 years

2. Notes on significant events affecting results

Prompt 21 — Cost Centre Report for Multi-Branch Company

Backstory:

A 30-year-old finance manager at a retail chain in Chennai needs to prepare monthly reports for each store location (cost centre). The head office wants to know which locations are profitable and which are running at a loss.

Goal:

Prepare a branch-wise cost centre report.

Prompt:

"You are a retail finance analyst. Create a monthly cost centre report.

Include: 

1. Revenue per branch 

2. Operating costs per branch 

3. Profit/loss per branch 

4. Ranking branches by profitability"

Inputs Required: 

1. Sales and expense data by branch 

2. Overhead allocation rules

Prompt 22 — Expense Ratio Analysis for Mutual Fund House

Backstory:

A 28-year-old performance analyst at a mutual fund company in Mumbai wants to analyze operating expense ratios for different fund categories to ensure they are competitive with industry averages.

Goal:

Prepare an expense ratio analysis report.

Prompt:

"You are a mutual fund reporting analyst. Prepare an expense ratio analysis by fund category.

Include:

1. Expense ratio for each fund

2. Industry average comparison

3. Recommendations for cost optimization"

Inputs Required:

1. Fund NAV and expense data

2. Industry benchmarks

Prompt 23 — Monthly Sales & Expense Consolidated Report

Backstory:

A 27-year-old entrepreneur in Delhi runs two separate businesses — a café and an online bakery. She wants a consolidated monthly report combining sales and expenses for both ventures to get a single profitability view.

Goal:

Prepare a consolidated monthly sales and expense report.

Prompt:

"You are a multi-business finance analyst. Prepare a monthly consolidated report.

Include:

1. Sales total for each business and combined total

2. Expense total for each business and combined total

3. Net profit/loss for each business and combined"

Inputs Required:

1. Monthly sales and expense data for both businesses

2. Allocation of shared expenses

Prompt 24 — Variance Analysis for Manufacturing Costs

Backstory:

A 32-year-old production head in a chemical manufacturing company in Gujarat wants to analyze the difference between standard cost estimates and actual manufacturing costs for the quarter. This helps in improving cost control measures.

Goal:

Prepare a manufacturing cost variance report.

Prompt:

"You are a manufacturing cost analyst. Prepare a quarterly variance report.

Include:

1. Standard cost vs. actual cost for materials, labor, and overheads

2. Variance amount and %

3. Root cause analysis of major variances"

Inputs Required:

1. Standard cost sheet

2. Actual cost records

3. Production volume data

Prompt 25 — Annual Compliance Reporting Template

Backstory:

A 29-year-old compliance officer at a fintech company in Bengaluru needs an annual report format that includes financial performance, compliance activities, and statutory audit summaries for submission to regulators.

Goal:

Create a structured compliance and performance annual report template.

Prompt:

"You are a corporate governance reporting expert. Create an annual compliance and performance report template.

Include:

1. Financial summary section

2. Compliance activities and audits section

3. Risk assessment section

4. Future compliance plan"

Inputs Required:

1. Annual financial statements

2. Compliance activity records

3. Audit reports


Business valuation & ROI calculation

Prompt 1 — Pre-Funding Startup Valuation

Backstory:

A 29-year-old founder from Bengaluru runs a SaaS platform for small retailers. She’s in talks with angel investors but needs to present a credible pre-funding valuation. The startup has been operational for 18 months, has ₹1.2 crore in ARR, and is growing at 15% month-on-month. She wants a valuation based on both revenue multiples and the discounted cash flow (DCF) method so she can justify her ask during investor meetings.

Goal:

Calculate a pre-funding valuation using multiple methods.

Prompt:

*"You are a startup valuation analyst. Calculate the company’s pre-funding valuation using:

1. Revenue multiple (based on SaaS industry norms)

2. Discounted Cash Flow (DCF) method with realistic assumptions

3. Comparison table of both results

4. Brief investor-friendly explanation of methodology"*

Inputs Required:

1. Current ARR and MRR

2. Last 12 months’ financials

3. Growth rate assumptions

4. Industry-standard multiples

5. Discount rate for DCF

Prompt 2 — ROI Calculation for New Product Launch

Backstory:

A 31-year-old FMCG entrepreneur in Pune plans to launch a new flavored beverage line. She has projected development and marketing costs of ₹40 lakhs and expects to sell 2 lakh units in the first year. She wants to know the ROI for year one and over a three-year horizon, factoring in unit price, expected margins, and marketing expenses.

Goal:

Calculate ROI for a product launch over multiple time frames.

Prompt:

*"You are a product finance analyst. Calculate ROI for the product launch:

1. Year 1, Year 2, and Year 3 ROI %

2. Break-even point in units and revenue

3. Payback period in months"*

Inputs Required:

1. Development, production, and marketing costs

2. Unit selling price and cost per unit

3. Sales projections for 3 years

Prompt 3 — Valuation for Business Sale

Backstory:

A 34-year-old restaurateur in Mumbai is considering selling his 4-year-old fine dining restaurant. He has consistent annual revenues of ₹3 crores with a 15% net profit margin. The buyer wants a fair market valuation considering both the asset value and earnings potential.

Goal:

Calculate fair market valuation using asset-based and earnings multiples methods.

Prompt:

*"You are a business broker. Calculate valuation using:

1. Net Asset Value method

2. Earnings Before Interest, Taxes, Depreciation, and Amortization (EBITDA) multiple

3. Final valuation range combining both approaches"*

Inputs Required:

1. Latest P&L statement

2. List of tangible and intangible assets

3. Industry multiple range for restaurants

Prompt 4 — ROI from Digital Marketing Campaign

Backstory:

A 27-year-old D2C brand owner in Jaipur ran a 6-month Facebook and Instagram ad campaign costing ₹18 lakhs. The campaign generated 1.8 crore in sales, but she’s unsure of the true ROI after considering product costs, returns, and ad agency fees.

Goal:

Calculate net ROI from the campaign after all costs.

Prompt:

*"You are a marketing ROI analyst. Calculate ROI for the campaign:

1. Gross sales generated

2. Deduct product costs, returns, and agency fees

3. Present net ROI % and ROI in ₹ terms"*

Inputs Required:

1. Campaign spend

2. Sales data from the campaign

3. COGS and return rates

4. Agency commission percentage

Prompt 5— Pre-IPO Company Valuation

Backstory:

A 32-year-old CFO at a mid-sized tech firm in Hyderabad is preparing for a possible IPO. The company has ₹250 crores in annual revenue, strong profitability, and significant brand presence. He wants a valuation using comparable listed company multiples and DCF to present to investment bankers.

Goal:

Estimate pre-IPO valuation using market comparables and DCF.

Prompt:

*"You are an investment banker. Calculate valuation using:

1. Comparable company analysis (P/E, EV/EBITDA multiples)

2. Discounted cash flow model

3. Sensitivity analysis based on different growth and discount rate assumptions"*

Inputs Required:

1. Historical financials for 3–5 years

2. Projected financials for next 5 years

3. Peer company valuation multiples

Prompt 6 — Valuation of Franchise Business

Backstory:

A 30-year-old entrepreneur in Ahmedabad operates 3 franchise outlets of a popular coffee chain. Each outlet has consistent footfall and steady profits, but the franchisor is changing royalty rates next year. She wants to value her franchise operations to negotiate with a potential buyer who is interested in taking over all three outlets.

Goal:

Calculate the valuation of the franchise considering operational profits and future royalty changes.

Prompt:

*"You are a franchise valuation consultant. Calculate the business value using:

1. EBITDA multiple method (based on industry range)

2. Adjustments for royalty rate change impact

3. Sensitivity analysis for profit fluctuations"*

Inputs Required:

1. Last 3 years’ P&L for each outlet

2. Franchise agreement details (royalty % and terms)

3. Industry benchmark multiples

Prompt 7 — ROI for New Manufacturing Equipment

Backstory:

A 28-year-old production manager in a textile unit in Surat is considering buying an advanced weaving machine costing ₹1.2 crores. The machine promises higher efficiency and reduced wastage, potentially increasing annual profits by ₹25 lakhs. Management wants to know the ROI and payback period before approving the purchase.

Goal:

Calculate ROI and payback period for new equipment investment.

Prompt:

*"You are a manufacturing finance analyst. Calculate:

1. Annual ROI % from cost savings and added revenue

2. Payback period in years

3. Net Present Value (NPV) over the equipment’s useful life"*

Inputs Required:

1. Equipment cost

2. Annual profit increase from efficiency gains

3. Useful life of equipment

4. Discount rate for NPV calculation

Prompt 8 — Startup Valuation for Seed Funding

Backstory:

A 26-year-old founder in Delhi has built a health-tech app with 50,000 monthly active users but limited revenue. She wants a valuation for seed funding discussions using the Berkus method and comparable early-stage startup deals.

Goal:

Value a pre-revenue startup using alternative valuation methods.

Prompt:

*"You are a startup funding advisor. Estimate valuation using:

1. Berkus Method

2. Comparable early-stage deal multiples (based on user base)

3. Final recommended valuation range"*

Inputs Required:

1. User base and growth rate

2. Product stage and traction metrics

3. Comparable funding deal data

Prompt 9 — ROI from Corporate Training Program

Backstory:

A 33-year-old HR manager in Mumbai spent ₹15 lakhs on a leadership training program for mid-level managers. She wants to show management the ROI by correlating it to reduced attrition and improved productivity.

Goal:

Calculate ROI from training investment using HR metrics.

Prompt:

*"You are an HR analytics consultant. Calculate training ROI:

1. Tangible benefits (productivity gains, attrition cost savings)

2. Intangible benefits (employee satisfaction, engagement)

3. ROI % and payback period"*

Inputs Required:

1. Training costs

2. Attrition rates before and after training

3. Productivity metrics before and after training

Prompt 10 — Valuation for ESOP Pricing

Backstory:

A 31-year-old CFO at a fintech startup in Bengaluru needs to determine the fair market value (FMV) of shares for issuing ESOPs to employees, in compliance with Indian tax laws.

Goal:

Calculate FMV for ESOP allotment.

Prompt:

*"You are a corporate finance advisor. Calculate FMV using:

1. DCF method

2. Net asset value method

3. Choose most appropriate based on company stage"*

Inputs Required:

1. Company financial statements

2. Future cash flow projections

3. Industry multiples

Prompt 11 — ROI for Retail Store Renovation

Backstory:

A 28-year-old boutique owner in Chandigarh is planning a ₹10 lakh renovation to improve store design and customer experience. She expects this to increase footfall by 30% and sales by 20%.

Goal:

Calculate ROI from store renovation.

Prompt:

*"You are a retail finance consultant. Calculate:

1. Incremental revenue from renovation

2. ROI % over 3 years

3. Payback period"*

Inputs Required:

1. Renovation cost

2. Current monthly sales

3. Expected % increase in sales

Prompt 12 — Startup Exit Valuation

Backstory:

A 34-year-old founder in Hyderabad is negotiating an acquisition offer for his B2B SaaS startup. He needs to know if the offer aligns with industry exit multiples and his company’s growth potential.

Goal:

Estimate fair acquisition value using market data.

Prompt:

*"You are an M&A analyst. Calculate exit valuation using:

1. Revenue multiple

2. EBITDA multiple

3. Comparison with recent industry exits"*

Inputs Required:

1. Current ARR and EBITDA

2. Industry exit deal database

3. Growth rate

Prompt 13 — ROI for Solar Panel Installation

Backstory:

A 30-year-old factory owner in Nagpur is considering installing solar panels costing ₹50 lakhs to reduce electricity bills. The panels are expected to save ₹9 lakhs annually.

Goal:

Calculate ROI and payback period for solar investment.

Prompt:

*"You are a sustainability finance analyst. Calculate:

1. Annual savings and ROI %

2. Payback period in years

3. 10-year NPV considering maintenance costs"*

Inputs Required:

1. Installation cost

2. Annual savings on electricity

3. Maintenance costs

4. Discount rate

Prompt 14 — Franchise ROI Evaluation

Backstory:

A 27-year-old entrepreneur in Jaipur is considering buying a fast-food franchise for ₹35 lakhs upfront and ₹3 lakhs/month operating costs. Expected monthly revenue is ₹6 lakhs.

Goal:

Evaluate ROI and feasibility of the franchise.

Prompt:

*"You are a franchise ROI consultant. Calculate:

1. Monthly and annual ROI %

2. Break-even point

3. 5-year payback analysis"*

Inputs Required:

1. Franchise investment cost

2. Monthly operating cost

3. Expected monthly revenue

Prompt 15 — Valuation of E-commerce Business for Sale

Backstory:

A 32-year-old e-commerce entrepreneur in Mumbai runs an Amazon store with ₹5 crores in annual revenue and ₹80 lakhs profit. She wants to sell the business and needs a valuation based on profit multiples and market comparables.

Goal:

Calculate e-commerce business valuation.

Prompt:

*"You are an e-commerce business broker. Calculate valuation using:

1. Seller’s Discretionary Earnings (SDE) multiple

2. Comparable online store sales data"*

Inputs Required:

1. Annual revenue and profit

2. SDE adjustments

3. Comparable sales data

Prompt 16 — ROI of Influencer Marketing

Backstory:

A 26-year-old fashion startup founder in Delhi spent ₹12 lakhs on influencer campaigns. She wants to measure the ROI by comparing sales generated directly from influencer links vs. the cost.

Goal:

Calculate influencer marketing ROI.

Prompt:

*"You are a marketing analytics consultant. Calculate:

1. Total revenue from influencer-driven sales

2. ROI %

3. CAC vs. LTV of customers acquired"*

Inputs Required:

1. Campaign cost

2. Sales from tracked influencer links

3. Average customer lifetime value

Prompt 17 — Valuation for Partnership Buyout

Backstory:

A 31-year-old co-owner of a small manufacturing unit in Ahmedabad wants to buy out his partner’s 50% stake. He needs a valuation that is fair to both parties using earnings multiples and asset valuations.

Goal:

Calculate a fair buyout value.

Prompt:

*"You are a partnership valuation expert. Calculate buyout value using:

1. Earnings multiple method

2. Net asset value method

3. Final blended value"*

Inputs Required:

1. Annual profit and assets list

2. Industry multiple range

Prompt 18 — ROI for Event Sponsorship

Backstory:

A 28-year-old beverage brand owner in Bengaluru sponsored a major sports event for ₹20 lakhs. She wants to calculate ROI in terms of increased sales and brand awareness.

Goal:

Evaluate event sponsorship ROI.

Prompt:

*"You are a brand ROI analyst. Calculate:

1. Incremental sales revenue post-event

2. ROI %

3. Intangible benefits summary"*

Inputs Required:

1. Sponsorship cost

2. Sales before and after event

3. Brand awareness survey data

Prompt 19 — Liquidation Value Estimation

Backstory:

A 33-year-old manufacturing business owner in Pune needs to shut down operations and sell assets. She wants to know the liquidation value of machinery, inventory, and other assets for settlement planning.

Goal:

Estimate liquidation value of assets.

Prompt:

*"You are an asset valuation consultant. Calculate:

1. Current market resale value for each asset

2. Total liquidation value after disposal costs"*

Inputs Required:

1. Asset list with purchase details

2. Current market price estimates

3. Disposal costs

Prompt 20 — ROI for R&D Project

Backstory:

A 30-year-old pharma company R&D head in Hyderabad is testing a new drug formulation. The project costs ₹2 crores and could generate ₹50 lakhs annually for 8 years if approved.

Goal:

Calculate ROI and NPV for the R&D project.

Prompt:

*"You are a pharma project analyst. Calculate:

1. Annual ROI %

2. Payback period

3. NPV over 8 years"*

Inputs Required:

1. Project cost

2. Annual revenue projections

3. Approval success probability

4. Discount rate

Prompt 21 — Valuation for Joint Venture Negotiation

Backstory:

A 29-year-old agri-business owner in Punjab is forming a joint venture with a logistics company. She needs a valuation of her business to determine equity split.

Goal:

Value business for JV equity discussions.

Prompt:

*"You are a joint venture valuation advisor. Calculate valuation using:

1. Comparable transactions method

2. Earnings multiple method"*

Inputs Required:

1. Business revenue and profits

2. Comparable JV deal data

Prompt 22 — ROI of Employee Wellness Program

Backstory:

A 32-year-old HR head in Gurgaon implemented a wellness program costing ₹10 lakhs. She wants to evaluate its ROI through reduced sick days and improved productivity.

Goal:

Calculate ROI for wellness programs.

Prompt:

*"You are an HR ROI analyst. Calculate:

1. Tangible savings from reduced absenteeism

2. Productivity gains in ₹ terms

3. ROI %"*

Inputs Required:

1. Program cost

2. Sick leave data before and after program

3. Productivity measurement metrics

Prompt 23 — Pre-Merger Synergy Valuation

Backstory:

A 34-year-old founder in Bengaluru is merging with a competitor. She needs to estimate the additional value generated from synergies like shared distribution and reduced marketing costs.

Goal:

Calculate synergy value for a merger.

Prompt:

*"You are an M&A consultant. Calculate:

1. Cost savings from synergy

2. Incremental revenue potential

3. Total synergy valuation"*

Inputs Required:

1. Current cost structures of both companies

2. Expected revenue increase

3. Industry synergy benchmarks

Prompt 24 — ROI of Export Market Expansion

Backstory:

A 30-year-old textile exporter in Tiruppur invested ₹25 lakhs in entering the European market. She wants to know the ROI based on first-year export orders and projected growth.

Goal:

Evaluate export expansion ROI.

Prompt:

*"You are an export business analyst. Calculate:

1. ROI % in first year

2. Payback period

3. 3-year ROI projection"*

Inputs Required:

1. Market entry costs

2. Export sales data

3. Growth assumptions

Prompt 25 — Valuation for Buy-Sell Agreement

Backstory:

A 33-year-old partner in a law firm in Delhi wants a formal valuation for their buy-sell agreement in case one partner exits. The valuation must consider earnings, client base value, and goodwill.

Goal:

Prepare a valuation for a professional services partnership.

Prompt:

*"You are a professional services valuation expert. Calculate:

1. Earnings-based valuation

2. Goodwill valuation based on client retention rate"*

Inputs Required:

1. Annual revenue and profits

2. Client list and retention rate

3. Comparable firm multiples
