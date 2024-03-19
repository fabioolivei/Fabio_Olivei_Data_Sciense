ML Applications in Fetal Health Diagnostics
==============================


<div align="center">

<img src="https://miro.medium.com/v2/resize:fit:720/format:webp/1*A0vtvf_qYlpJMR3VXeBiSw.png" />

</div>

**Situation:** The primary goal of this project was to develop a Machine Learning (ML) model capable of accurately classifying fetal health into three categories: 'Normal', 'Suspect', and 'Pathological'. This initiative aimed at enhancing prenatal care by facilitating the early detection and intervention of fetal health issues. Utilizing a comprehensive clinical dataset, including vital parameters like fetal heartbeat patterns, movements, and uterine contractions, was critical for the model's development.

**Task:** The task was to design a model that not only classifies fetal health with high accuracy but also effectively utilizes the clinical dataset to achieve a high AUC-ROC score. The ultimate objective was to support early detection and intervention strategies, thereby improving pregnancy outcomes and enhancing prenatal care efficiency.

**Action:** A Gradient Boosting Classifier model was selected and developed due to its ability to handle complex datasets and its strong performance in classification tasks. The model was trained on various features, including 'baseline value', 'accelerations', 'fetal_movement', and more, with a particular focus on 'abnormal_short_term_variability' and 'mean_value_of_short_term_variability', which were anticipated to be significant predictors.

**Result:** The Gradient Boosting Classifier model demonstrated exceptional performance metrics, with an accuracy of 95.77%, an AUC of 98.45%, and high recall and precision rates. The F1 score of 95.62% indicated a balanced performance between precision and recall, while the Kappa score of 88.30% and the MCC of 88.50% highlighted the model's substantial agreement and high quality in binary classifications, respectively. Clinically relevant features, particularly related to fetal heart rate monitoring, were identified as pivotal in the model's predictive capability. The successful development and implementation of this model represent a significant advancement in applying machine learning to fetal health monitoring, offering a reliable tool for healthcare professionals to support better clinical outcomes in prenatal care.

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
