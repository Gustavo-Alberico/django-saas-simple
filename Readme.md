# Django SaaS - Simple

This project aims to create a boilerplate for Django SaaS applications. It is focused on simple projects that use a single database with a shared schema.

## Setup project
```
cookiecutter https://github.com/Gustavo-Alberico/django-saas-simple.git
```

## After cookiecutter

### Run migrations
The first thing you need to do is run the migrations for the tenant and user tables.
```Python
python manage.py migrate
```


### Run initial configs script

After running migrations in your database, you need to create an initial tenant and an admin user; the environment variables can be found in the .env file

```python
python script/initial_configs.py
```


### vscode config

.vscode/settings.json

```json
{
    "[python]": {
        "editor.defaultFormatter": "ms-python.black-formatter",
        "editor.formatOnSave": true
    },
    "files.associations": {
        "**/templates/**/*.html": "django-html"
    },
    "emmet.includeLanguages": {
        "django-html": "html"
    }
}
```
