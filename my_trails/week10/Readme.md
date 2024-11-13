# Notes how to use django
# the folder structure
In Django, you should store your HTML template files and static files (such as CSS, JavaScript, and images) in separate directories to maintain a clear structure in your project.

1. **Templates**: HTML files should be stored in a `templates` directory. This is where you put your Django template files, which can contain dynamic content using Django's template language.

2. **Static Files**: CSS, JavaScript, and image files should be placed in a `static` directory. Each app can have its own static directory, and you can organize files within that directory as needed.

The `{% static %}` template tag is used to reference these static files in your template. It generates the proper URL for the static file based on the settings in your Django project.

So, to clarify, you should not put your CSS or JavaScript files in the `templates` directory. Instead, they should go in the `static` directory. Your HTML templates in the `templates` directory will reference these static files using the `{% static %}` tag. This separation keeps your project organized and helps Django serve the files efficiently.


## where do the static folder has to placed

In Django, you typically place the `static` directory inside each individual app. This way, you can manage static files specific to that app in an organized manner. However, you can also create a global static directory at the project level if you have common static files shared across multiple apps.

Here’s a common structure:

### Project-Level Structure

```
myproject/
│
├── myapp1/
│   ├── static/
│   │   └── myapp1/
│   │       ├── css/
│   │       │   └── style.css
│   │       └── js/
│   │           └── script.js
│   ├── templates/
│   │   └── myapp1/
│   │       └── base.html
│   └── views.py
│
├── myapp2/
│   ├── static/
│   │   └── myapp2/
│   │       ├── css/
│   │       │   └── other_style.css
│   │       └── img/
│   │           └── image.png
│   ├── templates/
│   │   └── myapp2/
│   │       └── other_base.html
│   └── views.py
│
├── static/  # Optional for global/static files shared across apps
│   ├── css/
│   └── js/
│
└── manage.py
```

### Key Points:
- **App-Level Static Directories**: Each app has its own `static` directory where you can keep app-specific static files. The convention is to create a subdirectory named after the app inside the `static` directory to avoid name clashes.
  
- **Global Static Directory**: If you have static files that are shared across multiple apps, you can create a `static` directory at the project level. You will need to configure Django's `STATICFILES_DIRS` setting to include this directory.

### Configuration in `settings.py`:
Make sure to include the appropriate settings in your `settings.py` file:

```python
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_URL = '/static/'

# Include any global static directories
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  # Project-level static directory
]
```

Using this structure will help Django find and serve your static files correctly.

