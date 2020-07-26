#!/usr/bin/env python

import os
import json
import urllib.request


def union_geojson():

    urls = [
        "https://maps.gsi.go.jp/xyz/kokuarea/8/215/110.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/216/109.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/216/110.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/217/109.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/219/101.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/218/108.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/219/108.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/219/103.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/219/102.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/219/107.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/220/104.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/220/102.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/220/103.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/220/106.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/220/105.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/221/101.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/221/102.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/221/103.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/221/104.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/221/105.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/221/108.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/222/100.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/222/101.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/222/102.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/222/103.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/223/100.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/223/101.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/223/102.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/224/100.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/224/101.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/224/102.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/225/99.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/225/100.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/225/101.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/226/98.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/226/100.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/226/101.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/226/102.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/227/94.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/227/95.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/227/96.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/227/97.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/227/98.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/227/99.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/227/100.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/227/101.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/227/102.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/227/103.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/228/91.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/228/93.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/228/94.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/228/95.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/228/96.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/228/97.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/228/98.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/228/100.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/228/109.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/229/92.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/229/93.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/229/94.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/230/92.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/230/93.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/230/94.geojson",
        "https://maps.gsi.go.jp/xyz/kokuarea/8/231/93.geojson",
    ]

    DOWNLOAD_FILENAME = "download.geojson"

    kokuareas = {"type": "FeatureCollection",    "features": []}

    for url in urls:
        print(url)

        urllib.request.urlretrieve(url, DOWNLOAD_FILENAME)

        with open(DOWNLOAD_FILENAME, 'r') as file:
            t = json.load(file)

        for feature in t["features"]:
            kokuareas["features"].append(feature)

    os.remove(DOWNLOAD_FILENAME)

    return kokuareas


if __name__ == "__main__":
    kokuareas = union_geojson()

    with open("all-kokuarea.geojson", 'w') as file:
        json.dump(kokuareas, file, ensure_ascii=False)
