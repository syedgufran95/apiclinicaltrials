from flask import Flask
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
from mymodule import *
from flask_restful import Resource, Api
import xml.etree.ElementTree as ET 
import csv
import json
import glob
import os

app=Flask(__name__)


@app.route("/")
def combine():
		r=initial()
		return r




UPLOAD_FOLDER="upload"
ALLOWED_EXTENSIONS={'xml'}
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS		

@app.route("/upload",methods=['POST'])
def upload1():
	if 'file' not in request.files:
		resp=jsonify({'message':"file not in the request"})
		resp.status_code=400
		return resp
	file=request.files['file']
	if file.filename=='':
		resp=jsonify({'message':"no file selected for upload"})
		resp.status_code=400
		return resp
	if file and allowed_file(file.filename):
		filename=secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
		resp=jsonify({'message':"file successfully uploaded"})
		resp.status_code=201
		return resp
	else:
		resp=jsonify({'message':'allowed file is xml'})
		resp.status_code=400
		return resp
@app.route("/append")
def append1():
	data_folder="upload"
	testdata = open('combined2.csv', 'a')
	csvwriter = csv.writer(testdata)
	obj=clinical()
	for filename in glob.iglob(data_folder+"/*.xml"):
		tree = ET.parse(filename)
		root = tree.getroot()
		t=[]
		
		nct=obj.find_nctid(root)
		if(find1(nct)!=True):
			t.append(obj.find_nctid(root))
			t.append(obj.get_status(root))
			t.append(obj.start_date(root))
			t.append(obj.completion_date(root))
			t.append(obj.condition(root))
			t.append(obj.studydesign(root))
			t.append(obj.eligibility(root))
			t.append(obj.has_expanded_access(root))
			t.append(obj.enrollment(root))	
			csvwriter.writerow(t)
			s="success"
			return s

		else:
			s="Already Present"
			return s

@app.route('/parse')
def parse1():
	with open('combined2.csv',encoding='utf-8') as csvf:
		csvreader=csv.DictReader(csvf)
		count=0
		for index,row in enumerate(csvreader):
			count=count+1
			id1=row["nct_id"]
			if(index==0):
				data={}
				data[id1]={}
			data[id1]={"overall_status":row['overall_status'],
			"start_date":row['start_date'],"completion_date":row['completion_date'],
			"condition":row['condition'],"Study design info":row['Study design info'],
			"eligibility":row['eligibility'],"has_expanded_access":row['has_expanded_access']
			,"enrollment":row['enrollment']}
	
	return data



def find1(nct_idu):
		s="not found"
		with open('combined2.csv',encoding='utf-8') as csvf:
			csvreader=csv.DictReader(csvf)
			for index,row in enumerate(csvreader):
				if row["nct_id"]==nct_idu:
					id1=row["nct_id"]
					s="found"
					data={}
					data[id1]={}
					data[id1]={"overall_status":row['overall_status'],
					"start_date":row['start_date'],"completion_date":row['completion_date'],
					"condition":row['condition'],"Study design info":row['Study design info'],
					"eligibility":row['eligibility'],"has_expanded_access":row['has_expanded_access']
					,"enrollment":row['enrollment']}
					return True
					
			return False
	

if __name__=="__main__":
	app.run(debug=True)
