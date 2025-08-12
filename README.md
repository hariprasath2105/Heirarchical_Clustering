# User Behavior Clustering (Hierarchical)

This project demonstrates a simple **Hierarchical Clustering** model to classify website or app users based on their behavior, such as usage time and session data. The model is deployed using **Flask**, and the frontend is styled using **HTML and CSS** with a gradient background.

---

## Features
- Hierarchical Clustering using `scipy` and `sklearn`
- Scaled inputs using `StandardScaler`
- Flask-based web interface for input and cluster prediction
- Visual cluster representation

---
## Tech Stack

- Python
- Flask
- HTML, CSS
- Scikit-learn
- Pandas
- Numpy
- Matplotlib

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-003366?style=for-the-badge&logo=matplotlib&logoColor=white)

---
## Project Structure

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

## Input Features
- **Daily Usage (Minutes)** — total time spent per day
- **Sessions Per Day** — number of app/site sessions per day
- **Average Session Length (Minutes)** — avg. time per session

---

## How It Works
1. User enters input values on the web form.
2. Values are scaled using the saved `StandardScaler`.
3. The saved Hierarchical clustering model predicts the cluster.
4. The result and a visual chart are displayed.

---

## How to Run

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
