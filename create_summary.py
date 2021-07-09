import gpxpy
import gpxpy.gpx
from fitparse import FitFile

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
    
    fitfile = FitFile(file)
    # Then go through all of the data entries in the file
    for data_message in fitfile.get_messages("record"):
        hr.append(data_message.get_value("heart_rate"))
        speed.append(data_message.get_value("speed"))

        if data_message.get_value("grade") and data_message.get_value("grade") > max_grade:
            max_grade = data_message.get_value("grade")
    
    max_hr = max(hr)
    avg_hr = sum(hr)/len(hr)

    print(max_hr, avg_hr, max_grade)



def summarize(activity, type):
    
    if type == ".fit":
        handle_fit(activity)
    elif type == ".gpx":
        pass