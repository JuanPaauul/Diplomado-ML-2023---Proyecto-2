import argparse
from pathlib import Path
from sklearn.model_selection import train_test_split
import pandas as pd
import os

parser = argparse.ArgumentParser("split")
parser.add_argument("--clean_data", type=str, help="Path to a clean dataset")
parser.add_argument("--split_ratio_train", type=float, help="Split ratio given for training")
parser.add_argument("--data_train", type=str, help="Training dataset file")
parser.add_argument("--data_test", type=str, help="Testing dataset file")

args = parser.parse_args()

print("Hola desde split...")

lines = [
    f"clean_data: {args.clean_data}",
    f"split_ratio for training: {args.split_ratio_train}",
    f"data_train: {args.data_train}",
    f"data_test: {args.data_test}",
]

print("Parametros: ...")

for line in lines:
    print(line)

clean_data = pd.read_csv(args.clean_data)

train_data, test_data = train_test_split(clean_data, train_size=args.split_ratio_train , random_state=42)

train_data.to_csv(os.path.join(args.data_train, 'train-data.csv'), index=False)
test_data.to_csv(os.path.join(args.data_test, 'test-data.csv'), index=False)