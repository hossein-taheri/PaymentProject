broker_url = 'redis://127.0.0.1:6379'
result_backend = 'mongodb://127.0.0.1:27017'

include = ['ZibalEntrance.tasks']

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'Asia/Tehran'
enable_utc = True
