Top 100 Highest-Grossing Movies
==============================

* ### [**Top 100 Highest-Grossing Movies:**](https://github.com/fabioolivei/Fabio_Olivei_Data_Sciense/blob/main/Top_100_Highest-Grossing_Movies/notebooks/top100movies_maiores_bilheterias.ipynb)

<div align="center">

<img src="https://miro.medium.com/v2/resize:fit:720/format:webp/1*LkNb1Mu83Vo6RMb38eKJ2Q.png" />

</div>

**Situation:** The purpose of our analysis was to explore box office revenues across different countries, genres, and time periods. This included a deep dive into the trends affecting box office revenue over time and identifying the most successful movie franchises.

**Task:** Our main tasks were to compare box office revenues by country, genre, and period; identify revenue trends over time; highlight top-performing franchises; and simplify the understanding of these trends through graphical representations. This comprehensive analysis aimed to provide a clear picture of the dynamics at play in the global movie industry.

**Action:** To achieve our objectives, we undertook several steps:
- Conducted a thorough Exploratory Data Analysis (EDA) to examine box office revenue data from various sources. This allowed us to gain a detailed understanding of the trends and patterns in the data.
- Compared box office revenues across different dimensions such as geographical location, genre of the films, and time periods to identify significant trends and outliers.
- Highlighted the most successful franchises by analyzing their performance in terms of box office revenues.
- Utilized graphical representations, including dynamic charts like bar chart races, to visualize the ranking of top-performing films and franchises over time. This approach made it easier to digest complex data and draw insights.

**Result:** The analysis provided a detailed view of the trends in box office revenues, revealing which films and distributors have dominated the box office and how revenue patterns have evolved over the years. By comparing box office revenues across different criteria, we identified key trends and success factors. The dynamic chart (bar chart race) created as a bonus helped to clearly understand the top 10 highest-grossing films, offering a visually engaging way to draw insights. This comprehensive analysis shed light on the dynamics of box office performance, contributing valuable insights for stakeholders in the film industry.

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
