import pandas as pd
import seaborn as sns
import itertools
import warnings
import pickle

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier

from tqdm.auto import tqdm
from tqdm_joblib import tqdm_joblib

warnings.filterwarnings("ignore")


df = pd.DataFrame(sns.load_dataset("iris"))

X = df.drop("species", axis=1)
y = df["species"]


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


rand_clsf = RandomForestClassifier(random_state=42, n_jobs=-1)


param_grid = {
    "n_estimators": [100, 200, 500],
    "max_depth": [None, 10, 20, 30],
    "min_samples_split": [2, 5, 10],
    "min_samples_leaf": [1, 2, 4],
    "max_features": ["sqrt", "log2", 0.5],
    "bootstrap": [True, False],
}


grid = GridSearchCV(rand_clsf, param_grid=param_grid, cv=5, n_jobs=-1, verbose=0)


param_combinations = list(
    itertools.product(
        param_grid["n_estimators"],
        param_grid["max_depth"],
        param_grid["min_samples_split"],
        param_grid["min_samples_leaf"],
        param_grid["max_features"],
        param_grid["bootstrap"],
    )
)

total_fits = len(param_combinations) * 5

print(f"Total fits: {total_fits}")


with tqdm_joblib(tqdm(desc="GridSearch Progress", total=total_fits)):
    grid.fit(X_train, y_train)

# Best model
best_model = grid.best_estimator_

print("\nBest Parameters:")
best_params = dict(best_model.get_params())

for key, value in enumerate(best_params):
    print(f"{value}: {best_params[value]}")

# Evaluate
score = best_model.score(X_test, y_test)
print(f"\nTest Accuracy: {score:.4f}")


# Save
with open("model.pkl", "wb") as f:
    pickle.dump(best_model, f)
