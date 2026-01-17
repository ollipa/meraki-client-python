"""Batch API endpoints."""

from meraki_client.api.batch.appliance import ActionBatchAppliance
from meraki_client.api.batch.camera import ActionBatchCamera
from meraki_client.api.batch.campus_gateway import ActionBatchCampusGateway
from meraki_client.api.batch.cellular_gateway import ActionBatchCellularGateway
from meraki_client.api.batch.devices import ActionBatchDevices
from meraki_client.api.batch.insight import ActionBatchInsight
from meraki_client.api.batch.nac import ActionBatchNac
from meraki_client.api.batch.networks import ActionBatchNetworks
from meraki_client.api.batch.organizations import ActionBatchOrganizations
from meraki_client.api.batch.sensor import ActionBatchSensor
from meraki_client.api.batch.sm import ActionBatchSm
from meraki_client.api.batch.spaces import ActionBatchSpaces
from meraki_client.api.batch.switch import ActionBatchSwitch
from meraki_client.api.batch.wireless import ActionBatchWireless


class Batch:
    """Batch class."""

    def __init__(self) -> None:
        self.appliance = ActionBatchAppliance()
        self.camera = ActionBatchCamera()
        self.campus_gateway = ActionBatchCampusGateway()
        self.cellular_gateway = ActionBatchCellularGateway()
        self.devices = ActionBatchDevices()
        self.insight = ActionBatchInsight()
        self.nac = ActionBatchNac()
        self.networks = ActionBatchNetworks()
        self.organizations = ActionBatchOrganizations()
        self.sensor = ActionBatchSensor()
        self.sm = ActionBatchSm()
        self.spaces = ActionBatchSpaces()
        self.switch = ActionBatchSwitch()
        self.wireless = ActionBatchWireless()
