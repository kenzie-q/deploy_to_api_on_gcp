import sklearn
import pandas as pd
import pickle

def read_model():
    with open('data/model.pkl', 'rb') as handle:
        model = pickle.load(handle)
    return model

def predict_json(json_content):
    model = read_model()
    y = model.predict(json_content)
    return str(y)
