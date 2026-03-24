from flask import Flask, render_template, request, redirect, url_for, session
from flask import Flask, render_template, request
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import nltk
from nltk.corpus import stopwords
import string
import pandas as pd

nltk.download('stopwords')

app = Flask(__name__)
app.secret_key = "secret123"
USERNAME = "admin"
PASSWORD = "1234"
model = SentenceTransformer('all-MiniLM-L6-v2')


# ---------- PREPROCESS ----------
def preprocess(text):
    text = text.lower()
    words = text.split()
    words = [word for word in words if word not in stopwords.words('english')]
    words = [word.strip(string.punctuation) for word in words]
    return " ".join(words)


# ---------- AI SIMILARITY ----------
def calculate_similarity(reference, student):
    embeddings = model.encode([reference, student])

    similarity = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0]

    return similarity


# ---------- MAIN PAGE ----------
@app.route('/', methods=['GET', 'POST'])
def index():
    if 'user' not in session:
        return redirect(url_for('login'))
    marks = None
    similarity = None
    feedback = ""

    if request.method == 'POST':
        reference = request.form['reference']
        student = request.form['student']

        similarity = calculate_similarity(reference, student)
        marks = round(similarity * 10, 2)

        # FEEDBACK LOGIC
        if marks >= 8:
            feedback = "🔥 Excellent answer! Covers most key points."
        elif marks >= 5:
            feedback = "👍 Good answer, but missing some important details."
        elif marks >= 2:
            feedback = "⚠️ Needs improvement. Try to include more key points."
        else:
            feedback = "❌ Poor answer. Revise the concept and try again."

    return render_template('index.html', marks=marks, similarity=similarity, feedback=feedback)


# ---------- CSV FEATURE ----------
@app.route('/evaluate_csv', methods=['POST'])
def evaluate_csv():
    file = request.files['file']
    reference = request.form['reference']

    df = pd.read_csv(file)

    results = []

    for index, row in df.iterrows():
        student_name = row['name']
        student_answer = row['answer']

        similarity = calculate_similarity(reference, student_answer)
        marks = round(similarity * 10, 2)

        # Feedback
        if marks >= 8:
            feedback = "Excellent"
        elif marks >= 5:
            feedback = "Good"
        elif marks >= 2:
            feedback = "Needs Improvement"
        else:
            feedback = "Poor"

        results.append({
            'name': student_name,
            'marks': marks,
            'feedback': feedback
        })

    # Convert to DataFrame for ranking
    results_df = pd.DataFrame(results)

    # Ranking (highest marks first)
    results_df = results_df.sort_values(by='marks', ascending=False)
    results_df['rank'] = range(1, len(results_df) + 1)

    # Save Excel file
    results_df.to_excel("results.xlsx", index=False)

    return render_template('results.html', results=results_df.to_dict(orient='records'))
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == USERNAME and password == PASSWORD:
            session['user'] = username
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error="Invalid Credentials")

    return render_template('login.html')
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))
# ---------- RUN ----------
if __name__ == '__main__':
    app.run()