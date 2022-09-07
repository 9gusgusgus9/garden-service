from flask import Flask, request
from manifest import Manifest
from status import GardenStatus, IrrigatorStatus

app = Flask(__name__)


@app.route('/data', methods=['POST'])
def getData():
   temperature = request.json["temperature"]
   manifest.setTemperature(temperature)
   luminosity = request.json["luminosity"]
   manifest.setLuminosity(luminosity)
   #print("Temperature: " + temperature + " Luminosity: " + luminosity)
   return manifest.getGardenStatus().toString()

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000)
   manifest = Manifest()
   