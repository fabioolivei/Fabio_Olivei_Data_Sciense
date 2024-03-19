* ### [**Diabetes Alert: A Machine Learning-Based App:**](https://github.com/fabioolivei/Fabio_Olivei_Data_Sciense/blob/main/Diabetes_Alert_A_Machine_Learning_Based_App/notebooks/Diabetes_Alert_A_Machine_Learning_Based_App.ipynb)

<div align="center">

<img src="https://miro.medium.com/v2/resize:fit:720/format:webp/1*3xBqh5Df8qJj98VNi2GS0w.jpeg" />

</div>

- **Situation:** In a health clinic, we attend to about 10,000 patients a month, of which 1,000 have diabetes. Before our project, only 150 of those cases were diagnosed in time for effective treatment.

- **Task:** Our mission was to develop a Machine Learning model capable of predicting diabetes cases with high precision and recall, aiming for early intervention and improved patient health management.

- **Action:** We decided to use an optimized XGBoost model for the task, due to its superior performance in classification tasks. After development, the model was implemented through a Gradio application, hosted on Hugging Face Spaces, making it accessible and easy to use by clinic staff.

- **Result:** With the deployment of our optimized model, we were able to identify 900 patients as potential diabetes cases, of which 750 actually had the disease and were diagnosed. This represented a significant increase in the detection of diabetes cases, jumping from only 150 diagnoses to 750, thanks to our diabetes prediction model.


To develop an ML model for predicting diabetes.For this project, the model was deployed using a Gradio app hosted on Hugging Face Spaces.

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
