COVID-19 in Brazil and the world
==============================
* ### [**Notebook here - COVID-19 in Brazil and the world:**](https://github.com/fabioolivei/Fabio_Olivei_Data_Sciense/blob/main/COVID-19%20in%20Brazil%20and%20the%20world/notebooks/COVID_19_no_Brasil_e_no_mundo.ipynb)

<div align="center">

<img src="https://miro.medium.com/v2/resize:fit:720/format:webp/1*ftxsVkc5-34nn7Ctz9SuAw.jpeg" />

</div>

**Situation:** Three years into the COVID-19 pandemic, there's a pressing need to assess its impact globally and within Brazil. The pandemic's enduring effects on health, economy, and society necessitate a detailed examination to inform ongoing response strategies and recovery efforts. This analysis aims to provide a comprehensive statistical overview of the current situation of the disease.

**Task:** The primary task is to collect and analyze current data on COVID-19 to understand its progression and impact better. This involves examining infection rates, death tolls, recovery statistics, and other relevant data points from both Brazil and around the world. A critical aspect of this task is to ensure that the data used for analysis is reliable and up-to-date, sourced from reputable organizations and local government reports.

**Action:** To achieve our objectives, the following steps were undertaken:
- **Data Collection:** Data was meticulously gathered from authoritative sources, including the World Health Organization (WHO), the European Centre for Disease Prevention and Control (ECDC), the Organisation for Economic Co-operation and Development (OECD), the United Nations (UN), and official reports from local governments. This ensured a broad and accurate dataset for analysis.
- **Data Analysis:** Conducted a comprehensive statistical analysis of the collected data to derive insights on the disease's progression, impact, and current state. This included examining trends over time, comparing the situation across different countries, and evaluating the effectiveness of various response measures.
- **Visualization:** As a bonus, a bar chart race was created to visualize the cumulative number of recorded deaths due to COVID-19 in 10 selected countries, providing an engaging and informative perspective on the data.

**Result:** Through our rigorous data collection and analysis, we were able to gain valuable insights into the current state of the COVID-19 pandemic, both in Brazil and globally. The statistical analysis highlighted key trends and patterns in the disease's progression, helping to identify areas where efforts have been successful and where challenges remain. The bar chart race offered a unique visual representation of the pandemic's impact, emphasizing the severity and global scale of COVID-19 deaths over time. This comprehensive examination provides stakeholders with crucial information needed to guide future pandemic response and recovery strategies, underlining the importance of continued vigilance and adaptation in the face of COVID-19.

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
