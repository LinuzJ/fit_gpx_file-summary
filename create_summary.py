import gpxpy
import gpxpy.gpx
import math
from fitparse import FitFile
from datetime import datetime
import xml.etree.ElementTree as ET
from xml.dom import minidom

def calculate_duration(start, end):
    diff = end - start
    return int(round(diff.total_seconds() / 60))

def calculate_distance(lat_1, lng_1, lat_2, lng_2): 
    
    d_lat = math.radians(lat_2) - math.radians(lat_1)
    d_lng = math.radians(lng_2) - math.radians(lng_1) 

    calculation = (  
         math.sin(d_lat / 2) ** 2 
       + math.cos(lat_1) 
       * math.cos(lat_2) 
       * math.sin(d_lng / 2) ** 2
    )

    return 6373.0 * (2 * math.atan2(math.sqrt(calculation), math.sqrt(1 - calculation)))

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

class Gpx_result:
    def __init__(self, gpx_file) -> None:
        gpx_file_open = open(gpx_file, 'r')

        gpx = gpxpy.parse(gpx_file_open)

        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    print(point.extensions[0].items())

        self.gpx = gpx




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
        result = Gpx_result(activity)
        print("end")