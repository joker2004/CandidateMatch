from flask import Flask, jsonify;
from flask_cors import CORS;
# from flask_restful import Resource, Api;


app = Flask(__name__)
# api=Api(app)
CORS(app)


import urllib.request, json
candidate_url="http://private-76432-jobadder1.apiary-mock.com/candidates"
job_url="http://private-76432-jobadder1.apiary-mock.com/jobs"
response_candidate = urllib.request.urlopen(candidate_url)
response_job= urllib.request.urlopen(job_url)

candidate_data = json.loads(response_candidate.read())
dict_list=[]

#print(json.dumps(candidate_data, indent = 4, sort_keys=True))
#print("**** CANDIDATE DATA END ****")
job_data = json.loads(response_job.read())
#print(json.dumps(job_data, indent = 4, sort_keys=True))
#print("**** JOB DATA END ****")

#print("MATCHED JOB CANDIATES")
for jobs in job_data:
    counter_list=[]
    detail_counter_list=[]
    job_list=jobs["skills"].split(',')
    job_title=jobs["name"]
    company=jobs["company"].split(',')
    for candidates in candidate_data:
        name=candidates["name"]
        skill_list=candidates["skillTags"].split(',')
        counter=0
        for skill in skill_list:
            if(skill in job_list):
                counter+=1
        counter_list.append(counter)
        detail_counter_list.append([name,job_title,company[0]])
    sorted_counter_list=sorted(counter_list)
    first_qualified=sorted_counter_list[-1]
    #print(first_qualified)
    second_qualified=sorted_counter_list[-2]
    index_first=counter_list.index(first_qualified)
    index_second=counter_list.index(second_qualified)
    #print(dict())
    diction=dict()
    diction["Name"]=detail_counter_list[index_first][0]
    diction["Job Description"]=detail_counter_list[index_first][1]
    diction["Company"]=detail_counter_list[index_first][2]
    diction2=dict()
    diction["Name"]=detail_counter_list[index_second][0]
    diction["Job Description"]=detail_counter_list[index_second][1]
    diction["Company"]=detail_counter_list[index_second][2]

    #print(diction)
    if(bool(diction)):
        dict_list.append(diction)
    if(bool(diction2)):
        dict_list.append(diction2)

#print(dict_list)
#print(sorted_counter_list)
#print(detail_counter_list)
#print(diction)


job_data = {
    "data":dict_list

}


@app.route("/", methods=['GET'])
def index():
    return "Welcome Please proceed to http://localhost:4200/";

@app.route("/jobData/", methods = ['GET'])
def jobData():
    global job_data
    return jsonify([job_data])

if __name__ == '__main__':
    app.run(debug=True)
