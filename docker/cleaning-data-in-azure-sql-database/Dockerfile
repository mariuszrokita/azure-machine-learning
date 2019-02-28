FROM python:3.6

# Prerequisites for Python ODBC library and installs necessary locales
RUN apt-get update && apt-get install -y unixodbc unixodbc-dev apt-transport-https locales \
    && echo "en_US.UTF-8 UTF-8" > /etc/locale.gen \
    && locale-gen \
	&& rm -rf /var/lib/apt/lists/* #reduce image size by removing obsolete package cache

# Install ODBC support for MS SQL Server
# (more info: https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-2017)
RUN curl --silent https://packages.microsoft.com/keys/microsoft.asc | apt-key add -; \
	curl --silent https://packages.microsoft.com/config/debian/9/prod.list > /etc/apt/sources.list.d/mssql-release.list; \
    apt-get update && ACCEPT_EULA=Y apt-get install msodbcsql17


COPY . /app
WORKDIR /app

# Install Python requirements
RUN pip install -r requirements.txt

EXPOSE 1433
CMD ["python", "./data_cleaning.py"]