# Dockerized Shiny App

To build a docker image execute following command:

```bash
docker build -t dockerizedshinyapp .
```

Then, to run a container by executing:

```bash
docker run -d -p 80:80 dockerizedshinyapp
```