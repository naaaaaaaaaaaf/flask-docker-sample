FROM python:3.8.5

ARG project_directory
WORKDIR $project_directory
ADD src/requirements.txt $project_directory
RUN pip install -r requirements.txt