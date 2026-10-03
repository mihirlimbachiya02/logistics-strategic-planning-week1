logistics_model.py

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

# Simulate Logistics Dataset
data = {
    "distance_km": [5.2, 12.4, 2.1, 15.0, 8.3, 4.0, 11.1],
    "package_weight_kg": [1.5, 4.0, 0.8, 10.2, 2.5, 1.1, 6.0],
    "traffic_density_index": [3, 8, 1, 9, 5, 2, 7],
    "delivery_time_mins": [18, 45, 10, 55, 30, 14, 40],
}
df = pd.DataFrame(data)

# Features and Target definition
X = df[["distance_km", "package_weight_kg", "traffic_density_index"]]
y = df["delivery_time_mins"]

# Train/Test Split & Model Training
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluation
predictions = model.predict(X_test)
print(f"Model Mean Absolute Error: {mean_absolute_error(y_test, predictions):.2f} mins")
