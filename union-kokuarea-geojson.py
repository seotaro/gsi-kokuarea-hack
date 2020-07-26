#!/usr/bin/env python

import json

filenames = [
    "8-215-110.geojson",
    "8-216-109.geojson",
    "8-216-110.geojson",
    "8-217-109.geojson",
    "8-219-101.geojson",
    "8-218-108.geojson",
    "8-219-108.geojson",
    "8-219-103.geojson",
    "8-219-102.geojson",
    "8-219-107.geojson",
    "8-220-104.geojson",
    "8-220-102.geojson",
    "8-220-103.geojson",
    "8-220-106.geojson",
    "8-220-105.geojson",
    "8-221-101.geojson",
    "8-221-102.geojson",
    "8-221-103.geojson",
    "8-221-104.geojson",
    "8-221-105.geojson",
    "8-221-108.geojson",
    "8-222-100.geojson",
    "8-222-101.geojson",
    "8-222-102.geojson",
    "8-222-103.geojson",
    "8-223-100.geojson",
    "8-223-101.geojson",
    "8-223-102.geojson",
    "8-224-100.geojson",
    "8-224-101.geojson",
    "8-224-102.geojson",
    "8-225-99.geojson",
    "8-225-100.geojson",
    "8-225-101.geojson",
    "8-226-98.geojson",
    "8-226-100.geojson",
    "8-226-101.geojson",
    "8-226-102.geojson",
    "8-227-94.geojson",
    "8-227-95.geojson",
    "8-227-96.geojson",
    "8-227-97.geojson",
    "8-227-98.geojson",
    "8-227-99.geojson",
    "8-227-100.geojson",
    "8-227-101.geojson",
    "8-227-102.geojson",
    "8-227-103.geojson",
    "8-228-91.geojson",
    "8-228-93.geojson",
    "8-228-94.geojson",
    "8-228-95.geojson",
    "8-228-96.geojson",
    "8-228-97.geojson",
    "8-228-98.geojson",
    "8-228-100.geojson",
    "8-228-109.geojson",
    "8-229-92.geojson",
    "8-229-93.geojson",
    "8-229-94.geojson",
    "8-230-92.geojson",
    "8-230-93.geojson",
    "8-230-94.geojson",
    "8-231-93.geojson"
]


kokuareas = {"type": "FeatureCollection",    "features": []}
print(kokuareas)

for filename in filenames:
    print(filename)

    with open(filename, 'r') as file:
        t = json.load(file)

    for feature in t["features"]:
        kokuareas["features"].append(feature)

with open("all-kokuarea.geojson", 'w') as file:
    json.dump(kokuareas, file, ensure_ascii=False)
