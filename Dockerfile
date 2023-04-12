FROM continuumio/anaconda3

#Install requirements directly in Dockerfile
#All env varialbes should be installed directly in Dockerfile.
#NO API Keys should be listed.
ENV PROJECT_ID aml-proejct-hrdc
ENV LOCATION us-central1 

# pip install including flask app requirements
RUN pip install --ignore-installed --force \
    Flask==2.0.1 \
	gcsfs \
    google-cloud-aiplatform \
    google-cloud-datalabeling \
    google-cloud-secret-manager \
    google-cloud-storage \ 
    gunicorn==20.1.0 \
    jsonlines \
    py-log \
    response \
    Werkzeug  
	

## set APP_HOME variable as path: /app
ENV APP_HOME /app
# set working directory to APP_HOME
WORKDIR $APP_HOME
# Copy everything from the build context into the app directory
COPY . ./
# Change the workdir to the project directory - need to specify directory
WORKDIR /app/deploy_to_api_on_gcp

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
# Timeout is set to 0 to disable the timeouts of the workers to allow Cloud Run to handle instance scaling.
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app