from python:3.8-alpine

ADD . /code

RUN pip install -r /code/requirements.txt

ENTRYPOINT [ "python", "./code/dahua_camera_backup_manager.py" ]