import json
import csv
from datetime import datetime
# from random import uniform

# l = [[uniform(-90, 90), uniform(-180, 180)] for _ in range(1000)]
# with open("random_1k.json", 'w') as f:
#     json.dump(l, f, indent=4)

runs_list = ["2015-11-01 00:00:00",
        "2015-11-01 06:00:00",
        "2015-11-01 12:00:00",
        "2015-11-01 18:00:00",
        "2015-11-02 06:00:00",
        "2015-11-02 12:00:00",
        "2015-11-03 00:00:00",
        "2015-11-03 06:00:00",
        "2015-11-03 12:00:00",
        "2015-11-03 18:00:00",
        "2015-11-04 00:00:00",
        "2015-11-04 06:00:00",
        "2015-11-04 12:00:00",
        "2015-11-04 18:00:00",
        "2015-11-05 00:00:00",
        "2015-11-05 06:00:00",
        "2015-11-05 12:00:00",
        "2015-11-05 18:00:00",
        "2015-11-06 00:00:00",
        "2015-11-06 06:00:00",
        "2015-11-06 12:00:00",
        "2015-11-06 18:00:00",
        "2015-11-07 00:00:00",
        "2015-11-07 06:00:00",
        "2015-11-07 12:00:00",
        "2015-11-07 18:00:00",
        "2015-11-08 00:00:00",
        "2015-11-08 06:00:00",
        "2015-11-08 12:00:00",
        "2015-11-08 18:00:00",
        "2015-11-09 00:00:00",
        "2015-11-09 06:00:00",
        "2015-11-09 12:00:00",
        "2015-11-09 18:00:00",
        "2015-11-10 00:00:00",
        "2015-11-10 06:00:00",
        "2015-11-10 12:00:00",
        "2015-11-10 18:00:00",
        "2015-11-11 00:00:00",
        "2015-11-11 06:00:00",
        "2015-11-11 12:00:00",
        "2015-11-11 18:00:00",
        "2015-11-12 00:00:00",
        "2015-11-12 06:00:00",
        "2015-11-12 12:00:00",
        "2015-11-12 18:00:00",
        "2015-11-13 00:00:00",
        "2015-11-13 06:00:00",
        "2015-11-13 12:00:00",
        "2015-11-13 18:00:00",
        "2015-11-14 00:00:00",
        "2015-11-14 06:00:00",
        "2015-11-14 12:00:00",
        "2015-11-14 18:00:00",
        "2015-11-15 00:00:00",
        "2015-11-15 06:00:00",
        "2015-11-15 12:00:00",
        "2015-11-15 18:00:00",
        "2016-11-01 00:00:00",
        "2016-11-01 06:00:00",
        "2016-11-01 12:00:00",
        "2016-11-01 18:00:00",
        "2016-11-02 00:00:00",
        "2016-11-02 06:00:00",
        "2016-11-02 12:00:00",
        "2016-11-02 18:00:00",
        "2016-11-03 00:00:00",
        "2016-11-03 06:00:00",
        "2016-11-03 12:00:00",
        "2016-11-03 18:00:00",
        "2016-11-04 00:00:00",
        "2016-11-04 06:00:00",
        "2016-11-04 12:00:00",
        "2016-11-04 18:00:00",
        "2016-11-05 00:00:00",
        "2016-11-05 06:00:00",
        "2016-11-05 12:00:00",
        "2016-11-05 18:00:00",
        "2016-11-06 00:00:00",
        "2016-11-06 06:00:00",
        "2016-11-06 12:00:00",
        "2016-11-06 18:00:00",
        "2016-11-07 00:00:00",
        "2016-11-07 06:00:00",
        "2016-11-07 12:00:00",
        "2016-11-07 18:00:00",
        "2016-11-08 00:00:00",
        "2016-11-08 06:00:00",
        "2016-11-08 12:00:00",
        "2016-11-08 18:00:00",
        "2016-11-09 00:00:00",
        "2016-11-09 06:00:00",
        "2016-11-09 12:00:00",
        "2016-11-09 18:00:00",
        "2016-11-10 00:00:00",
        "2016-11-10 06:00:00",
        "2016-11-10 12:00:00",
        "2016-11-10 18:00:00",
        "2016-11-11 00:00:00",
        "2016-11-11 06:00:00",
        "2016-11-11 12:00:00",
        "2016-11-11 18:00:00",
        "2016-11-12 00:00:00",
        "2016-11-12 06:00:00",
        "2016-11-12 12:00:00",
        "2016-11-12 18:00:00",
        "2016-11-13 00:00:00",
        "2016-11-13 06:00:00",
        "2016-11-13 12:00:00",
        "2016-11-13 18:00:00",
        "2016-11-14 00:00:00",
        "2016-11-14 06:00:00",
        "2016-11-14 12:00:00",
        "2016-11-14 18:00:00",
        "2016-11-15 00:00:00",
        "2016-11-15 06:00:00",
        "2016-11-15 12:00:00",
        "2016-11-15 18:00:00",
        "2017-11-01 00:00:00",
        "2017-11-01 06:00:00",
        "2017-11-01 12:00:00",
        "2017-11-01 18:00:00",
        "2017-11-02 00:00:00",
        "2017-11-02 06:00:00",
        "2017-11-02 12:00:00",
        "2017-11-02 18:00:00",
        "2017-11-03 00:00:00",
        "2017-11-03 06:00:00",
        "2017-11-03 12:00:00",
        "2017-11-03 18:00:00",
        "2017-11-04 00:00:00",
        "2017-11-04 06:00:00",
        "2017-11-04 12:00:00",
        "2017-11-04 18:00:00",
        "2017-11-05 00:00:00",
        "2017-11-05 06:00:00",
        "2017-11-05 12:00:00",
        "2017-11-05 18:00:00",
        "2017-11-06 00:00:00",
        "2017-11-06 06:00:00",
        "2017-11-06 12:00:00",
        "2017-11-06 18:00:00",
        "2017-11-07 00:00:00",
        "2017-11-07 06:00:00",
        "2017-11-07 12:00:00",
        "2017-11-07 18:00:00",
        "2017-11-08 00:00:00",
        "2017-11-08 06:00:00",
        "2017-11-08 12:00:00",
        "2017-11-08 18:00:00",
        "2017-11-09 00:00:00",
        "2017-11-09 06:00:00",
        "2017-11-09 12:00:00",
        "2017-11-09 18:00:00",
        "2017-11-10 00:00:00",
        "2017-11-10 06:00:00",
        "2017-11-10 12:00:00",
        "2017-11-10 18:00:00",
        "2017-11-12 00:00:00",
        "2017-11-12 06:00:00",
        "2017-11-13 00:00:00",
        "2017-11-13 06:00:00",
        "2017-11-13 12:00:00",
        "2017-11-13 18:00:00",
        "2017-11-14 00:00:00",
        "2017-11-14 06:00:00",
        "2017-11-14 12:00:00",
        "2017-11-14 18:00:00",
        "2017-11-15 00:00:00",
        "2017-11-15 06:00:00",
        "2017-11-15 12:00:00",
        "2017-11-15 18:00:00",
        "2018-11-01 00:00:00",
        "2018-11-01 06:00:00",
        "2018-11-01 12:00:00",
        "2018-11-01 18:00:00",
        "2018-11-02 00:00:00",
        "2018-11-02 06:00:00",
        "2018-11-02 12:00:00",
        "2018-11-02 18:00:00",
        "2018-11-03 00:00:00",
        "2018-11-03 06:00:00",
        "2018-11-03 12:00:00",
        "2018-11-03 18:00:00",
        "2018-11-04 00:00:00",
        "2018-11-04 06:00:00",
        "2018-11-05 18:00:00",
        "2018-11-06 00:00:00",
        "2018-11-07 00:00:00",
        "2018-11-07 06:00:00",
        "2018-11-07 12:00:00",
        "2018-11-07 18:00:00",
        "2018-11-08 00:00:00",
        "2018-11-08 06:00:00",
        "2018-11-08 12:00:00",
        "2018-11-08 18:00:00",
        "2018-11-09 00:00:00",
        "2018-11-09 06:00:00",
        "2018-11-09 12:00:00",
        "2018-11-09 18:00:00",
        "2018-11-10 00:00:00",
        "2018-11-10 06:00:00",
        "2018-11-10 12:00:00",
        "2018-11-10 18:00:00",
        "2018-11-11 00:00:00",
        "2018-11-11 06:00:00",
        "2018-11-11 12:00:00",
        "2018-11-11 18:00:00",
        "2018-11-12 00:00:00",
        "2018-11-12 06:00:00",
        "2018-11-12 12:00:00",
        "2018-11-12 18:00:00",
        "2018-11-13 00:00:00",
        "2018-11-13 06:00:00",
        "2018-11-13 12:00:00",
        "2018-11-13 18:00:00",
        "2018-11-14 00:00:00",
        "2018-11-14 06:00:00",
        "2018-11-14 12:00:00",
        "2018-11-14 18:00:00",
        "2018-11-15 00:00:00",
        "2018-11-15 06:00:00",
        "2018-11-15 12:00:00",
        "2018-11-15 18:00:00",
        "2019-11-01 00:00:00",
        "2019-11-01 06:00:00",
        "2019-11-01 12:00:00",
        "2019-11-01 18:00:00",
        "2019-11-02 00:00:00",
        "2019-11-02 06:00:00",
        "2019-11-02 12:00:00",
        "2019-11-02 18:00:00",
        "2019-11-03 00:00:00",
        "2019-11-03 06:00:00",
        "2019-11-03 12:00:00",
        "2019-11-03 18:00:00",
        "2019-11-04 00:00:00",
        "2019-11-04 06:00:00",
        "2019-11-04 12:00:00",
        "2019-11-04 18:00:00",
        "2019-11-05 00:00:00",
        "2019-11-05 12:00:00",
        "2019-11-05 18:00:00",
        "2019-11-06 00:00:00",
        "2019-11-06 18:00:00",
        "2019-11-07 00:00:00",
        "2019-11-07 06:00:00",
        "2019-11-07 12:00:00",
        "2019-11-07 18:00:00",
        "2019-11-08 00:00:00",
        "2019-11-08 06:00:00",
        "2019-11-08 12:00:00",
        "2019-11-09 06:00:00",
        "2019-11-09 12:00:00",
        "2019-11-09 18:00:00",
        "2019-11-10 00:00:00",
        "2019-11-10 06:00:00",
        "2019-11-10 12:00:00",
        "2019-11-10 18:00:00",
        "2019-11-11 00:00:00",
        "2019-11-11 06:00:00",
        "2019-11-11 12:00:00",
        "2019-11-11 18:00:00",
        "2019-11-12 00:00:00",
        "2019-11-12 06:00:00",
        "2019-11-12 12:00:00",
        "2019-11-12 18:00:00",
        "2019-11-13 00:00:00",
        "2019-11-13 06:00:00",
        "2019-11-13 12:00:00",
        "2019-11-13 18:00:00",
        "2019-11-14 00:00:00",
        "2019-11-14 12:00:00",
        "2019-11-14 06:00:00",
        "2019-11-14 18:00:00",
        "2019-11-15 00:00:00",
        "2019-11-15 06:00:00",
        "2019-11-15 12:00:00",
        "2019-11-15 18:00:00"
]

runs = {k: [] for k in runs_list}

with open("transat.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    for row in reader:
        runs[row["Run"]].append([row["Latitude"], row["Longitude"]])
    with open(f"example_routes.json", 'w') as f:
        json.dump(runs, f, indent=4)

# with open("example_routes.json", 'r') as routes_file,\
#   open("30_routes.json", 'w') as routes_sample:
#     json.dump([i for s in list(json.load(routes_file).values())[:20] for i in s], routes_sample)
