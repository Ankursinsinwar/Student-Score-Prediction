# Student Exam Score Predictor

This project predicts student exam scores based on various factors such as hours studied, number of practice tests taken, attendance rate, and sleep hours. It uses a trained machine learning model and is deployed with Streamlit for an interactive user interface.

## Features
- Input features:
  - **Hours Studied** (0-10)
  - **Number of Practice Tests Taken** (0-10)
  - **Attendance Rate (%)** (0-100)
  - **Sleep Hours** (0-10)
- Predicts the **exam score** based on the provided inputs.

## Tech Stack
- **Python** (Machine Learning Model)
- **Streamlit** (Web UI)
- **Scikit-learn** (Model Training)
- **Pickle** (Model Serialization)
- **NumPy** (Data Processing)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Ankursinsinwar/Student-Score-Prediction.git
   cd student-score-predictor
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

Model Training
--------------

The machine learning model was trained using a regression algorithm and saved as student_score.pkl using pickle. The model takes four input features and predicts the exam score.

Usage
-----

*   Enter the required inputs (study hours, practice tests, attendance rate, sleep hours).
    
*   Click the "Predict Exam Score" button.
    
*   The model will predict the student's exam score.
    

File Structure
--------------
```
├── app.py                  # Streamlit Web App
├── student_score.pkl        # Trained ML Model
├── student_score_pridiction.ipynb # Jupyter Notebook (Model Training)
├── requirements.txt         # Required Libraries
```

Dependencies
------------

Ensure you have the following installed:

*   Python 3.x
    
*   Streamlit
    
*   Scikit-learn
    
*   NumPy
    
*   Pickle

## UI 
![image](https://github.com/user-attachments/assets/1a7b1697-ec01-4895-ae18-acb99828cc9c)


This project is open-source and contributions are welcome!
