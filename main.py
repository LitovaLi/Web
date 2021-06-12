from flask import Flask, json
import csv

app = Flask(__name__)


@app.route('/flights/<id>', methods=['GET'])
def flights(id):
    with open('flights.csv') as file:
        file_reader = csv.reader(file)
        id_flight = id
        for row in file_reader:
            if row[0] == id_flight:
                data = {
                    'ArrivalTime': row[6],
                    'DepartureTime': row[4],
                    'Number': row[7]
                }
                return json.dumps(data)
        return "<h3>Sorry, try another id flight<h3>"


if __name__ == '__main__':
    app.run()
