# Use latest python image
FROM python:latest 

# Set "app" to be the directory where all the following instructions will be executed
WORKDIR /app

# Copy local file "requirements.txt" into "app"
COPY ./requirements.txt /app

# Run an instruction to install all requirements in "requirements.txt"
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy all local file into "app"
COPY . /app

# for local usage
# ENV PORT=8000
# EXPOSE 8000
# CMD ["python3", "manage.py","runserver", "0.0.0.0:8000"]

CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT