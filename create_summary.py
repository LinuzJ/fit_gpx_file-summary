import gpxpy
import gpxpy.gpx
from fitparse import FitFile
from datetime import datetime

def calculate_duration(start, end):
    diff = end - start
    return int(round(diff.total_seconds() / 60))

class Fit_Result:
    def __init__(self, fit_file):
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
        
        fitfile = FitFile(fit_file)
        # Then go through all of the data entries in the file
        for data_message in fitfile.get_messages("record"):
            hr.append(data_message.get_value("heart_rate"))
            speed.append(data_message.get_value("speed"))
            time_collection.append(data_message.get_value("timestamp"))

            if data_message.get_value("grade") and data_message.get_value("grade") > max_grade:
                max_grade = data_message.get_value("grade")

            if data_message.get_value("distance") and data_message.get_value("distance") > max_grade:
                distance = data_message.get_value("distance")

        self.time = calculate_duration(time_collection[0], time_collection[-1])
        self.max_hr = max(hr)
        self.avg_hr = round(sum(hr)/len(hr))
        self.max_speed = max(speed)
        self.avg_speed = round(sum(speed)/len(speed))
        self.distance = distance/1000
        self.max_grade = max_grade
        

def print_result(result_object):
    print("____________________________________________________")
    print("                                                    ")
    print("  Duration: %s         Distance: %a \n  Max HR: %s          Average HR: %s" % (result_object.time, result_object.distance, result_object.max_hr, result_object.avg_hr))
    print("  Max Speed: %s        Average Speed: %s \n  Max grade: %s" % (result_object.max_speed, result_object.avg_speed, result_object.max_grade))
    print("____________________________________________________")

def summarize(activity, type):
    
    if type == ".fit":
        result = Fit_Result(activity)
        print_result(result)
    elif type == ".gpx":
        pass