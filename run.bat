@echo off
echo ===================================================
echo COVID-19 India Analysis - Data Pipeline ^& Dashboard
echo ===================================================
echo.
echo [1/2] Running Data Fetching Pipeline...
python fetch_data.py
echo.
echo [2/2] Starting Streamlit Dashboard...
streamlit run app.py
pause
