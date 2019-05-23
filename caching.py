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

def append_in_json_file(file_name, data):
    with open(str(file_name), "a+") as file_hender:
        demo = json.dumps(data)
        file_hender.write(demo)
        # return file_hender
    # demo = json.loads(file_hender)
    # demo = json.loads(demo)
    # return demo

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
    print ("***")
    print (len(data['data']))
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

config = Path('courses.json')

if config.is_file():
    str_file = read_json_file("courses.json")
    dict_file = json.loads(str_file)
else:
    call_api = request_url(course_url)
    data = json.dumps(call_api)
    open_json_file("courses.json", data)
    str_file = read_json_file("courses.json")
    dict_file = json.loads(str_file)
name = "name"
id_list = courses(dict_file, name)
print (" ")
user = int(input("Enter course number for id:- "))
id = (id_list[user-1])
