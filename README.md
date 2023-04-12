# Tutorial on Deploying a Model on GCP Cloud Run

This tutorial is based on the sklearns Iris Dataset and assumes that you have trained a model and stored said model as a pickle file. This tutorial also assumes that you are working from a Vertex AI environment and have a basic understanding of Docker. For reference this has been done in the `dev.ipynb` file. Once you're model has been stored, complete the following steps: 

1. Script your predict functionalities in `model.py`
2. Create Dockerfile
    - Debug Dockerfile in terminal 
3. Create `cloudbuild.yaml` file. 
    - First edit the detials in the `yaml_env.txt`
    - Then in your terminal, run `python create_yaml.py`
    - This script will create a yaml file in your home directory which will be used and a copy within your repository to be referenced as needed.
4. Be sure that your could build service account has the Cloud Run Admin and Service Account User Permissions in your IAM control panel.
5. In the terminal, at the main directory, run  `gcloud builds submit`
    - This will deploy the model to Cloud Run
6. Once your model has been deployed, try calling the API and debug as necessary. The API URL can be found on the Cloud Run UI once you click on your service name. Permissions will need changing to allow for speicific service accounts to hit the API. This can also be configured within the Cloud Run UI or in the IAM Permissions.

## Helpful Terms: 
- yaml file: instructions that cloud run uses to execute commands for deployment. Must be named `cloudbuild.yaml`
- IAM Permssions: IAM controls are how GCP gives permissions to service accounts and users within your GCP project.


## Helpful links:
https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service
https://cloud.google.com/run/docs/deploying