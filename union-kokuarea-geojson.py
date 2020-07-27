#!/usr/bin/env python

import os
import json
import hashlib
import urllib.request
import time

OUTPUT_FILENAME = "all-kokuarea.geojson"


def download_geojsons():

    filenames = []

    # ズームレベルは8だけ。x と y は日本全体を囲む範囲で。
    for x in range(214, 233):
        for y in range(90, 112):
            url = "https://maps.gsi.go.jp/xyz/kokuarea/8/{0}/{1}.geojson".format(
                x, y)

            filename = hashlib.md5(url.encode()).hexdigest() + ".geojson"

            try:
                urllib.request.urlretrieve(url, filename)
                filenames.append(filename)
                print("download", url, "to", filename)

            except urllib.error.HTTPError as e:
                print("http error", e.code, url)

            time.sleep(1)  # サーバーの負荷を下げるため sleep を入れる。

    return filenames


def union_geojsons(filenames):

    kokuareas = {"type": "FeatureCollection",    "features": []}

    for filename in filenames:
        with open(filename, 'r') as file:
            t = json.load(file)

        for feature in t["features"]:
            kokuareas["features"].append(feature)

        print("union", filename)

    return kokuareas


def remove_files(filenames):

    for filename in filenames:
        os.remove(filename)
        print("remove", filename)


if __name__ == "__main__":
    filenames = download_geojsons()
    kokuareas = union_geojsons(filenames)
    remove_files(filenames)

    with open(OUTPUT_FILENAME, 'w') as file:
        json.dump(kokuareas, file, ensure_ascii=False)

    print("output", OUTPUT_FILENAME)
