
# LogB

LogB is a blogging website.

## 👇 Prerequisites

Before installation, please make sure you have already installed the following tools:

- [Git](https://git-scm.com/downloads)
- [Python](https://www.python.org/downloads/release/python-3916/)

## 🛠️Installation

1. Clone Logb

  ```bash
    git clone https://github.com/OmAvhad/LogB
  ```
    
2. Move into the project
  ```bash
    cd my-project/
  ```

3. Create environment and activate it.
  ```bash
    # install environment package
    pip install virtualenv

    # create environment
    virtualenv virtualenv_name

    # activate virtual environment
    # Windows
    venv\Scripts\activate
    # Linux
    source venv/bin/activate
    # Mac os
    source venv/bin/activate
  ```

4. Install packages.
  ```bash
  pip install requirements.txt
  ```

5. To connect to PostgresSQL database create .env file inside project directory and add the below variables in it.
  ```python
  DB_NAME= db_name
  DB_USER= db_username
  DB_PASSWORD= db_password
  DB_HOST= db_host
  DB_PORT= db_port
  ```

6. Run Django app.
  ```bash
  # runserver
  python manage.py runserver
  ```

7. Apply database migrations
  ```bash
  # migrate changes
  python manage.py makemigrations
  python manage.py migrate
  ```