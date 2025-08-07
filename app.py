from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
import pickle
from scipy.cluster.hierarchy import fcluster

app = Flask(__name__)

# Load model and scaler
with open("model.pkl", "rb") as f:
    Z, scaler = pickle.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        usage = float(request.form['usage_minutes'])
        sessions = float(request.form['sessions_per_day'])
        avg_session = float(request.form['avg_session_length'])

        input_data = np.array([[usage, sessions, avg_session]])
        scaled = scaler.transform(input_data)

        cluster = fcluster(Z, t=3, criterion='maxclust')[0]

        # Visualization
        df = pd.read_csv("website_usage_behavior.csv")
        X = df[['Daily_Usage_Minutes', 'Sessions_Per_Day', 'Average_Session_Length']]
        scaled_data = scaler.transform(X)
        df['cluster'] = fcluster(Z, t=3, criterion='maxclust')

        plt.figure(figsize=(8, 6))
        for c in sorted(df['cluster'].unique()):
            subset = scaled_data[df['cluster'] == c]
            plt.scatter(subset[:, 0], subset[:, 1], label=f"Cluster {c}", alpha=0.6)

        plt.scatter(scaled[0, 0], scaled[0, 1], color='red', s=100, label='You', edgecolors='black')
        plt.xlabel("Usage (scaled)")
        plt.ylabel("Sessions Per Day (scaled)")
        plt.title("User Cluster Placement")
        plt.legend()

        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        plot_data = base64.b64encode(buf.read()).decode('ascii')
        plt.close()

        return render_template("result.html", cluster=cluster,
                               usage=usage, sessions=sessions,
                               avg_session=avg_session, plot_url=plot_data)

    except Exception as e:
        return f"Error processing input: {e}"

if __name__ == '__main__':
    app.run(debug=True)
