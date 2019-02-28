# Brief code description

The code presents an example of dockerized python code that loads data from Azure SQL database into Pandas data frame, performs some calculations (i.e. data cleaning, feature engineering) and saves changes back in the database.

The main challenge was to establish a connection to the Azure SQL database from the docker container, which was not possible due to the following error:

```bash
(pyodbc.Error) ('01000', "[01000] [unixODBC][Driver Manager]Can't open lib 'ODBC Driver 13 for SQL Server'
```

Luckily, the problem has been overcome by changing Dockerfile - by installing additional prerequisites for Python ODBC library and installing ODBC support for MS SQL Server.