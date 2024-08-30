# cat-downloader
django + celery + redis
## build and run
<code>docker compose up</code>
## localhost:8000/
download random cat (for many cats just relaod page)
## localhost:5555/
flower - monitoring celery workers and tasks
## localhost:8000/admin
to add schedule (by default = download 1 cat every 1 minute)
