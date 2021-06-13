from flask import Flask, json
import csv

app = Flask(__name__)


@app.route('/flights/<flight_id>', methods=['GET'])
def flights(flight_id):
    with open('flights.csv') as file:
        file_reader = csv.reader(file)
        for row in file_reader:
            if row[0] == flight_id:
                data = {
                    'ArrivalTime': row[6],
                    'DepartureTime': row[4],
                    'Number': row[7]
                }
                return json.dumps(data)
        return "<h3>Sorry, try another id flight<h3>"


if __name__ == '__main__':
    app.run()
