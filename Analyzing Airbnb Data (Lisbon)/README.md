Analyzing Airbnb Data (Lisbon)
==============================

* ### [**Analyzing Airbnb Data (Lisbon):**](https://github.com/fabioolivei/Fabio_Olivei_Data_Sciense/blob/main/Analyzing%20Airbnb%20Data%20(Lisbon)/notebooks/Analisando_os_Dados_do_Airbnb_(Lisboa).ipynb)

<div align="center">

<img src="https://camo.githubusercontent.com/c5fa04297b1d7ac37119d62a88af6d11080adb83f077c3e2a0f647f748ae0db3/68747470733a2f2f63646e2d696d616765732d312e6d656469756d2e636f6d2f6d61782f3830302f312a4a56565f526e38686a6668535f644d613854723559512e706e67" />

</div>

**Situation:** The aim of our study was to explore the Airbnb market in Lisbon, a city with deep historical ties to Brazil, noted for its unique architecture, cuisine, and hospitality. Our investigation sought to provide insights into the types of accommodations available, as well as their distribution across different neighborhoods. The data for this analysis was sourced exclusively from the Inside Airbnb website.

**Task:** Our primary task was to analyze the Airbnb listings in Lisbon to understand the variety of lodging options offered to travelers. This included categorizing the types of accommodations available and assessing their distribution and pricing across the city's neighborhoods. The goal was to offer valuable insights for travelers considering Lisbon as their next destination, as well as for property owners looking to list their properties on Airbnb.

**Action:** To accomplish our objectives, we undertook the following steps:
- **Data Acquisition:** Gathered all necessary data from the Inside Airbnb website, ensuring a comprehensive dataset that included various types of accommodations across Lisbon.
- **Analysis:** Conducted detailed analyses to:
    - Identify the types of Airbnb accommodations available (e.g., full houses/apartments, private rooms).
    - Assess the distribution of these accommodations across Lisbon's neighborhoods.
    - Calculate the average of the highest and lowest values for accommodations in the top 10 neighborhoods, providing a pricing overview.

**Result:** Our analysis revealed that the majority of Airbnb properties in Lisbon are full houses or apartments available for rent, reflecting a preference among visitors for private and spacious accommodations. There is also a substantial availability of private rooms, catering to budget-conscious travelers. Through our examination of the top 10 neighborhoods, we were able to define the average high and low pricing, offering potential visitors and property owners valuable insights into the market. This study not only highlights Lisbon's appeal as a travel destination, with its rich cultural offerings and historical significance, but also provides a clear picture of its Airbnb market, assisting travelers in making informed accommodation choices.

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
