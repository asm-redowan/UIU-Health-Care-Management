FROM python:3.11.9-alpine
COPY . .
RUN pip install --upgrade pip 
RUN pip install -r requriment.txt

RUN python manage.py migrate

EXPOSE 8000
CMD ["python","manage.py","runserver","0.0.0.0:8000"]