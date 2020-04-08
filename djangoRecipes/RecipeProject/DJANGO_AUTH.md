# Django Authentication

Django come with it's own auth sysyem - yay battries included!  
See the 'User authentication in Django' documentation.  

<hr />
We will need to open the developer tools, and use the Application tab. We are looking for cookies.  
For auth, the CSRF token isn't really important. That's for handling form stuff.  

First, we can look at `urls.py`  
And, the LOGIN_URL in `settings.py`  
For the purposes of this assignment, we can leave the LOGOUT_REDIREC_URL as `'/'`  
In views, we will use a `@login_required()` decorator. from `django.contrib.auth.decorators`  

With our login function (still in `views.py`) we take in the request, as always,  
we will want to use Model.object.create_user() and pass it to our login function.  

if we do have access to a user, we should consider `authenticate()` 
if we do know the user, we can use `login()` (For creating a new user, the data isn't stored, so we can't auth)  





