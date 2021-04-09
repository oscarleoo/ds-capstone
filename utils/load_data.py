import pandas as pd


def load_data():
    """
    This function loads both the training and test datasets.
    It converts the timestamps to pandas datatime and adds
    building information and weather data to train and test.
    
    Outputs:
        train - DataFrame with training data
        test - DataFrame with testing data
    """
    
    # Load data
    weather = pd.concat([pd.read_csv('data/weather_train.csv'), pd.read_csv('data/weather_test.csv')])
    building_metadata = pd.read_csv('data/building_metadata.csv')
    train = pd.read_csv('data/train.csv')
    test = pd.read_csv('data/test.csv')
    
    # Convert to pandas datetime
    weather['timestamp'] = pd.to_datetime(weather['timestamp'])
    train['timestamp'] = pd.to_datetime(train['timestamp'])
    test['timestamp'] = pd.to_datetime(test['timestamp'])
    
    return train, test, weather, building_metadata