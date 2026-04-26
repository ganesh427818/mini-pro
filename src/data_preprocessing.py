import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

def load_dataset(path):
    data = pd.read_csv(path)
    return data

def preprocess_data(data):

    # Handle missing values
    data = data.dropna()

    # Encode categorical variables
    le = LabelEncoder()

    data["Airline"] = le.fit_transform(data["Airline"])
    data["Origin"] = le.fit_transform(data["Origin"])
    data["Destination"] = le.fit_transform(data["Destination"])
    data["Aircraft_Type"] = le.fit_transform(data["Aircraft_Type"])

    # Normalize numerical data
    scaler = StandardScaler()

    num_cols = [
        "Temperature",
        "Wind_Speed",
        "Visibility",
        "Precipitation",
        "Air_Traffic"
    ]

    data[num_cols] = scaler.fit_transform(data[num_cols])

    return data, scaler