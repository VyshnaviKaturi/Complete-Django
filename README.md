🛠️ Project Setup & Architecture
This section documents the standard workflow for initializing a Django project and connecting an application.
1. Environment Initialization
First, isolate the project dependencies to avoid conflicts with other Python projects.
# Create the virtual environment
python -m venv venv

# Activate it (Windows)
.\venv\Scripts\activate

# Activate it (Mac/Linux)
source venv/bin/activate

2. Project & App Creation
Django follows a "Project-contains-Apps" structure.
# Install Django
pip install django

# Create the main project configuration
django-admin startproject my_project .

# Create a functional unit (app)
python manage.py startapp my_app

3. Application Registration
To make the project aware of the new app, it must be registered in the configuration core.

File: my_project/settings.py

Action: Add the app name to the INSTALLED_APPS list.
INSTALLED_APPS = [
    ...,
    'my_app', 
]
4. The Request-Response Cycle (Views & URLs)
To render a page, we connect a logic function (View) to a web address (URL).

Create a View: In my_app/views.py, define a function that returns an HttpResponse.

Map the URL: In my_project/urls.py, import your view and add it to the urlpatterns list.
# Example URL Mapping
from my_app import views

urlpatterns = [
    path('hello/', views.hello_world),
]
