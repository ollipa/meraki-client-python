"""Batch API endpoints."""

from meraki_dashboard_sdk.api.batch.appliance import ActionBatchAppliance
from meraki_dashboard_sdk.api.batch.camera import ActionBatchCamera
from meraki_dashboard_sdk.api.batch.cellularGateway import ActionBatchCellularGateway
from meraki_dashboard_sdk.api.batch.devices import ActionBatchDevices
from meraki_dashboard_sdk.api.batch.insight import ActionBatchInsight
from meraki_dashboard_sdk.api.batch.networks import ActionBatchNetworks
from meraki_dashboard_sdk.api.batch.organizations import ActionBatchOrganizations
from meraki_dashboard_sdk.api.batch.sensor import ActionBatchSensor
from meraki_dashboard_sdk.api.batch.sm import ActionBatchSm
from meraki_dashboard_sdk.api.batch.switch import ActionBatchSwitch
from meraki_dashboard_sdk.api.batch.wireless import ActionBatchWireless


class Batch:
    """Batch class."""

    def __init__(self) -> None:
        # Action Batch helper API endpoints by section
        self.organizations = ActionBatchOrganizations()
        self.networks = ActionBatchNetworks()
        self.devices = ActionBatchDevices()
        self.appliance = ActionBatchAppliance()
        self.camera = ActionBatchCamera()
        self.cellularGateway = ActionBatchCellularGateway()
        self.insight = ActionBatchInsight()
        self.sensor = ActionBatchSensor()
        self.sm = ActionBatchSm()
        self.switch = ActionBatchSwitch()
        self.wireless = ActionBatchWireless()
