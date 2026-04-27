# Flight Delay Prediction System

## Project Overview
Flight Delay Prediction System is a machine learning based web application developed using Python and Streamlit to predict possible flight delays based on various factors such as weather conditions, air traffic congestion, route history and operational parameters.

The system analyzes input parameters and predicts delay time using a trained Random Forest model. It also provides interactive graphs for visualization and analysis.

## Objectives
- Predict flight delays accurately
- Analyze factors affecting delays
- Reduce uncertainty in flight operations
- Provide visual analysis using graphs

## Features
- Flight delay prediction
- Weather impact analysis
- Traffic impact analysis
- Correlation heatmap
- Interactive Streamlit interface
- Machine learning based prediction

## Technologies Used
- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Matplotlib
- Seaborn

## Project Structure
mini-pro/
│
├── app/
│   └── app.py
│
├── dataset/
│   └── flight_delay_dataset_200.csv
│
├── model/
│   └── flight_delay_model.pkl
│
├── requirements.txt
└── README.md


## Installation
Clone repository:
```bash
git clone https://github.com/yourusername/flight-delay-prediction.git
cd flight-delay-prediction
```

Create virtual environment:
```bash
python -m venv venv
```

Activate environment:


Install dependencies:
```bash
pip install -r requirements.txt
```

## Run Project
```bash
streamlit run app/app.py
```

## Output
Open browser:
http://localhost:8501

## Input Parameters Used
- Airline
- Origin
- Destination
- Aircraft Type
- Temperature
- Wind Speed
- Visibility
- Precipitation
- Air Traffic

## Prediction Graphs
- Temperature vs Delay
- Traffic Impact Analysis
- Weather Factors Analysis
- Correlation Heatmap

## Machine Learning Model
Random Forest Regressor is used for prediction.

## Future Enhancements
- Real-time airport data integration
- Deep Learning models
- Live flight API integration
- Deployment in cloud
- Improved prediction accuracy

## Team Member
Ganeshkumar S
Siva kumar R
Mohamed Aman S
