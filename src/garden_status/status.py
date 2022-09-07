from enum import Enum

class Status(Enum):
    MANUAL = "MANUAL"
    AUTO = "AUTO"
    ALARM = "ALARM"

    switcher = {
        "MANUAL": Status.MANUAL,
        "AUTO": Status.AUTO,
        "ALARM": Status.ALARM
    }

    @staticmethod
    def fromString(status):
        return switcher[status]

    def toString(self):
        return self.value


class IrrigatorStatus(ENUM):
    READY = "READY"
    OPEN = "OPEN"
    CLOSED = "CLOSED"

    switcher = {
        "READY": IrrigatorStatus.READY,
        "OPEN": IrrigatorStatus.OPEN,
        "CLOSED": IrrigatorStatus.CLOSED
    }

    @staticmethod
    def fromString(status):
        return switcher[status]
    
    def toString(self):
        return self.value