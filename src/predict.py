import numpy as np

def predict_delay(model, scaler, sample):

    sample = scaler.transform([sample])

    sample = np.array(sample)

    sample = sample.reshape((1,1,sample.shape[1]))

    prediction = model.predict(sample)

    return prediction[0][0]