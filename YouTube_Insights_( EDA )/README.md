YouTube Insights ( EDA )
==============================

* ### [**YouTube Insights ( EDA ):**](https://github.com/fabioolivei/Fabio_Olivei_Data_Sciense/blob/main/YouTube_Insights_(%20EDA%20)/notebooks/YouTube_Insights_Uma_An%C3%A1lise_dos_Canais_Mais_Bem_Sucedidos_da_Plataforma.ipynb)

<div align="center">

<img src="https://miro.medium.com/v2/resize:fit:720/format:webp/1*0oAVUuAAK6kiDILND2EReA.png" />

</div>

**Situation:** The landscape of YouTube has become increasingly diverse, with channels from around the world contributing to a rich tapestry of content. Recognizing the importance of understanding this ecosystem, our analysis aimed to explore the most popular YouTube channels, their categories, and the influence of different countries on the platform. Key success metrics such as the number of subscribers and video views were central to our examination, as these factors are crucial in understanding the revenue potential for creators.

**Task:** Our primary task was to conduct a thorough analysis to identify trends, patterns, and correlations within the YouTube platform. This included categorizing channels by country and genre, analyzing subscriber and view counts, and assessing the impact of these metrics on creators' earnings. The ultimate goal was to provide insights that could aid in optimizing content and marketing strategies for better engagement and profitability.

**Action:** We initiated our analysis by performing an Exploratory Data Analysis (EDA) to gain a fundamental understanding of the dataset. This involved:
- Conducting a detailed statistical description of the dataset to identify basic trends and patterns.
- Performing a temporal analysis to see how certain variables changed over time and their impact on the platform.
- Analyzing the count of channels from different countries and categorizing them to simplify comparisons and understand thematic distributions.
- Investigating trends and correlations, particularly focusing on how engagement metrics like subscriber counts and video views relate to profitability.

**Result:** Through our comprehensive analysis, we were able to uncover valuable insights into the YouTube ecosystem. We identified key trends that highlight the relationship between engagement and profitability, revealing that certain categories and countries dominate in terms of subscriber counts and views. Our findings underscore the critical role of data analysis and analytics in content and marketing strategy optimization. By understanding these dynamics, content creators and marketers can make informed decisions to enhance their content's appeal and reach, ultimately increasing engagement and revenue. This analysis not only provided a snapshot of the current YouTube landscape but also offered strategic insights for optimizing future content creation and distribution.

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
