import requests                                                 # we import requests moduele because request is allowing to send HTTP to server cause we can get every thing whatever we want.   
base_url = "http://saral.navgurukul.org/api/courses"            # here in base_url I store one link and I will take all the data of this link thats why we are using json or request because if we have need of data so we can feach from other.
request = requests.get(base_url)                                # Now I use requests.get() because I want data of this link so from this link I can get data of that link, "requests.get() is helping to get data from any link."
                                                                #The method get() returns a value for the given key.If key is not available then returns defult value None.
response = request.json()
                                                                # And here whatever data I goted in request variable, I am changing in json because I can use that data in any program.
                                                                # JSON is helping to communicate with other languase thats why we are using JSON.
                                                                # print (reponce)
                                                                # Than after I print reponce, Now we can see the data of that link and we use also.
print (response)
print (type(response))
import json                                                     # Now I import json for make new json file.
data = json.dumps(response)                                     # Because I want to use json file thats why I am dumping the json data which is stor in reponce in a string and storing in data variable.
with open("course.json", "w") as file_hender:                   # after dumping I am opening one json file name is course.json and I want to write on that file that's why I am using w and for writing on that file I took one variable file_hander who will help us to write in json file.
    file_hender.write(data)                                     # And here the file_hender is writing in that file whatever stored in data variable.
read_file = open("course.json","r") 
str_file = read_file.read()
                                                                # print (str_file)
                                                                # print (type(str_file))
dict_file = json.loads(str_file)
                                                                # print (dict_file)
                                                                # print (type(dict_file))
count = 0
num = 1
                                                                # print (len(dict_file["availableCourses"]))
while count < len(dict_file["availableCourses"]):
    print (num,dict_file["availableCourses"][count]["name"]) 
    count = count + 1
    num = num + 1
user = eval(input("Type your course number, about which course do you want to know? : - "))
print ("*******This is the data of your course *******")
print (" ")
print (dict_file["availableCourses"][user - 1])
course_id = dict_file["availableCourses"][user - 1]["id"]
                                                                # print (course_id)
user_url = "http://saral.navgurukul.org/api/courses/" + str(course_id) + "/exercises"
                                                                # print (user_url)
import requests
link_value = requests.get(user_url)
json_value = link_value.json()
print (json_value)
str_json_value = json.dumps(json_value)
dict_json_value = json.loads(str_json_value)
                                                                # print ("########################################################")
                                                                # print (dict_json_value)
                                                                # print (type(json_value))print (dict_json_value)
                                                                # print (type(json_value))
print (" ")                                                                
print ("**********" + "open in new file name:- " + "exercises_" + str(course_id) + ".json" + "**********")
with open("exercises_" + str(course_id) + ".json", "w") as helper_file:
    helper_file.write(str_json_value)
read_file = open("exercises_" + str(course_id) + ".json", "r")
show_file = read_file.read()
print (show_file)
print ("################" +"Till here" + "################")
print (" ")
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
num = 0
while(count < len(dict_json_value["data"])):
    print (num, "Slug :- ", dict_json_value["data"][count]["slug"])
    print ("id :- ", dict_json_value["data"][count]["id"])
    num = num + 1
    count = count + 1
