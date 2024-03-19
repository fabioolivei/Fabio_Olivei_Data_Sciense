ML - Card Fraud
==============================

* ### [**Billions in Losses Avoided! Machine Learning in the Fight Against Card Fraud:**](https://github.com/fabioolivei/Fabio_Olivei_Data_Sciense/blob/main/ML_Card_Fraud/notebooks/Ml_Fraud.ipynb)


<div align="center">

<img src="https://miro.medium.com/v2/resize:fit:720/format:webp/1*mnxrPjQxlHBdty3ZiVW8iw.png" />

</div>

**Situation:** A company processes R$ 500 billion in transactions, within which R$ 7.5 billion are fraudulent. Without an effective detection model, the company was only able to detect and prevent 15% of these frauds, equating to R$ 1.125 billion, leaving R$ 6.375 billion in frauds undetected.

**Task:** The critical task was to enhance fraud detection capabilities to mitigate the substantial financial losses incurred due to undetected frauds. The goal was to leverage Machine Learning to significantly improve the detection and prevention of fraudulent transactions.

**Action:** In this project, we embarked on developing and fine-tuning a Machine Learning model to accurately identify fraudulent transactions. Through rigorous experimentation and optimization, the best performing model identified was an advanced Machine Learning model, specifically designed to pinpoint fraudulent activities with high precision.

**Result:** With the implementation of the optimal Machine Learning model, we managed to identify R$ 7.05 billion as potential frauds. Remarkably, R$ 6.2 billion of this amount were confirmed frauds, which the model successfully helped to avoid. Consequently, the company managed to significantly reduce its losses by preventing an additional R$ 6.2 billion in fraudulent transactions. This outcome underscores the pivotal role of Machine Learning in enhancing operational efficiency and safeguarding financial assets.

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
