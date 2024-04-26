# Working with Django Models
Demo code for the course "Working with Django Models" on [Pluralsight](https://www.pluralsight.com).

There's a commit for each module in the course, as well as a tag:


- [Project Start - Module 3:Model Classes and Instances](https://github.com/codesensei-courses/django-models/releases/tag/m3-model-classes)
- [Starting Module 4: Django Module Fields](https://github.com/codesensei-courses/django-models/releases/tag/m4-model-fields)
- [Starting Module 5: Managers and QuerySets](https://github.com/codesensei-courses/django-models/releases/tag/m5-managers-querysets)
- [Starting Module 6: Customizing Model Behaviour](https://github.com/codesensei-courses/django-models/releases/tag/m6-customizing-models)
- [Starting Module 7: Migrations](https://github.com/codesensei-courses/django-models/releases/tag/m7-migrations)
- [Starting Module 8: Optimizing Your Code](https://github.com/codesensei-courses/django-models/releases/tag/m8-optimizing)
- [After Module 8](https://github.com/codesensei-courses/django-models/releases/tag/end-of-course)
# Setup instructions

## 1. Clone this repository

Check out any specific commit you like.

## 2. Create and activate a virtual environment

How to do this depends on your system; depending on your IDE this may not be necessary.

If you don't know how to do this: see my course [Development Environments and Package Management in Python 3](https://www.pluralsight.com/courses/python-3-development-environments-package-management)

## 3. Install dependencies

Inside the project, run `python -m pip install -r requirements.txt`.

## 4. Move into the `carved_rock` folder

You want to be in the folder where the file `manage.py` is.

To get there, You probably need to run `cd carved_rock`.

But watch out: there are two of those and you want to be in the
*outer* carved_rock folder. If you end up 1 level too deep, run
`cd ..` to move up 1 level.

## 5. Run the project

The command for this is `python manage.py runserver`.

You can now view the project at http://localhost:8000

If this does not work, you are probably not in the correct folder.

# 6. Admin password

Setup your admin login using the command `python manage.py createsuperuser`.

