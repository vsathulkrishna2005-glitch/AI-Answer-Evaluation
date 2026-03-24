# 🧠 AI-Based Student Answer Evaluation System

A smart web application that automatically evaluates student answers using **Natural Language Processing (NLP)** and **AI-based semantic similarity**.

---

## 🚀 Features

* ✅ Evaluate student answers using AI
* 🤖 Semantic similarity using transformer models
* 📊 Marks generation (out of 10)
* 💬 Automatic feedback system
* 🔍 Missing keyword detection
* 📂 Bulk evaluation using CSV upload
* 🏆 Student ranking system
* 📥 Export results to Excel
* 🔐 User authentication (Login/Register system)
* 🎨 Modern dark-themed UI

---

## 🛠️ Tech Stack

* **Frontend:** HTML, CSS
* **Backend:** Flask (Python)
* **AI/NLP:** Sentence Transformers, Scikit-learn, NLTK
* **Database:** SQLite
* **Other:** Pandas, Gunicorn

---

## 🧠 How It Works

1. User enters a **reference answer** and a **student answer**
2. The system uses **AI embeddings** to understand semantic meaning
3. Calculates similarity score using cosine similarity
4. Converts similarity into marks
5. Generates feedback and highlights missing keywords

---

## 📂 Project Structure

```
student-grading-system/
│
├── app.py
├── requirements.txt
├── Procfile
├── users.db
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   └── results.html
│
└── static/
    └── style.css
```

---

## ⚙️ Installation & Setup

1. Clone the repository:

```
git clone https://github.com/your-username/your-repo-name.git
```

2. Navigate to the project folder:

```
cd student-grading-system
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Run the application:

```
python app.py
```

5. Open in browser:

```
http://127.0.0.1:5000/
```

---

## 🔐 Login System

* Users can **register and login**
* Credentials are stored in an **SQLite database**
* Session-based authentication is used

---

## 📊 CSV Format for Bulk Evaluation

```
name,answer
Rahul,Java is an object oriented programming language
Priya,Java is programming language
```

---

## 🌐 Deployment

The project can be deployed using platforms like:

* Render
* Railway
* Heroku

---

## 🧠 Future Enhancements

* 🔐 Password hashing for better security
* 📊 Dashboard with charts
* 🧑‍🏫 Multi-teacher system
* 🌐 Live deployment with custom domain

---

## 👨‍💻 Author

Developed by Athul

---

## ⭐ Note

This project is developed as part of a BCA final year project and demonstrates the use of AI in education technology.
