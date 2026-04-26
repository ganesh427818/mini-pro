import streamlit as st
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
import os

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(
page_title="Flight Delay Prediction",
layout="wide"
)

st.title(
"✈ Flight Delay Prediction System"
)

st.write(
"Machine Learning Based Flight Delay Predictor"
)


# -------------------------
# PATHS
# -------------------------
BASE_DIR=os.path.dirname(__file__)

MODEL_PATH=os.path.join(
BASE_DIR,
"..",
"model",
"flight_delay_model.pkl"
)

DATA_PATH=os.path.join(
BASE_DIR,
"..",
"dataset",
"flight_delay_dataset_200.csv"
)


# -------------------------
# LOAD MODEL
# -------------------------
try:

    with open(
    MODEL_PATH,
    "rb"
    ) as f:

        model=pickle.load(f)

except Exception as e:

    st.error(
    f"Model file not found : {e}"
    )

    st.stop()


# -------------------------
# LOAD DATASET
# -------------------------
try:

    data=pd.read_csv(
    DATA_PATH
    )

except Exception as e:

    st.error(
    f"Dataset not found : {e}"
    )

    st.stop()



# -------------------------
# CATEGORY MAPS
# -------------------------
airlines=data["Airline"].unique()
origins=data["Origin"].unique()
dests=data["Destination"].unique()
aircrafts=data["Aircraft_Type"].unique()

airline_map={
a:i for i,a in enumerate(airlines)
}

origin_map={
a:i for i,a in enumerate(origins)
}

dest_map={
a:i for i,a in enumerate(dests)
}

aircraft_map={
a:i for i,a in enumerate(aircrafts)
}



# -------------------------
# SIDEBAR
# -------------------------
st.sidebar.header(
"Enter Flight Details"
)

flight_no=st.sidebar.number_input(
"Flight Number",
101,
999,
150
)

airline=st.sidebar.selectbox(
"Airline",
airlines
)

origin=st.sidebar.selectbox(
"Origin",
origins
)

destination=st.sidebar.selectbox(
"Destination",
dests
)

aircraft=st.sidebar.selectbox(
"Aircraft Type",
aircrafts
)

temperature=st.sidebar.slider(
"Temperature",
0.0,
50.0,
30.0
)

wind=st.sidebar.slider(
"Wind Speed",
0.0,
100.0,
20.0
)

visibility=st.sidebar.slider(
"Visibility",
0.0,
20.0,
10.0
)

rain=st.sidebar.slider(
"Precipitation",
0.0,
20.0,
2.0
)

traffic=st.sidebar.slider(
"Air Traffic",
0.0,
500.0,
150.0
)



# -------------------------
# INPUT DATA
# -------------------------
sample=pd.DataFrame({

"Flight_Number":[flight_no],

"Airline":[
airline_map[airline]
],

"Origin":[
origin_map[origin]
],

"Destination":[
dest_map[destination]
],

"Temperature":[temperature],

"Wind_Speed":[wind],

"Visibility":[visibility],

"Precipitation":[rain],

"Air_Traffic":[traffic],

"Aircraft_Type":[
aircraft_map[aircraft]
]

})


prediction=15

# -------------------------
# PREDICT
# -------------------------
if st.button(
"Predict Flight Delay"
):

    prediction=model.predict(
    sample
    )[0]

    st.success(
    f"Predicted Delay = {prediction:.2f} Minutes"
    )

    if prediction<15:
        st.write(
        "Status : On Time"
        )

    elif prediction<30:
        st.write(
        "Status : Moderate Delay"
        )

    else:
        st.write(
        "Status : High Delay"
        )



# -------------------------
# VALUES
# -------------------------
st.subheader(
"Current Input Values"
)

st.write(
sample
)



# -------------------------
# GRAPH 1
# -------------------------
st.subheader(
"Temperature vs Delay"
)

fig1=plt.figure()

x=np.linspace(
0,
50,
20
)

y=x*0.5 + wind*0.3 + traffic*0.03

plt.plot(
x,
y
)

plt.scatter(
temperature,
prediction,
s=150
)

plt.xlabel(
"Temperature"
)

plt.ylabel(
"Delay"
)

st.pyplot(
fig1
)



# -------------------------
# GRAPH 2
# -------------------------
st.subheader(
"Traffic Impact"
)

fig2=plt.figure()

tx=np.linspace(
0,
500,
20
)

dy=tx*0.05+temperature

plt.plot(
tx,
dy
)

plt.scatter(
traffic,
prediction,
s=150
)

plt.xlabel(
"Traffic"
)

plt.ylabel(
"Delay"
)

st.pyplot(
fig2
)



# -------------------------
# BAR GRAPH
# -------------------------
st.subheader(
"Weather Factors"
)

fig3=plt.figure()

labels=[
"Temp",
"Wind",
"Rain",
"Traffic"
]

vals=[
temperature,
wind,
rain*10,
traffic/10
]

plt.bar(
labels,
vals
)

st.pyplot(
fig3
)



# -------------------------
# RISK
# -------------------------
risk=(
temperature+
wind+
rain+
traffic/10
)

st.subheader(
"Delay Risk Level"
)

if risk<50:

    st.success(
    "Low Risk"
    )

elif risk<100:

    st.warning(
    "Medium Risk"
    )

else:

    st.error(
    "High Risk"
    )