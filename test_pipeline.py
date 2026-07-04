import os
import pandas as pd
import pytest

def test_data_directories_exist():
    """Test if the data folder exists after the pipeline runs."""
    assert os.path.exists('data'), "Data directory should exist."

def test_historical_data_validity():
    """Test if historical data is fetched, saved, and contains expected columns."""
    file_path = 'data/covid_19_india_historical.csv'
    assert os.path.exists(file_path), "Historical data CSV is missing."
    
    df = pd.read_csv(file_path)
    assert not df.empty, "Historical dataframe is empty."
    assert 'Daily New Cases' in df.columns, "'Daily New Cases' column is missing."
    assert 'Date' in df.columns, "'Date' column is missing."

def test_state_data_validity():
    """Test if state data is fetched, saved, and contains expected columns."""
    file_path = 'data/StatewiseTestingDetails.csv'
    assert os.path.exists(file_path), "State data CSV is missing."
    
    df = pd.read_csv(file_path)
    assert not df.empty, "State dataframe is empty."
    assert 'State' in df.columns, "'State' column is missing."
    assert 'Total Confirmed' in df.columns, "'Total Confirmed' column is missing."
