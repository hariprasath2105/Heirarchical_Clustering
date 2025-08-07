# User Behavior Clustering (Hierarchical Clustering)

This project demonstrates a simple **Hierarchical Clustering** model to classify website or app users based on their behavior, such as usage time and session data. The model is deployed using **Flask**, and the frontend is styled using **HTML and CSS** with a gradient background.

---

## 🚀 Features
- Hierarchical Clustering using `scipy` and `sklearn`
- Scaled inputs using `StandardScaler`
- Flask-based web interface for input and cluster prediction
- Gradient background and clean styled form UI
- Visual cluster representation

---

## 📂 Project Structure

```
project_folder/
│
├── static/
│   └── style.css          # Styled form with background and UI enhancements
│
├── templates/
│   ├── index.html         # Input form page
│   └── result.html        # Result page with cluster & chart
│
├── app.py                 # Flask app to handle routes and predictions
├── model.py               # Clustering model training and saving (with pickle)
├── user_behavior.csv      # Dataset used for training the model
└── model.pkl              # Saved clustering model and scaler
```

---

## 🧠 Input Features
- **Daily Usage (Minutes)** — total time spent per day
- **Sessions Per Day** — number of app/site sessions per day
- **Average Session Length (Minutes)** — avg. time per session

---

## 📌 How It Works
1. User enters input values on the web form.
2. Values are scaled using the saved `StandardScaler`.
3. The saved Hierarchical clustering model predicts the cluster.
4. The result and a visual chart are displayed.

---

## ⚙️ How to Run

1. Install dependencies:
```bash
pip install flask numpy pandas matplotlib scipy scikit-learn
```

2. Run the model training (if not done yet):
```bash
python model.py
```

3. Start the Flask app:
```bash
python app.py
```

4. Open your browser and visit `http://127.0.0.1:5000`

---

## 📊 Output Example
- Cluster Number: `Cluster 1`
- Visualization: Cluster plot with your data point highlighted

---

## 📁 Dataset Source
A mock dataset (`user_behavior.csv`) was used to simulate user activity.

---

## 📌 Note
This model is for demonstration purposes and may require scaling and customization for production use.