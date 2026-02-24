# Flask Framework - Summary Notes
## Integrating HTML with Python

---

## 1. WSGI (Web Server Gateway Interface)
- WSGI is a specification that describes how a web server communicates with web applications
- It acts as an interface between the web server and the Flask application
- Flask is a WSGI framework that handles the communication between server and app

**Example:**
```
python
app = Flask(__name__)  # Creates WSGI application instance
```

---

## 2. Flask Application Setup
- `Flask(__name__)` creates an instance of the Flask class
- This instance is your WSGI application
- `__name__` helps Flask locate templates and static files

**Basic Setup:**
```
python
from flask import Flask
app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)
```

---

## 3. Routing in Flask
- Routes define URL paths and their corresponding view functions
- Use the `@app.route()` decorator to define routes
- Routes can handle different HTTP methods (GET, POST, etc.)

**Examples:**
```
python
@app.route("/")              # Root URL
@app.route("/index")         # /index URL
@app.route("/about")         # /about URL

def welcome():
    return "Hello World"
```

---

## 4. Rendering HTML Templates
- `render_template()` function renders HTML files from the templates folder
- Templates must be placed in a folder named "templates" (mandatory)
- Wrong file name results in: `jinja2.exceptions.TemplateNotFound`

**Syntax:**
```
python
from flask import render_template

@app.route("/")
def welcome():
    return render_template('index1.html')
```

**Template Folder Structure:**
```
FlaskFrameWork/
├── app.py              # Main Flask application
├── templates/          # MANDATORY folder name
│   ├── index1.html
│   ├── about.html
│   └── other.html
```

---

## 5. Jinja2 Template Engine
- Jinja2 is Flask's built-in template engine
- Combines HTML templates with dynamic data sources:
  - SQL databases
  - CSV files
  - MongoDB
  - Machine Learning models
  - APIs

**Key Features:**
- `{{ variable }}` - Output variables
- `{% for %}` - Loops
- `{% if %}` - Conditionals
- `{% include %}` - Include other templates
- `{% extends %}` - Template inheritance

**Example with Variables:**
```
html
<h1>Welcome, {{ name }}</h1>
{% for item in items %}
    <li>{{ item }}</li>
{% endfor %}
```

---

## 6. Debug Mode
- `debug=True` enables automatic reloading on code changes
- Shows detailed error pages when exceptions occur
- Should be False in production

```
python
if __name__ == "__main__":
    app.run(debug=True)
```

---

## 7. Returning Different Response Types

**Plain String Response:**
```
python
@app.route("/index")
def index():
    return "Welcome to the index page"
```

**HTML Template Response:**
```
python
@app.route("/about")
def about():
    return render_template('about.html')
```

**JSON Response (API):**
```
python
from flask import jsonify

@app.route("/api/data")
def get_data():
    return jsonify({'key': 'value'})
```

---

## 8. Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| jinja2.exceptions.TemplateNotFound | Wrong template filename or missing templates folder | Ensure templates folder is named exactly "templates" and filename matches exactly |
| ImportError: No module named 'flask' | Flask not installed | Run `pip install flask` |
| Port already in use | Default port 5000 is in use | Change port with `app.run(port=5001)` |

---

## 9. Complete Example Code
```
python
from flask import Flask, render_template

'''
It creates an instance of the flask class 
which will be your WSGI(web server gateway interface) application 
'''

## WSGI Application 
app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template('index1.html')   ## wrong file name will give you a jinja2.exception.templatesnotfound

@app.route("/index")
def index():
    return "Welcome to the index page"

@app.route('/about')
def about():
    return render_template('about.html')  ## eg 

if __name__=="__main__":
    app.run(debug=True) 
```

---

## Key Points to Remember

1. **WSGI** - Web Server Gateway Interface, helps communicate between web server and Flask app
2. **Jinja2** - Template engine that combines HTML with dynamic data (SQL, CSV, DB, ML models, MongoDB)
3. **Templates Folder** - Must be named exactly "templates" (case-sensitive)
4. **render_template()** - Used to render HTML files from templates folder
5. **debug=True** - Auto-reloads server on code changes (use only in development)
6. **@app.route()** - Decorator to define URL paths and their handlers

---

*These notes cover the fundamentals of integrating HTML with Python using Flask framework.*

---

## 10. How to Run and View

### Step 1: Install Flask (if not installed)
```bash
pip install flask
```

### Step 2: Run the Flask Application
```bash
python main.py
# OR
python app.py
```

You should see output like:
```
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
 * Restarting with reloader...
```

### Step 3: View in Browser
Open your web browser and navigate to:
- `http://127.0.0.1:5000/` - Shows index1.html (welcome page)
- `http://127.0.0.1:5000/index` - Shows "Welcome to the index page"
- `http://127.0.0.1:5000/about` - Shows about.html

### Alternative Methods:
- Use `http://localhost:5000/` instead of 127.0.0.
- Change port: `app.run(port=8080)` for different port

---

## Quick Reference Commands

| Command | Description |
|---------|-------------|
| `pip install flask` | Install Flask |
| `python app.py` | Run Flask app |
| `Ctrl+C` | Stop server |
| debug=True | Auto-reload on changes |

---
