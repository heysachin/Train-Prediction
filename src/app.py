
# Created by Sachin Dev on 09/06/18

import csv
from flask import Flask, render_template, request
from common.database import Database
from models.stations.station import Station
from models.trains.train import Train
from src.models.timetables.timetable import TimeTable

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = 'sachin'


@app.before_first_request
def _init_db():
    Database.initialize()


@app.route('/trains/btw', methods=['POST'])
def trains_between_stations():
    source = request.form['source']
    source = source.upper()
    destination = request.form['destination']
    destination = destination.upper()
    trains = TimeTable.trains_btw_stations(source, destination)
    return render_template("trains_btw_stations.html", trains=trains, source=source,destination=destination)


@app.route('/trains/through', methods=['POST'])
def trains_through():
    source = request.form['source']
    source = source.upper()
    source_station = Station.get_by_id(source)
    through = request.form['through']
    through = through.upper()
    through_station = Station.get_by_id(through)
    destination = request.form['destination']
    destination = destination.upper()
    destination_station = Station.get_by_id(destination)
    trains = TimeTable.connecting_trains(source, through, destination)
    return render_template("trains_through.html", trains=trains, source=source_station, through=through_station, destination=destination_station)


@app.route('/timetable/<string:train_no>')
def get_timetable(train_no):
    train_class = Train.get_by_id(train_no)
    stations = TimeTable.get_stations_class_by_train(train_no)
    return render_template("timetable.html", stations=stations, train_class=train_class)


@app.route('/')
def home():
    stations = Station.all()
    return render_template('home.html', stations=stations)


Database.initialize()

# path = '/Volumes/SSD2/Documents/Python Workplace/Train Prediction/src/'
# Database.initialize()
# # For initialising MongoDB on Railway Stations
# file = open(path + "station_data.csv", "r", encoding='utf-8')
# reader = csv.reader(file)
# for line in reader:
#     t = line[0], line[1]
#     station = Station(str(line[1]), str(line[0]))
#     station.save_to_mongo()
#     print(t)

# # For initialising MongoDB on Trains
# file = open(path + "train_data.csv", "r", encoding='utf-8')
# reader = csv.reader(file)
# for line in reader:
#     t = line[0], line[1], line[2], line[3]
#     train = Train(str(line[1]), str(line[2]), str(line[3]), str(line[0]))
#     train.save_to_mongo()
#     print(t)


# #For initialising MongoDB on Timetable Full
# file = open(path + "timetable_expanded.csv", "r", encoding='utf-8')
# reader = csv.reader(file)
# for line in reader:
#     t = line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10], line[11]
#     timetable = TimeTable(str(line[0]), str(line[1]), str(line[2]), str(line[3]),
#                           str(line[4]), str(line[5]),str(line[6]), str(line[7]),
#                           str(line[8]), str(line[9]), str(line[10]), str(line[11]))
#     timetable.save_to_mongo()
#     print(t)

# print(TimeTable.get_trains_by_station("PGT"))
# print(TimeTable.trains_btw_stations("PGT", "TVC"))
# print(TimeTable.get_stations_by_train("16343"))