Hello!

This is a little Django user management system. It does everything that was asked in the task description and maybe even more (although no auth).

I created an additional population script (population_script.py) to create an example set.

I used the Django REST framework toolkit for this task. I tried to use as little of it as possible to make it as native Django as possible. I think I did  good job in that as in I used it mainly for displaying purposes. As such, the UI used comes from the framework. I focused mainly on the practicality and the logic behind this exercise.

 In my opinion it works great. If you have any questions then let me know!

 May the Force be with you.

`python manage.py makemigrations clients`
`python manage.py migrate`
`python manage.py runserver`
`python population_script.py`

127.0.0.1:8000/clients/ for clients
127.0.0.1:8000/workout_plans/ for workout plans

I did not create additional views for exercises or their plans as the displaying of the data was not my focus. 
