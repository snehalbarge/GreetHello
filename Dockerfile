FROM python:latest

 

# set the working directory in the container to /app
ADD . /app
WORKDIR /app

 

# add the current directory to the container as /app


 

# install all the requirements
RUN pip install --trusted-host pypi.python.org -r requirements.txt

 


EXPOSE 8000

 

# execute the Flask app
CMD ["python3", "manage.py","runserver","0.0.0.0:8000"]