# **NextRead.ai** — A Personalized Book Recommender System Using Machine Learning

<div align="center">
  <img src="demo/6.jpeg" alt="demo image" width="70%">
</div>

---

### Built By: **Nirali Bhargava**

📧 [niralibhargava12@gmail.com](mailto:niralibhargava12@gmail.com)

---

## Project Summary

**NextRead.ai** is a user-centric book recommendation system developed using machine learning. It applies **collaborative filtering** with **K-Nearest Neighbors (KNN)** and **cosine similarity** to generate tailored book suggestions based on user preferences.

This project addresses a real-world need—helping readers explore meaningful titles from large datasets. A clean, interactive UI is built using **Streamlit**, offering a seamless user experience. The model is trained on the **Book-Crossing** dataset and is deployed on **Heroku** for accessibility.

---

## Core Technologies Used

| Category         | Tools / Libraries                     |
| ---------------- | ------------------------------------- |
| Language         | Python 3.7                            |
| Data Handling    | Pandas, NumPy                         |
| Machine Learning | scikit-learn (KNN, Cosine Similarity) |
| Model Saving     | Joblib                                |
| Web App          | Streamlit                             |

---

## Key Highlights

* Collaborative Filtering with a user-item matrix and cosine distance
* Pre-trained model for efficient, low-latency predictions
* Based on the Book-Crossing dataset with 1M+ ratings
* Interactive Streamlit UI for input and output display
* Cloud deployment on Heroku for real-time access

---

## Skills Demonstrated

* Data preprocessing and feature engineering
* Implementation of unsupervised ML algorithms (KNN)
* Use of similarity metrics for recommendation logic
* Web application development with Streamlit
* Model serialization and deployment pipelines
* Git, version control, and collaborative development practices
* End-to-end machine learning system design

---

## Algorithm Logic

1. Build a sparse user-item matrix using book rating data.
2. Apply K-Nearest Neighbors with cosine similarity to find related books based on user behavior.
3. Identify top-K books with the highest similarity scores.
4. Display recommended books via a modern web interface.

---

## Dataset Used

**Book-Crossing Dataset**
Includes:

* Book metadata (`BX-Books.csv`)
* User ratings (`BX-Book-Ratings.csv`)
* User demographics (`BX-Users.csv`)

**Source**: [Kaggle - Book Recommendation Dataset](https://www.kaggle.com/ra4u12/bookrecommendation)

---

## App Interface

<div align="center">
  <img src="demo/1.png" width="70%"><br><br>
  <img src="demo/2.png" width="70%"><br><br>
  <img src="demo/3.png" width="70%">
</div>

---

## How to Run Locally

### 1. Clone the repository:

```bash
git clone https://github.com/your-username/NextRead.ai.git
cd NextRead.ai
```

### 2. Create and activate the virtual environment:

```bash
conda create -n nextread python=3.7 -y
conda activate nextread
```

### 3. Install required packages:

```bash
pip install -r requirements.txt
```

### 4. (Optional) Train model via Jupyter Notebook:

```bash
jupyter notebook Books\ Recommender.ipynb
```

### 5. Run the Streamlit app:

```bash
streamlit run app.py
```

Then open `http://localhost:8501` in your browser.

---

## Sample Input / Output

**Input**: `"The Hobbit"`
**Output Recommendations**:

* The Lord of the Rings
* Harry Potter and the Sorcerer’s Stone
* Eragon
* Percy Jackson & the Olympians
* Chronicles of Narnia

---

## Future Enhancements

* Add auto-complete for book title inputs
* Integrate content-based filtering for a hybrid system
* Enable user authentication and session storage
* Incorporate feedback loops for improved recommendation accuracy
* Include light/dark themes and UI personalization options

---

## Recruiter Note

This project highlights the ability to build a fully functional, end-to-end machine learning application—from data wrangling and algorithm design to user interface development and cloud deployment. It reflects core strengths in **machine learning**, **Python engineering**, and delivering production-ready solutions with clear user value.

---
