from uplink import Consumer, get
from .maintenance_pb2 import Maintenance
from .status_pb2 import Status
from .information_pb2 import Information

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

    @get("/web/v1/information")
    def get_information(self) -> Information:
        pass
