# COVID-19 Global Impact Analysis for India - Short Report

## What is this?
I built this data science project to track and analyze the covid situation in India, keeping it aligned with the World Health Organization (WHO) reporting standard. It basically pulls data, makes some graphs, and uses a time series model (Prophet) to predict what might happen in the next couple of months.

## Where did the data come from?
I didn't hardcode any data. It's fetched using a python script from disease.sh APIs. These APIs just aggregate the official numbers from the Indian Ministry of Health and Family Welfare (MoHFW) and WHO.

- WHO Dashboard: [WHO COVID-19](https://covid19.who.int/)
- Source API: [disease.sh API Documentation](https://disease.sh/)
- Real Link for India State Data: [Statewise API Link](https://disease.sh/v3/covid-19/gov/India)
- Real Link for India Historical Data: [Historical API Link](https://disease.sh/v3/covid-19/historical/India?lastdays=all)
- Official Government Portal: [Ministry of Health and Family Welfare (MoHFW), India](https://www.mohfw.gov.in/)

## Summary Report
1. **High Recovery Rate:** The visualizations clearly show that the majority of infected individuals in India have successfully recovered. The active cases today are very low compared to historical peaks.
2. **State Distribution:** States like Maharashtra and Kerala have recorded the highest total cases historically. However, their active case count is now minimal, and recoveries form the largest part of the statistics.
3. **Forecasting Stability:** The Prophet model predicts a stable, flat trend for daily new cases over the next 60 days, indicating that the situation remains under control.

---
*This report and the associated Streamlit Dashboard were built to showcase Data Extraction, Data Analysis with Pandas, Data Visualization with Plotly, and Time-Series Forecasting skills.*
