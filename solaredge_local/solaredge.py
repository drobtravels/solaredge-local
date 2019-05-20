from uplink import Consumer, get
from .maintenance_pb2 import Maintenance
from .status_pb2 import Status

class SolarEdge(Consumer):
    @get("/web/v1/status")
    def get_status(self) -> Status:
        pass

    @get("/web/v1/maintenance")
    def get_optimizers(self) -> Maintenance:
        pass

    @get("/web/v1/maintenance")
    def get_maintenance(self) -> Maintenance:
        pass
