# SolarEdge Local

The goal if this respository is to provide information about using the local API available on some solar edge inverters.  This is a WIP based on my observations and may contain inaccuracies.  Pull Requests or Issues are encouraged to correct any mistakes or add additonal informatoin.

### Relevant Models

The local API is available on the [SExxxxH-US models with SetApp](https://www.solaredge.com/sites/default/files/se-hd-wave-single-phase-inverter-with-setapp-datasheet-na.pdf) as well as European three phase inverters SEXXK-XXXTXBXX4 models with SetApp like [SE3K-E10K](https://www.solaredge.com/sites/default/files/se-three-phase-inverter-setapp-ds.pdf), [SE12.5K-SE27.6K](https://www.solaredge.com/sites/default/files/se-three-phase-inverter-setapp-datasheet.pdf) and [SE33.3K](https://www.solaredge.com/sites/default/files/se-three-phase-inverter-for-277-480-grid-setapp-datasheet.pdf). Same goes for Australian inverters [SE2500H->SE10000H](https://www.solaredge.com/sites/default/files/se-single-phase-HD-wave-inverter-setapp-datasheet-aus.pdf). 
Please check carefully the datasheets if in the section "Additional Features", sub-section "Inverter Commissioning" is present the following line "With the SetApp mobile application using built-in Wi-Fi access point for local connection".

More inforation on SetApp could be found [here](https://www.solaredge.com/us/products/installer-tools/setapp). These models have no LED screen and are provisioned ONLY via a phone app during commissioning.
Check also the [SetApp FAQ](https://www.solaredge.com/sites/default/files/solaredge-setapp-faqs-eng.pdf) for more info.
For convenience it is reported here one Q&A:

> Q: Can the new app be used for already installed inverters?
>
> A: Only SolarEdge inverters with a new communication board (no display) can be activated or configured via SetApp.

Reportedly, these new inverters have a CPU number starting with 04.

You can check by finding the IP address of your inverter and visiting it in a browser.  If it supports the local API, you'll see the SolarEdge logo and a "Commissioning" menu.

If you do not have the local API available, see [this repository](https://github.com/jbuehl/solaredge) as an alternative.

### Using the Python wrapper

For convinience, a python API wrapper, [solaredge_local](https://pypi.org/project/solaredge-local/) is available.  **Only python 3 is supported**

To install: `pip install solaredge-local`

To use:

```
from solaredge_local import SolarEdge
client = SolarEdge("http://<inverter ip address>")
client.get_status()  # Provides general energy and other overview information
client.get_maintenance() # Provides optimizer level information and other details
client.get_information() # Provides software versions and error log list.
client.get_power_control() # Provides power control information and other details.
```

### API Endpoints

* AppConfigs: "web/v1/app_configs"
* Region: "web/v1/region"
* Region_Country: "web/v1/region/country"
* Region_Language: "web/v1/region/language"
* Pairing: "web/v1/pairing"
* Pairing_Request: "web/v1/pairing/request"
* Communication: "web/v1/communication"
* Communication_Server: "web/v1/communication/server"
* Communication_Lan: "web/v1/communication/lan"
* Communication_Rs485_SlaveDetect: "web/v1/communication/rs485/<id>/slave_detect"
* Communication_Rs485_Protocol: "web/v1/communication/rs485/<id>/protocol"
* Communication_Rs485_DeviceId: "web/v1/communication/rs485/<id>/deviceid"
* Communication_Rs485_Modbus: "web/v1/communication/rs485/<id>/modbus"
* Communication_Rs485_Modbus_AddDevice: "web/v1/communication/rs485/<id>/modbus/add_device"
* Communication_Rs485_Modbus_RemoveDevice: "web/v1/communication/rs485/<id>/modbus/remove_device"
* Communication_Wifi: "web/v1/communication/wifi"
* Communication_Wifi_Wps: "web/v1/communication/wifi/wps"
* Communication_Wifi_Connect: "web/v1/communication/wifi/connect"
* Communication_Cellular: "web/v1/communication/cellular"
* Communication_Zigbee_Defaults: "web/v1/communication/zigbee/defaults"
* Communication_Zigbee_ModuleConfigs: "web/v1/communication/zigbee/module_configs"
* Communication_Zigbee_OpMode: "web/v1/communication/zigbee/op_mode"
* Communication_Gpio_Pri: "web/v1/communication/gpio/pri"
* Communication_ModbusTcp: "web/v1/communication/modbus_tcp"
* PowerControl: "web/v1/power_control"
* PowerControl_GridControl: "web/v1/power_control/grid_control"
* PowerControl_EnergyManager_LimitControl: "web/v1/power_control/energy_manager/limit_control"
* PowerControl_EnergyManager_EnergyControl: "web/v1/power_control/energy_manager/energy_control"
* PowerControl_EnergyManager_StorageControl: "web/v1/power_control/energy_manager/storage_control"
* PowerControl_ReactivePower: "web/v1/power_control/reactive_power"
* PowerControl_ActivePower: "web/v1/power_control/active_power"
* PowerControl_Wakeup: "web/v1/power_control/wakeup"
* PowerControl_Advanced: "web/v1/power_control/advanced"
* PowerControl_Reset: "web/v1/power_control/reset"
* PowerControl_Rrcr: "web/v1/power_control/rrcr"
* Maintenance: "web/v1/maintenance"
* Maintenance_DateTime: "web/v1/maintenance/date_and_time"
* Maintenance_ResetCounters: "web/v1/maintenance/reset_counters"
* Maintenance_ResetFactory: "web/v1/maintenance/reset_factory"
* Maintenance_Afci: "web/v1/maintenance/afci"
* Maintenance_AfciTest: "web/v1/maintenance/afci/test"
* Maintenance_Inverters_SelfTest: "web/v1/maintenance/inverters/<position>/self_test"
* Maintenance_Standby: "web/v1/maintenance/standby"
* Maintenance_GridProtectionLogin: "web/v1/maintenance/grid_protection/login"
* Maintenance_GridProtection: "web/v1/maintenance/grid_protection"
* Maintenance_UpgradeUsb: "web/v1/maintenance/fw_upgrade/usb"
* Information: "web/v1/information"
* Status: "web/v1/status"
* Status_ServerCommTest: "web/v1/status/server_comm_test"

The Status endpoint appears to the most useful for realtime production data.
Optimizer level data is available from the maintenance API endpoint.


## Using the API

All endpoints I have explored so far appear to be a GET, and responses use [Protocol Buffers](https://developers.google.com/protocol-buffers/).  There is no authentication

### View Raw Response

You can see the raw data by doing the following (assuming you have the protoocal buffers CLI tool installed)

```
curl -s http://<inverter ip>/web/v1/status | protoc --decode_raw
```

Many numbers appear to be 32 bit floating point.

The proto definitions required to fully parse the responses are available in  javascript if you choose "view source" in the developer tools of your browser.

### View Parsed response

If there is a corresponding `.proto` file in [message_types](/message_types), you can view the parsed response from the API.  Each proto file correspond to the name of an API endpoint. These are very much a WIP and may be incomplete.  These can be created by choosing "view source" in the developer tools of your browser, and searching for text like `proto.web_status.<apiNameInCamelCase>.toObject`

Here is an example for the status API:

```
curl -s http://<inverter ip>/web/v1/status | protoc --decode Status message_types/status.proto
```

### Updating Protocol Buffer response

To add or change the Protocol Buffer defintions, please do the following

1. Manually change the `message_types/*.proto` files as required
2. Test the file using `curl` as described in [View Parsed Response](#view-parsed-response)
3. Update the generated `*_pb2.py` files for each file changed by running a command like:

    ```
    protoc -I=message_types --python_out=solaredge_local message_types/<filename_changed>.proto
    ```
4. Commit the generated updates
