Hello!

This is a little Django user management system.  

The purpose of this assignment was to create a system (REST API), where you can create and edit users, exercises, daily plans and workout plans.  

A plan has a name and consists of several (workout) days.  
A day can have multiple exercises that you should perform that day.  
A plan can be assigned to one or more user(s).  
Whenever a user is assigned to a workout plan, he(she) should receive an email confirmation.  
Whenever a plan is modified, the user(s) connected should be notified of the change by mail.  

  
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
