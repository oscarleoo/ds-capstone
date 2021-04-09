import numpy as np
import pandas as pd


def adjust_weather_timestamp(df, correct_hour=16):
    """
    This function takes the weather data from one site and shifts it
    so that the hour with the highest average temperature is the
    same as "correct_hour"
    
    Inputs:
        df - The weather data for a specific site
        correct_hour - The hour that should have the highest average temnperature
        
    Outputs:
        df - The shifted weather data
    """
    df['hour'] = df.timestamp.dt.hour
    max_hour = df.groupby('hour').mean()['air_temperature'].sort_values().index[-1]
    n_hours = correct_hour - max_hour
    df.timestamp = df.timestamp +  pd.to_timedelta(n_hours, unit='h')
    return df.drop('hour', axis=1)


def add_missing_rows_to_weather(weather_df):
    """
    This function adds missing rows to the weather dataframe.
    
    Input:
        weather_df - The weather data
        
    Outputs:
        df - The weather data with added rows
    """
    corrected_sites = []
    start = pd.to_datetime('2016-01-01')
    expected_timestamps = [start + pd.to_timedelta(i * 3600, unit='s') for i in range(26304)]
    for site_id in weather_df.site_id.unique():
        site_df = pd.DataFrame(expected_timestamps, columns=['timestamp'])
        site_df = site_df.merge(weather_df[weather_df.site_id == site_id], on='timestamp', how='left')
        site_df.site_id = site_id
        corrected_sites.append(site_df)
    
    return pd.concat(corrected_sites).sort_values('timestamp')


def interpolate_weather_data(weather_df):
    """
    This function replaces missing values through interpolation
    
    Inputs:
        df - The DataFrame to fill values for
        group_column - The column to group by
        
    Outputs:
        df - A DataFrame without NaN values
    """
    return weather_df.groupby('site_id').apply(lambda group: group.interpolate(limit_direction='both'))


def remove_bad_start(df, n_values_to_keep):
    """
    Saves the last n_values_to_keep in the sequence
    
    Inputs:
        df - The dataframe to filter
        n_values_to_keep - The number of values to keep
        
    Outputs:
        df - A DataFrame with length n_values_to_keep
    """
    return df[-n_values_to_keep:]


def remove_constants(df, constant_length):
    """
    Removes sequences of constant values
    
    Inputs:
        df - The dataframe to filter
        constant_length - The minimum length of sequences to remove
        
    Outputs:
        df - A DataFrame without long sequences of constant values
    """
    df['std'] = df.meter_reading.rolling(constant_length, center=True, min_periods=1).std().round()
    return df[df['std'] != 0].drop('std', axis=1)


def remove_zeros(df, zero_length):
    """
    Removes sequences of zeros
    
    Inputs:
        df - The dataframe to filter
        constant_length - The minimum length of sequences to remove
        
    Outputs:
        df - A DataFrame without long sequences of zeros
    """
    df['mean'] = df.meter_reading.rolling(zero_length, center=True, min_periods=1).mean().round()
    return df[df['mean'] != 0].drop('mean', axis=1)


def apply_filter(df, building_ids, meter, filter_function):
    """
    A helper function that decides if the filter should be applied
    
    Inputs:
        df - The dataframe to filter
        building_ids - The ids to apply the filter to
        meter - the meters to apply the filter to
        filter_function - The filter to apply
        
    Outputs:
        df - A filtered or unfiltered dataframe
    """
    if df.iloc[0].building_id not in building_ids:
        return df
    if df.iloc[0].meter != meter:
        return df
    else:
        return filter_function(df)

def filter_groups(df, building_ids, meter, filter_function):
    """
    A function that groups a the datafram on building_id and meter
    and then applies the filter to each group by using the "apply_filter" helper.
    
    Inputs:
        df - The dataframe to filter
        building_ids - The ids to apply the filter to
        meter - the meters to apply the filter to
        filter_function - The filter to apply
        
    Outputs:
        df - A filtered or unfiltered dataframe
    """
    df = df.sort_values('timestamp')
    df = df.groupby(['building_id', 'meter'])
    df = df.apply(lambda group: apply_filter(group, building_ids, meter, filter_function))
    return df.reset_index(drop=True)

