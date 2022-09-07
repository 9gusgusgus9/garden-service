from garden_status.status import GardenStatus, IrrigatorStatus, LedStatus

class Manifest:

    def __init__(self):

        # Garden Status
        self.gardenStatus = GardenStatus.AUTO

        # SensorBoard status
        self.sensorboardLed = LedStatus.ON
        self.temperature = 0
        self.luminosity = 0

        # Controller Status
        self.irrigatorStatus = IrrigatorStatus.READY
        self.controllerLed1 = LedStatus.OFF
        self.controllerLed2 = LedStatus.OFF
        self.controllerLed3 = LedStatus.OFF
        self.controllerLed4 = LedStatus.OFF

    def getGardenStatus(self):
        return self.gardenStatus

    def setGardenStatus(self, status):
        self.gardenStatus = status

    def getIrrigatorStatus(self):
        return self.irrigatorStatus

    def setIrrigatorStatus(self, status):
        self.irrigatorStatus = status
        #Bisogna importarela velocita dell'irrigatore
    
    def getSensorboardLed(self):
        return self.sensorboardLed

    def setSensorboardLed(self, status):
        self.sensorboardLed = status

    def setControllerLedOn(self, value):
        self.controllerLed1 = LedStatus.ON
        self.controllerLed2 = LedStatus.ON
        self.controllerLed3 = LedStatus.ON
        self.controllerLed4 = LedStatus.ON
        #bisogna impostare i valori di led 3 e 4

    def setControllerLedOff(self):
        self.controllerLed1 = LedStatus.OFF
        self.controllerLed2 = LedStatus.OFF
        self.controllerLed3 = LedStatus.OFF
        self.controllerLed4 = LedStatus.OFF

    def getTemperature(self):
        return self.temperature

    def getLuminosity(self):
        return self.luminosity

    def setTemperature(self, temperature):
        self.temperature = temperature

        #Sarebbe meglio spostare i controlli su server.py
        if self.temperature > 5 and slef.getIrrigatorStatus != IrrigatorStatus.OPEN:
            self.setGardenStatus(GardenStatus.ALARM)
            self.setSensorboardLed(LedStatus.OFF)
    
    def setLuminosity(self, luminosity):
        self.luminosity = luminosity

        #sarebbe meglio spostare i controlli su server.py
        if self.luminosity < 5:
            self.setControllerLedOn(luminosity)
            if self.luminosity < 2:
                self.setIrrigatorStatus(IrrigatorStatus.OPEN)
            else:
                self.setIrrigatorStatus(IrrigatorStatus.CLOSED)
        else: 
            self.setControllerLedOff()
            self.setIrrigatorStatus(IrrigatorStatus.CLOSED)