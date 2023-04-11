## Create yaml file based on changes made to yaml_env.txt
## Creates yaml in outer directory and another copy within the repo for version control

import os


def main():
	#read yaml template
	with open('yaml_template.txt') as f:
		yaml_string = f.read()
	
	with open('yaml_env.txt') as f:
		variables = f.read()
		
	#make variables callable from env.txt
	variables_list = variables.split('\n')
	var_dict = {var.split('=')[0]:var.split('=')[1] for var in variables_list}
	
	yaml_string = yaml_string.format(PROJECT_ID=var_dict['PROJECT_ID'],
                                 IMAGE=var_dict['IMAGE'],
                                 path_to_Dockerfile=var_dict['path_to_Dockerfile'],
                                REGION=var_dict['REGION'],
                                SERVICE_NAME=var_dict['SERVICE_NAME'])
	#write yaml for deployment
	with open('../cloudbuild.yaml','w') as f:
		f.write(yaml_string)
	#write yaml to save in repo
	image = var_dict['IMAGE']
	with open(f'cloudbuild.yaml_{image}','w') as f:
		f.write(yaml_string)

	return


if __name__ == '__main__': 
	main()
