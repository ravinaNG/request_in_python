import requests   
import json
from pathlib import Path 

def request_url(url):
    request = requests.get(url)
    response = request.json()
    return (response)

def open_json_file(file_name, data):
    with open(file_name, "w") as file_hender:
        file_hender.write(data)
        return file_hender

def read_json_file(file_name):
    read_file = open(file_name,"r") 
    str_file = read_file.read()
    return str_file

def courses(data, name):
    count = 0
    id_list = []
    while(count < len(data["availableCourses"])):
        print ((count+1), data["availableCourses"][count][name])
        id_list.append(data["availableCourses"][count]['id'])
        count = count + 1
    return id_list

def child_and_parentExercise(data):
    exercise_slug_list = []
    count = 0
    num = 1
    while (count < len(data['data'])):
        print (num, (data['data'][count]['name']))
        exercise_slug_list.append(data['data'][count]['slug'])
        if (data['data'][count]['childExercises'] != []):
            counter = 0
            while (counter < len(data['data'][count]['childExercises'])):
                print (("    "), (num+1), (data['data'][count]['childExercises'][counter]['name']))
                exercise_slug_list.append(data['data'][count]['childExercises'][counter]['slug'])
                num = num + 1
                counter = counter + 1
        num = num + 1
        count = count + 1
    return exercise_slug_list

def child_or_parentExercise(data, exercise_name):
    count = 0
    while (count < len(data['data'])):
        if(exercise_name == (data['data'][count]['name'])):
            print ("This is ParentExercise.")
        if (data['data'][count]['childExercises'] != []):
            counter = 0
            while (counter < len(data['data'][count]['childExercises'])):
                if(exercise_name == (data['data'][count]['childExercises'][counter]['name'])):
                    print ("This is childExercise.")
                counter = counter + 1
        count = count + 1

course_url = "http://saral.navgurukul.org/api/courses"

call_api = request_url(course_url)
data = json.dumps(call_api)

config = Path('courses.json')

if config.is_file():
    str_file = read_json_file("courses.json")
    dict_file = json.loads(str_file)
else:
    open_json_file("courses.json", data)
    str_file = read_json_file("courses.json")
    dict_file = json.loads(str_file)
name = "name"
id_list = courses(dict_file, name)
print (" ")
user = int(input("Enter course number for id:- "))
id = (id_list[user-1])

exercise_url = "http://saral.navgurukul.org/api/courses/" + str(id) + "/exercises" 
exerercise_data = request_url(exercise_url)
exerercise_data = json.dumps(exerercise_data)

config = Path('course' + str(id) + '.json')
file_name = 'course' + str(id) + '.json'
print (config)

if config.is_file():
    str_file = read_json_file(file_name)
    json_file = json.loads(str_file)
    print ("*******************************************************************")
else:
    open_json_file(file_name, exerercise_data)
    str_file = read_json_file(file_name)
    json_file = json.loads(str_file)
    print ("-----------------------------------------------------------------------")

print (json_file)
exercise_slug_list = child_and_parentExercise(json_file)

user_for_slug = int(input("Enter Exercise number for slug:- "))
exercise_name = exercise_slug_list[user_for_slug-1]
child_or_parentExercise(json_file, exercise_name)

slug_url = "http://saral.navgurukul.org/api/courses/" + str(id) + "/exercise" + "/getBySlug?slug=" + exercise_name
print (" ")
print (slug_url)
slug_data = request_url(slug_url)
content = json.dumps(slug_data)
for_slug = json.loads(content)
print (" ")
print ("..................................................................................")
print (for_slug["content"])

while True:
    print (" ")
    any_more = input("up-course, n-next and p-privious what do you want:- ")
    if(user_for_slug == 0 or user_for_slug == len(exercise_slug_list)):
        print ("Sorry there is no slug.")
        break
    if(any_more == "up"):
        call_api = request_url(course_url)
        data = json.dumps(call_api)
        str_file = read_json_file("courses.json")
        dict_file = json.loads(str_file)
        name = "name"
        list = courses(dict_file, name)
    elif(any_more == "n"):
        user_for_slug = user_for_slug + 1
        exercise_name = exercise_slug_list[user_for_slug-1]
        child_or_parentExercise(json_file, exercise_name)
        slug_url = "http://saral.navgurukul.org/api/courses/" + str(id) + "/exercise" + "/getBySlug?slug=" + exercise_name
        print (" ")
        print (slug_url)
        slug_data = request_url(slug_url)
        content = json.dumps(slug_data)
        for_slug = json.loads(content)
        print (" ")
        print ("..................................................................................")
        print (for_slug["content"])
    elif(any_more == "p"):
        user_for_slug = user_for_slug - 1
        exercise_name = exercise_slug_list[user_for_slug-1]
        child_or_parentExercise(json_file, exercise_name)
        slug_url = "http://saral.navgurukul.org/api/courses/" + str(id) + "/exercise" + "/getBySlug?slug=" + exercise_name
        print (" ")
        print (slug_url)
        slug_data = request_url(slug_url)
        content = json.dumps(slug_data)
        for_slug = json.loads(content)
        print (" ")
        print ("..................................................................................")
        print (for_slug["content"])

























# open_json_file("course2.json", data)
# str_file = read_json_file("course2.json")
# dict_file = json.loads(str_file)