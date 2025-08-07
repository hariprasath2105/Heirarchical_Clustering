# User Behavior Clustering (Hierarchical)

This project demonstrates a simple **Hierarchical Clustering** model to classify website or app users based on their behavior, such as usage time and session data. The model is deployed using **Flask**, and the frontend is styled using **HTML and CSS** with a gradient background.

---

## 🚀 Features
- Hierarchical Clustering using `scipy` and `sklearn`
- Scaled inputs using `StandardScaler`
- Flask-based web interface for input and cluster prediction
- Visual cluster representation

---

## 📂 Project Structure

```
heirarchical/
│
├── static/
│   └── style.css          
│
├── templates/
│   ├── index.html        
│   └── result.html        
│
├── app.py               
├── model.py              
├── user_behavior.csv     
└── model.pkl            
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

## Input

<img width="646" height="541" alt="image" src="https://github.com/user-attachments/assets/4f2d6074-04ec-4664-b0b5-d256cc6498d7" />

---

## Output 

<img width="646" height="627" alt="image" src="https://github.com/user-attachments/assets/170b34e3-ff40-4ab7-8bbf-9030cf4886fb" />

---

## 🙋‍♂️ Author

**Hari Prasath**  
[GitHub Profile](https://github.com/hariprasath2105)

---

## 📘 License

This project is open source and free to use.
