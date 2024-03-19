A/B Testing Strategies in Fast Food Advertising
==============================

* ### [**A/B Testing Strategies in Fast Food Advertising:**](https://github.com/fabioolivei/Fabio_Olivei_Data_Sciense/blob/main/A-B_Testing_Strategies_in_Fast_Food_Advertising/notebooks/A_B_Testing_Strategies_in_Fast_Food_Advertising.ipynb)

<div align="center">

<img src="https://miro.medium.com/v2/resize:fit:720/format:webp/1*BiwbOpLPRZIZbBZh6RHyjQ.png" />

</div>

**Situation:** The objective was to analyze a dataset from a Fast Food Marketing Campaign to discern the impact of different promotional strategies on sales. This analysis aimed to identify which marketing promotions were most effective at driving sales, addressing the critical question of how to allocate marketing resources efficiently.

**Task:** The key question we needed to answer was which marketing promotions are most effective in driving sales. This required a detailed analysis of the dataset to compare the effectiveness of various promotional strategies employed by the fast-food chain.

**Action:** To achieve our objectives, we employed several analytical techniques, including:
- **Statistical Significance Testing:** We conducted A/B testing to compare the sales impact of different promotions. Specifically, we compared Promotion 1 vs. Promotion 2, Promotion 1 vs. Promotion 3, and Promotion 2 vs. Promotion 3. The p-values from these comparisons were analyzed to determine statistical significance.
    - Promotion 1 vs Promotion 2: p-value ≈ 4.29e-10
    - Promotion 1 vs Promotion 3: p-value ≈ 0.121
    - Promotion 2 vs Promotion 3: p-value ≈ 1.57e-06
- **Cross-Validation:** We also utilized cross-validation techniques to assess the model's performance, focusing on the Mean Squared Error (MSE) as a measure of accuracy. The lowest MSE observed was 0.085, indicating a relatively good performance of the model in that specific fold.

**Result:** The A/B testing results indicated that Promotion 1 and Promotion 3 are statistically more effective than Promotion 2 in driving sales. This was supported by the p-values, which showed significant differences between the promotions. The cross-validation process, particularly the analysis of the lowest MSE, further validated the effectiveness of our analytical approach. By identifying the most effective marketing promotions, we can now recommend focusing resources on Promotion 1 and Promotion 3 for future marketing campaigns. This analysis not only answers the key question posed but also provides a foundation for optimizing marketing strategies to enhance sales performance.
[Click here to see the full study]([https://shre.ink/rhPB](https://github.com/fabioolivei/Fabio_Olivei_Data_Sciense/blob/main/A-B_Testing_Strategies_in_Fast_Food_Advertising/notebooks/A_B_Testing_Strategies_in_Fast_Food_Advertising.ipynb))


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
