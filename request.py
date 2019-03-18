import requests   
import json 

ifCache = True # False

def request_url(url):
    request = requests.get(url)
    response = request.json()
    return (response)

def open_json_file(file_name, data):
    with open("file_name", "w") as file_hender:
        file_hender.write(data)

def read_json_file(file_name):
    read_file = open("file_name","r") 
    str_file = read_file.read()
    return str_file

base_url = "http://saral.navgurukul.org/api/courses" 
call_api = request_url(base_url)
print (call_api)
data = json.dumps(call_api) 

open_json_file("course.json", data)
str_file = read_json_file("course.json")
dict_file = json.loads(str_file)
count = 0
num = 1
while count < len(dict_file["availableCourses"]):
    print (num,dict_file["availableCourses"][count]["name"]) 
    count = count + 1
    num = num + 1
user = eval(input("Type your course number, about which course do you want to know? : - "))
course_id = dict_file["availableCourses"][user - 1]["id"]
file_name = "exercises_" + str(course_id) + ".json"
print (" ")
print ("File name.")
print (file_name)
print ("File name.")
print (" ")
slug_list = []
user_url = "http://saral.navgurukul.org/api/courses/" + str(course_id) + "/exercises"
try:
        if (ifCache == True):
                read_file = open("exercises_" + str(course_id) + ".json", "r")
                show_file = read_file.read()
                # print ("your data is in this file:- ", "exercises_" + str(course_id) + ".json")
                print (show_file)
                # print (" ")
                ifCache = False
        
except:
        print (" ")
        print ("yes")
        print (dict_file["availableCourses"][user - 1])
        print ("yes")
        print (" ")
        course_id = dict_file["availableCourses"][user - 1]["id"]
        user_url = "http://saral.navgurukul.org/api/courses/" + str(course_id) + "/exercises"
        json_value = request_url(user_url)
        str_json_value = json.dumps(json_value)
        dict_json_value = json.loads(str_json_value)
        with open("exercises_" + str(course_id) + ".json", "w") as helper_file:
                helper_file.write(str_json_value)
        read_file = open("exercises_" + str(course_id) + ".json", "r"   )
        show_file = read_file.read()
        print (show_file)
        count = 0
        num = 1
        print (" ")
        print ("****** childExercises********************")
        while(count < len(dict_json_value["data"])):
                if (dict_json_value["data"][count]["childExercises"] == []):
                        print (num, "none")
                else:
                        print (num, dict_json_value["data"][count]["childExercises"])
                count = count + 1
                num = num + 1
        print (" ")
        print ("*************************slug and id************************************")
        count = 0
        num = 1
        while(count < len(dict_json_value["data"])):
                print (num, dict_json_value["data"][count]["slug"])
                slug_list.append(dict_json_value["data"][count]["slug"])
                print ("id :- ", dict_json_value["data"][count]["id"])
                num = num + 1
                count = count + 1

user = input("If you want to see content of this exercise enter exercise number:- ")
print (dict_json_value["data"][user - 1]["slug"]) 
# content =  user_url + "/getBySlug?slug=" + (dict_json_value["data"][user - 1]["slug"]) 
# print (" ")
# print ("*****************************************************")
# # print (slug_list)
# slug_apicall = request_url(content)
# print (slug_apicall)
# print ("####")