# IMPORT PYTHON 3.6
FROM python:3.6-alpine3.10

# EXPOSE PORT 8000 FOR APPLICATION
EXPOSE 8000

# CREATE DIRECTORY FOR APPLICATION
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# COPY DEPENDENCIES FILE
COPY requirements.txt .

# INSTALL DEPENDENCIES
RUN pip install -r requirements.txt

# COPY ALL FILES
# COPY . .

RUN python3 manage.py collectstatic
RUN python3 manage.py migrate

CMD ["gunicorn", "--chdir", "superlists", "--bind", ":8000", "superlists.wsgi:application"]
