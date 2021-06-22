
from flask import Flask, url_for, jsonify , request,json
import numpy as np
import pickle
import pandas as pd
import csv
import os
from sklearn.preprocessing import StandardScaler
from flask import abort
import uuid

from flask import Response




# random
#import linecache
#from model import model as sentiment
from app_key import require_appkey


import sys
if sys.version_info.major < 3:
    reload(sys)




app = Flask(__name__)
csv.field_size_limit(sys.maxsize)


#@app.before_first_request

@app.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Access-Control-Allow-Headers, Origin, X-Requested-With, Content-Type, Accept, Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS, HEAD'
    response.headers['Access-Control-Expose-Headers'] = '*'
    return response


@app.route('/apiTest',methods=['get','post'])
#@require_appkey
def api_core():
  try:
    tab=request.json['tab']
    c = pd.read_csv('foo.csv', index_col=0, encoding = "ISO-8859-1")
    filename = 'model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    a = np.vstack([c, tab])

    resultat=loaded_model.predict(a).tolist()
    data={
      'resultat' : resultat 
    }
    return jsonify (data)
  except:
 
   return jsonify ({'msg':'erreur'})


@app.route('/')
def api():
  response_object = {'status': 'success'}
 
 
  
   

  return jsonify(response_object)






if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port='4000')