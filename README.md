Product Categorization
==============================

Product Categorization with Machine Learning

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
    ├── scraping
    │   └── scraping
    |       └── spiders    <- Crawlers scripts.
    |
    |
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
    ├── tests              <- Automated tests
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org

## Prerequisite
- [Docker(Compose)](https://docs.docker.com)

## Build docker image
```sh
docker-compose build
```

## Running specs
```sh
docker-compose run web make test
```

## Crawl public product's info from an e-commerce
The spider script collect product info from Petlove's site.
After spider script has finished, a `dataset.csv` file will be generated to `data/external` directory.
```
  docker-compose run web make crawl_petlove
```

## Make a prediction
Run docker container
```sh
docker-compose up -d
```
Make HTTP request using curl:
```sh
curl -d '{"name": "Ração Premier Pet Formula Cães Adultos Raças Pequenas","description": "Indicada para cães adultos de raça pequena, Ração Sabor Frango, Contem apenas ingredientes nobres e selecionados sob rigoroso controle de qualidade, Pelagem bonita e saudável, rico em acido graxo essenciais, Omega 3 e Omega 6, Ajuda no equilibrio intestinal, combinação de ingredientes de alta digestibilidade, fibras alimentares e prebioticos, Enriquecido com vitaminas e minerais que proporcional maior saúde e vitalidade"}' -H "Content-Type: application/json" -X POST http://localhost:5000/api/predict
```
Expected response:
```json
{
  "prediction": {
    "category": "Cachorro, Rações, Ração Seca"
  }
}
```

## Access Jupyter notebook
```
docker run -it -v $PWD:/opt/nb -p 8888:8888 felixleung/auto-sklearn \
/bin/bash -c "mkdir -p /opt/nb && jupyter notebook --notebook-dir=/opt/nb --ip='0.0.0.0' --port=8888 --no-browser --allow-root"
```

## Datasets
- A public dataset of `1980 products` with `88 categories` extracted from `Petlove`, each product has `name`, `description` and `category` - https://s3.amazonaws.com/product-categorization/dataset.csv
