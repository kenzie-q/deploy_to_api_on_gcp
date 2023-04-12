#standard imports
import logging, os, sys
from datetime import datetime
import numpy as np
#additional libraries
from flask import Flask
from flask import jsonify
from flask import request

import model

app = Flask(__name__)

@app.route("/",  methods=['GET', 'POST'])
 # This route is for sending a single piece of text for prediction
 # This route will return a prediction response
 # The request needs to be of type application/json and it requires a json payload in the format
#'''
#{'content':"whatever string you want to predict"}

def main():
   #logger, fileHandler = py_log.start_logger()
	try:
		json_content = request.get_json()
		logging.info("Received text to predict: "+str(json_content['content']))
		if json_content['mode']=='batch':
			arr = np.array(json_content['content'])
		elif json_content['mode'] == 'live':
			arr = np.array(json_content['content']).reshape(1,-1)
		response = model.predict_json(arr)
		logging.info('Received Response from model')
		result = 'success'
		
	except: 
		logging.exception('')
		response = 'failure'
	return jsonify(response)


if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

