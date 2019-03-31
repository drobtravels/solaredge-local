from uplink import Consumer, get
from .maintenance_pb2 import Maintenance
from .status_pb2 import Status

class SolarEdge(Consumer):
    @get("/web/v1/status")
    def get_status(self) -> Status:
        pass

    @get("/maintenance")
    def get_optomizers(self):
        pass
