# bind = "127.0.0.1:8000"                   # Don't use port 80 becaue nginx occupied it already. 
errorlog = './logs/gunicorn-error.log'  # Make sure you have the log folder create
accesslog = './logs/gunicorn-access.log'
logconfig='./logging.ini'
loglevel = 'debug'
workers = 4
# statsd_host='172.20.0.4:9125'
# statsd_prefix='tasks'
