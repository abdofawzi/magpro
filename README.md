# MagPro
MagPro is project management web app based on [DJango framework](https://www.djangoproject.com/) can help you to manage:
* **Projects**
* **Tasks**
* **Users**
* **Wiki**

## Installation
* **required DJango 1.11:**  Follow [Django Quick install guide](https://docs.djangoproject.com/en/1.11/intro/install/)
* **Install Required Packages:** You can find required packages in `requirements.txt`
* **Optional** Run `create_permissions_groups.py` script to create all group of permissions you could use
```
python create_permissions_groups.py
```

## Edit .gitignore
* remove sqlite from gitignore file to commit DB 
```
db.sqlite3
```
* remove migrations from gitignore file to commit migrations files
```
*/migrations/*
```

