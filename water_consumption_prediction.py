import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv('data/global_wf_175_crops_average_2010_2019.csv')
print(df.head())
# Drop rows with missing values (or use df.fillna() if you prefer)
df = df.dropna()

# Features and target
X = df.drop(columns=['wf_tot_m3_t'])
y = df['wf_tot_m3_t']

# Identify categorical and numerical features
categorical_features = ['crop_name', 'crop_group']
numerical_features = ['production_t', 'wfg_m3_t', 'wfb_cr_m3_t', 'wfb_i_m3_t']

# Preprocessing: encode categorical data
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
    ],
    remainder='passthrough'  # Keep numerical features as is
)

# Pipeline with preprocessing and model
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
])

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R^2 Score:", r2_score(y_test, y_pred))
