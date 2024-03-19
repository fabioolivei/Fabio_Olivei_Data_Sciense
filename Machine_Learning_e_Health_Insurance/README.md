Machine_Learning_e_Health_Insurance
==============================

* ### [**Machine Learning and Health Insurance**](https://github.com/fabioolivei/Fabio_Olivei_Data_Sciense/blob/main/Machine_Learning_e_Health_Insurance/notebooks/Machine_Learning_e_Health_Insurance_Impacto_na_Previs%C3%A3o_de_Seguros_de_Sa%C3%BAde.ipynb)

<div align="center" >

<img src="https://media.licdn.com/dms/image/D4D12AQFhjYnh9YPVQQ/article-cover_image-shrink_720_1280/0/1704463771968?e=1714608000&v=beta&t=DAQzeITTnvwhfglzk0nWg-QYtx0y1cB_jPXXb4BS7WQ" width=700 />

</div>

- **Business Understanding:**
The dataset focuses on predicting health insurance costs based on factors such as age, gender, Body Mass Index (BMI), number of children, smoking status, and region. Understanding these relationships is crucial for insurers to price policies accurately.

**Situation:** Without an effective risk prediction model for health insurance, an insurer serving 50,000 clients faces a yearly challenge: 5,000 of these clients incur high and unexpected medical expenses. This lack of foresight prevents the insurer from adjusting its policies and pricing accurately, resulting in significant financial losses.

**Task:** To mitigate these losses and improve accuracy in insurance policy pricing, the insurer needs to develop a Machine Learning model capable of identifying clients at high risk of incurring elevated medical expenses in advance, taking into account variables such as age, gender, BMI, number of children, smoking habits, and region.

**Action:** The insurer opted to implement an optimized Gradient Boosting Regressor model, recognized for its superior performance in regression tasks. This model was trained to analyze clients' historical data and risk factors, identifying those most likely to generate high costs. The analysis and modeling considered factors such as the number of children, smoking habits, and BMI, as well as evaluated regional differences to adapt pricing and coverage strategies more effectively.

**Result:** With the implementation of the Gradient Boosting Regressor model, the insurer was able to accurately identify 4,000 clients with the potential for high medical expenses, of which 3,500 actually incurred elevated costs. This advancement allowed the insurer to better adjust its policies and pricing strategies for these clients, avoiding surprises and financial losses. Adopting this model not only increased operational efficiency and financial sustainability for the insurer but also enabled the offering of more personalized and fair health plans, significantly improving customer satisfaction and service. This data-driven approach reinforces the power of risk analysis and predictive modeling in optimizing health insurance management.

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
