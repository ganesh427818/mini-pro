def create_features(data):

    data["Weather_Score"]=(
    data["Temperature"]+
    data["Wind_Speed"]+
    data["Precipitation"]
    )

    data["Traffic_Weather"]=(
    data["Air_Traffic"]*
    data["Weather_Score"]
    )

    # Historical Delay Data
    data["Route_Delay_History"]=(
    data["Delay_Minutes"].rolling(3).mean().fillna(0)
    )

    # Operational Factors
    data["Crew_Availability"]=1
    data["Gate_Changes"]=0
    data["Turnaround_Time"]=45

    return data