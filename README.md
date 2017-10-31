# moviecollection
Sample movie collection application to store title, length, storyline, imdb rating and trailer url etc. developed using python and django

## How to run the application
```
Clone the Project
Navigate to moviecollection folder
Run python manage.py makemigrations
Run python manage.py migrate
Run python manage.py runserver
```

## Technologies used
```
Python 2.7
Django 1.9.1
SQLite3
Jquery
Bootstrap
Django forms
```

## Testing
```
Home page will display 8 movies with thumbnails and movie name
When user click on thumbnail a modal popup will be appeared with the available data in the database
Pagination will be available at bottom to load next 8 movies
In admin page table with 8 movies and pagination will be appeared
On top of the table add movie button will be available to add a new movie information
This Add Movie button will open a form to fill the complate information and on click of submit the data will be stored
If user click on any of the movie from the table that will open a form to edit the data related to movie
There will be a button available to delete movie information from database
```