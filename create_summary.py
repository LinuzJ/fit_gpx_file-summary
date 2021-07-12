import gpxpy
import gpxpy.gpx
from fitparse import FitFile
from datetime import datetime

def calculate_duration(start, end):
    diff = end - start
    return int(round(diff.total_seconds() / 60))

def handle_fit(file):
    # Metrics we want to evaluate
    distance = 0
    time = 0
    max_hr = 0
    avg_hr = 0
    max_speed = 0
    avg_speed = 0
    max_grade = 0

    # collections of data
    hr = []
    speed = []
    time_collection = []
    
    fitfile = FitFile(file)
    # Then go through all of the data entries in the file
    for data_message in fitfile.get_messages("record"):
        hr.append(data_message.get_value("heart_rate"))
        speed.append(data_message.get_value("speed"))
        time_collection.append(data_message.get_value("timestamp"))

        if data_message.get_value("grade") and data_message.get_value("grade") > max_grade:
            max_grade = data_message.get_value("grade")

        if data_message.get_value("distance") and data_message.get_value("distance") > max_grade:
            distance = data_message.get_value("distance")

    time = calculate_duration(time_collection[0], time_collection[-1])
    max_hr = max(hr)
    avg_hr = sum(hr)/len(hr)


    print(time)



def summarize(activity, type):
    
    if type == ".fit":
        handle_fit(activity)
    elif type == ".gpx":
        pass