import os
import pandas as pd
import requests
import logging

# Configure professional logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def fetch_covid_data():
    logging.info("Starting COVID-19 data fetch pipeline...")
    
    # Create data directory if it doesn't exist
    if not os.path.exists('data'):
        os.makedirs('data')
        logging.info("Created 'data' directory.")
        
    try:
        # Fetching historical data
        logging.info("Fetching historical data from disease.sh API...")
        historical_url = "https://disease.sh/v3/covid-19/historical/India?lastdays=all"
        hist_response = requests.get(historical_url, timeout=15)
        hist_response.raise_for_status()
        
        hist_data = hist_response.json()
        
        # Parse timeline
        timeline = hist_data['timeline']
        dates = list(timeline['cases'].keys())
        cases = list(timeline['cases'].values())
        deaths = list(timeline['deaths'].values())
        recovered = list(timeline['recovered'].values())
        
        # Create DataFrame
        hist_df = pd.DataFrame({
            'Date': dates,
            'Total Cases': cases,
            'Total Deaths': deaths,
            'Total Recovered': recovered
        })
        
        # Calculate daily new cases
        hist_df['Daily New Cases'] = hist_df['Total Cases'].diff().fillna(0)
        
        hist_df.to_csv('data/covid_19_india_historical.csv', index=False)
        logging.info("Successfully saved historical data to data/covid_19_india_historical.csv")
        
    except Exception as e:
        logging.error(f"Failed to fetch historical data: {e}")
        
    try:
        # Fetching state wise data
        logging.info("Fetching state-wise data from disease.sh API...")
        state_url = "https://disease.sh/v3/covid-19/gov/India"
        state_response = requests.get(state_url, timeout=15)
        state_response.raise_for_status()
        
        state_data = state_response.json()
        states = state_data['states']
        
        state_df = pd.DataFrame(states)
        
        # Rename columns to match what the dashboard expects
        state_df = state_df.rename(columns={
            'state': 'State',
            'cases': 'Total Confirmed',
            'deaths': 'Total Deaths',
            'recovered': 'Total Recovered',
            'active': 'Active Cases'
        })
        
        state_df.to_csv('data/StatewiseTestingDetails.csv', index=False)
        logging.info("Successfully saved state data to data/StatewiseTestingDetails.csv")
        
    except Exception as e:
        logging.error(f"Failed to fetch state data: {e}")
        
    logging.info("Data pipeline execution completed.")

if __name__ == "__main__":
    fetch_covid_data()
