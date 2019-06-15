FROM python:3.6-slim

RUN apt-get clean \
    && apt-get -y update

RUN apt-get -y install nginx \
    && apt-get -y install python3-dev \
    && apt-get -y install build-essential

# install requirements
COPY requirements.txt /
RUN pip install -r requirements.txt

# copy application files
COPY app /flaskapp/app
COPY .   /flaskapp

# set working directory
WORKDIR /flaskapp

# inform about ports used by apps and services
EXPOSE 80

# execute startup script
COPY nginx.conf /etc/nginx
RUN chmod +x ./launcher.sh
CMD ["./launcher.sh"]