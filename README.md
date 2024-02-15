# Wallet api

Simple wallet api django app

## Development

### Make sure to have the following on your host:

- [Python 3.10](https://www.python.org/downloads/)
- [MySQL 8.0](https://www.mysql.com/downloads/)


### Clone the repo

```bash
git clone git@github.com:aatrubilin/wallet-api.git
```

### Go to project path

```bash
cd wallet-api
```

### Virtualenv (optionally)

Poetry can work with an existing virtualenv (and can also be installed directly in a virtual env)
More information: https://poetry.eustace.io/docs/basic-usage/#poetry-and-virtualenvs

```shell
python3.10 -m venv .venv
. .venv/bin/activate
```

### Install Poetry (optionally)

https://python-poetry.org/docs/

Install poetry

```shell
pipx install poetry
```

### Install dependencies

```shell
poetry install
```

### Install pre-commit hooks

https://pre-commit.com/

```shell
pre-commit install
```

Run against all the files (optionally).

_It's usually a good idea to run the hooks against all of the files when adding new hooks._

```shell
pre-commit run --all-files
```

### Setup MySQL DB


```mysql
CREATE DATABASE wallet CHARACTER SET utf8;
CREATE USER 'wallet'@'%' IDENTIFIED BY 'wallet';
GRANT ALL ON wallet.* TO 'wallet'@'%';
```

### Setup config

```shell
touch .env
echo 'DATABASE_URL=mysql://wallet:wallet@127.0.0.1:3306/wallet' >> .env
echo 'DATABASE_ECHO=True' >> .env
```

### Run migrations

```shell
python manage.py migrate
```

### Run server

```shell
python manage.py runserver
```

Boom! :fire: It's done! Go to `http://localhost:8000/api/`

## Running the tests

```shell
pytest
```

## Built With

* [Django](https://www.djangoproject.com/) - High-level Python web framework
* [Django REST framework](https://www.django-rest-framework.org/) - Powerful and flexible toolkit for building Web APIs
* [Django REST framework JSON:API](https://django-rest-framework-json-api.readthedocs.io/) - JSON:API support for Django REST framework
* [MySQL](https://www.mysql.com/) - Relational Database

## Authors

* **Alexandr Trubilin** - [AATrubilin](https://github.com/aatrubilin)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
