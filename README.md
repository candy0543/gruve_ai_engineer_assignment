# **1. Project Overview**

```text
This project aims to predict hospital readmission outcomes using a diabetes dataset. 
The target variable (`readmitted`) indicates whether a patient was readmitted.

The workflow includes:
- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Stratified data splitting (train/test/unseen)
- Feature encoding
- Model training using machine learning algorithms
- Performance evaluation on a hold-out test set
- Final validation on unseen data
```

---

# **2. Environment Setup (using uv)**

```text
1. Install uv (if not installed):
   pip install uv

2. Create virtual environment:
   uv venv

3. Activate environment:
   - Windows:
     .venv\Scripts\activate
   - Mac/Linux:
     source .venv/bin/activate

4. Install dependencies:
   uv pip install -r requirements.txt
```

---

# **3. Repository Structure**

```text
.
│
├── dataset/
│   ├── diabetes_data.csv
│   ├── id_mapping.csv
│   ├── processed/
│   │   ├── train.csv
│   │   ├── test.csv
│   │   └── unseen_data.csv
│
├── notebooks/
│   └── eda_diabetic.ipynb
├── scripts/
│   └── inference.py
│
├── autogluon_model/
│   └── models/
│        ├── {model_name}
│             └── model.pkl
│
├── requirements.txt
├── README.md

```


---

# **4. Running the Training Script**

```text
To run the full pipeline:
run eda_diabetic.ipynb
```


---

# **5. Running Inferencing **

```text
To generate predictions on unseen data:

python scipts/inference.py
```

---

# **6. Model Performance**

```text
The model was evaluated on a stratified 20% hold-out test set.

Key metrics:
- Accuracy: ~0.54 

---

#  **7. Dependencies**

```text
Python Version:
- Python 3.12+

Key Libraries:
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn
```


