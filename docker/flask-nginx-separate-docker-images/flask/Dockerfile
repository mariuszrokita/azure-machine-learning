FROM ubuntu:latest

RUN apt-get update -y && \  
    apt-get install -y python3-pip python3-dev

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app 
ADD . /app

# Install the dependencies
RUN pip3 install -r requirements.txt

# run the command to start uWSGI
CMD ["uwsgi", "app.ini"]