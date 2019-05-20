from uplink import Consumer, get
from .maintenance_pb2 import Maintenance
from .status_pb2 import Status
from .information_pb2 import Information
from .powercontrol_pb2 import PowerControl

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

    @get("/web/v1/power_control")
    def get_power_control(self) -> PowerControl:
        pass