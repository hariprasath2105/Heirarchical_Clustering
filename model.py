import pandas as pd
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import linkage
import pickle

df = pd.read_csv("website_usage_behavior.csv")

features = ['Daily_Usage_Minutes', 'Sessions_Per_Day', 'Average_Session_Length']
X = df[features]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

Z = linkage(X_scaled, method='ward')

with open("model.pkl", "wb") as f:
    pickle.dump((Z, scaler), f)
