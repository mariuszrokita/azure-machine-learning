uid = 'www-data'
gid = 'www-data'
workers = 5
threads = 2
bind = 'unix:/tmp/uwsgi.socket'
worker_class = 'sync'