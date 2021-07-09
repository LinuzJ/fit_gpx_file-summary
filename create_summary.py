import gpxpy
import gpxpy.gpx
from fitparse import FitFile

def summarize(activity, type):
    if type == ".fit":
        print("fit")
    elif type == ".gpx":
        print("gpx")