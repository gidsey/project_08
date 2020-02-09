# Treehouse Python Techdegree: Project 08

## Mineral Catalog

### Description
Filtering and Searching the Mineral Catalog

Minerals can be filtered by:
* First letter of the mineral name
* Group
* Streak

In addition a full-text search will search across all fields in the database.
 
### Information 
Package requirements for the project are outlined in the 'requirements.txt' file.'

On first run, the database will need to be populated from the 'minerals.json' file.
Follow the link on the homepage to /import to run the script that will populate the database.

## Running Locally

```bash
git clone https://github.com/gidsey/project_08.git
```

```bash
pip install -r requirements.txt
```
  
```bash
 python manage.py migrate
```

```bash
 python manage.py runserver
```

The site will be visible at http://127.0.0.1:8000/
The admin site will be at: http://127.0.0.1:8000/admin


## Tests
The project includes unit tests which cover:
* Mineral model
* List view
* Group view
* Streak view
* Search view
* Data import


## Future Development Tasks
* Upgrade to Django 3.0.3
* Add Django Rest Framework (DRF)
* Create APIs


## Attributions

Project built by [Chris Guy](https://www.linkedin.com/in/gidsey/), October 2019


