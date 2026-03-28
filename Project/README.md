# Student Academic Advisor

This project predicts whether a student is likely to show good academic performance based on five inputs:

- `studytime`
- `failures`
- `absences`
- `G1`
- `G2`

The model predicts one of two labels:

- `Good Performance`
- `Needs Improvement`

## Project Structure

```
Project/
├── data/
│   └── student-data.csv
├── model/
│   └── model.pkl
├── backend/
│   ├── app.py
│   └── preprocess.py
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
├── notebook/
│   └── model_training.ipynb
├── requirements.txt
└── README.md
```

## What the notebook does

The notebook at [Project/notebook/model_training.ipynb](Project/notebook/model_training.ipynb) trains a `RandomForestClassifier`.

It performs:

1. Dataset loading from `../data/student-data.csv`
2. Missing-value handling
3. Feature selection and consistent feature ordering
4. Target creation using `G3` with a Good/Bad threshold
5. Train/test split
6. Accuracy and confusion matrix evaluation
7. Model export to `../model/model.pkl`

## Install Dependencies

```bash
pip install flask pandas scikit-learn joblib
```

Or install everything from the local file:

```bash
pip install -r requirements.txt
```

## Train the model

1. Open [Project/notebook/model_training.ipynb](Project/notebook/model_training.ipynb)
2. Run all cells
3. The trained model will be saved to [Project/model/model.pkl](Project/model/model.pkl)

## Run the backend

```bash
cd Project/backend
python app.py
```

The Flask server runs on `http://localhost:5000`.

## Open the frontend

Open [Project/frontend/index.html](Project/frontend/index.html) in your browser.

The page sends prediction requests to the Flask backend and displays the result on screen.

## Example request

```json
{
  "studytime": 2,
  "failures": 0,
  "absences": 4,
  "G1": 12,
  "G2": 13
}
```

Example response:

```json
{
  "prediction": "Good Performance"
}
```

## Notes

- The backend and notebook share the same preprocessing logic in [Project/backend/preprocess.py](Project/backend/preprocess.py).
- If any input is missing or invalid, the API returns a clear error message.
- The frontend can work when opened directly or when served from Flask.
