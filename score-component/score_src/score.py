import argparse
import joblib  
import pandas as pd  
from pathlib import Path
import os
import pickle

parser = argparse.ArgumentParser("score")
parser.add_argument("--model_input", type=str, help="Path of input model")
parser.add_argument("--test_data", type=str, help="Path to test data")
parser.add_argument("--score_output", type=str, help="Path of scoring output")
args = parser.parse_args()

# cargar el modelo entrenado:
filename = "decission_tree_model.pkl"
model = pickle.load(open((Path(args.model_input) / filename), "rb")) 

test_data = pd.read_csv(args.test_data)
X_test = test_data.drop(columns=['Potability'])
y_pred = model.predict(X_test)

test_data['predictions'] = y_pred

test_data.to_csv(args.score_output)