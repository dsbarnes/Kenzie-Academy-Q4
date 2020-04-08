# Django, Hierarchical Data and Me. 

Djando Hierarchical Data and Me is a Django app to demonstrate and learn about trees.

## Requirements
Python 3  
Something to manage virtual environments, preferably, poetry. 

## Installation

Clone this github repo.  
Change directories into the new directory that was created by cloning this repo  
Run `poetry shell` followed by `poetry install`  

If you prefer to manage virtual environments with something other than poetry,  
please refer to the necessary documentation concerning package management and installation.

## Usage

After the repo is cloned and you are in a virtual environment run the following commands:

```python
python manage.py runserver
```

Open a browser and navigate to `localhost:8000` to see a visual representation of the data in the tree.  

If the page is empty of content run
```python
python manage.py makemigrations dropbox
python manage.py migrate
```
from the root directory of the cloned repo.
  
We can also navigate to `localhost:8000/admin`  
To log in use the username: derek, password: root, alternatively run

```python
python manage.py createsuperuser
```

Fill the form out accordingly.  

Once logged in, click on the File_Objects link
The user should see a drag and drop section to make and arrange 'folder' and 'files'

## License
Forward all requests about Licensing to Kenzie Academy
