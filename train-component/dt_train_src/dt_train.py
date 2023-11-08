import argparse
from pathlib import Path
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

parser = argparse.ArgumentParser("dt_train")
parser.add_argument("--training_data", type=str, help="Path to training data")
parser.add_argument("--criterion", type=str, help="The function to measure the quality of a split")
parser.add_argument("--min_samples_split", type=int, help="The minimum number of samples required to split an internal node")
parser.add_argument("--max_depth", type=int, help="The maximum depth of the tree")
parser.add_argument("--model_output", type=str, help="Path of output model")

args = parser.parse_args()

print("Hola desde DT_train...")

lines = [
    f"Training data path: {args.training_data}",
    f"Criterion: {args.criterion}",
    f"Min samples Split: {args.min_samples_split}",
    f"Max depth: {args.max_depth}",
    f"Model output path: {args.model_output}",
]

print("Parametros: ...")

for line in lines:
    print(line)

training_data = pd.read_csv(Path(args.training_data))

X_train = training_data.drop(columns=['Potability'])
y_train = training_data['Potability']

dt = DecisionTreeClassifier(criterion= args.criterion, min_samples_split= args.min_samples_split, max_depth=args.max_depth)
dt.fit(X_train,y_train)

filename = Path(args.model_output) / '/decission_tree_modelo.pkl'
pickle.dump(dt, open(filename, "wb"))
print(f"Modelo guardado en el directorio: {Path(args.model_output)}")