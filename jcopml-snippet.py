# import library
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

# import from jcopml
from jcopml.pipeline import num_pipe, cat_pipe
from jcopml.utils import save_model, load_model
from jcopml.plot import plot_missing_value
from jcopml.feature_importance import mean_score_decrease

# Import Data
df = pd.read_csv("____________", index_col="___________", parse_dates=["____________"])
df.head()

plot_missing_value(df)

# Dataset Splitting
X = df.drop(columns="___________")
y = "_____________"

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
X_train.shape, X_test.shape, y_train.shape, y_test.shape

# Preprocessor
preprocessor = ColumnTransformer([
    ('numeric', num_pipe(), ["______________"]),
    ('categoric', cat_pipe(encoder='onehot'), ["_____________"]),
])

# Training jcopml 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from jcopml.tuning import grid_search_params as gsp

pipeline = Pipeline([
    ('prep', preprocessor),
    ('algo', KNeighborsClassifier())
])

model = GridSearchCV(pipeline, gsp._______________, cv="___", scoring='___', n_jobs=-1, verbose=1)
model.fit(X_train, y_train)

print(model.best_params_)
print(model.score(X_train, y_train), model.best_score_, model.score(X_test, y_test))

# Save Model
save_model(model.best_estimator_, "__________.pkl")
