#
# CS 196 Data Hackerspace
# Assignment 1: Data Parsing and NumPy
# Due September 24th, 2018
#

import json
import csv
import numpy as np

def histogram_times(filename):
    import re
    with open('airplane_crashes.csv') as f:
        csv_reader = csv.reader(f)
        airplane_data = list(csv_reader)
    time = []
    count = 0
    for i in range(0,24):
        time.append(0)
    for row in airplane_data[1:]:
        raw = row[1]
        onlyNumber = re.sub("[^0-9].", "", raw)
        if onlyNumber is '':
            continue
        hour = int(onlyNumber[:2])
        count += 1
        modded = int(hour % 24)
        time[modded] += 1
    return time

def weigh_pokemons(filename, weight):
    import re
    with open(filename) as f:
        pokemon_json = json.load(f)
    weighted = []
    for item in pokemon_json["pokemon"]:
        pkmnWeight = item.get("weight")
        non_decimal = re.compile(r'[^\d.]+')
        onlyNum = non_decimal.sub('', pkmnWeight)
        if (float(onlyNum) == weight):
            weighted += {item.get("name")}
    return weighted

def single_type_candy_count(filename):
    with open(filename) as f:
        candy_json = json.load(f)
    totalCandy = 0
    for item in candy_json["pokemon"]:
        pkmnType = item.get("type")
        if (len(pkmnType) != 1):
            continue
        if (item.get("candy_count") != None):
            totalCandy += int(item.get("candy_count"))
    return totalCandy

def reflections_and_projections(points):
    pyArray = np.array(points)
    for i in range(0,len(pyArray[0])):
        pyArray[1][i] = pyArray[1][i] * (-1) + 2
    multiplier = [[0, -1], [1, 0]]
    rotated = np.matmul(multiplier, pyArray)
    multiplier2 = [[0.1, 0.3], [0.3, 0.9]]
    projected = np.matmul(multiplier2, rotated)
    return projected

def normalize(image):
    minimum = np.amin(image)
    maximum = np.amax(image)
    subtracted = np.subtract(image, minimum)
    normal = np.multiply(image, 255/(maximum - minimum))
    return normal

def sigmoid_normalize(image, variance):
    import math
    pPrime = []
    single = np.ravel(image)
    for i in range(0, len(single)):
        pPrime.append(255(1 + float(single[i]) ** (-1)))
    return pPrime
