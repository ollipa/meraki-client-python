"""Camera API endpoints."""

import urllib
from collections.abc import Generator
from typing import Any

from meraki_dashboard_sdk.aio.rest_session import AsyncRestSession


class AsyncCamera:
    """Camera class."""

    def __init__(self, session: AsyncRestSession) -> None:
        super().__init__()
        self._session = session

    def get_device_camera_analytics_live(self, *, serial: str) -> dict[str, Any] | None:
        """Returns live state from camera analytics zones.

        https://developer.cisco.com/meraki/api-v1/#!get-device-camera-analytics-live

        Args:
            serial: Serial.

        """
        metadata = {
            "tags": ["camera", "monitor", "analytics", "live"],
            "operation": "get_device_camera_analytics_live",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/camera/analytics/live"

        return self._session.get(metadata, resource)

    def get_device_camera_analytics_overview(
        self,
        *,
        serial: str,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        object_type: str | None = None,
    ) -> dict[str, Any] | None:
        """Returns an overview of aggregate analytics data for a timespan.

        https://developer.cisco.com/meraki/api-v1/#!get-device-camera-analytics-overview

        Args:
            serial: Serial.
            t0: The beginning of the timespan for the data. The maximum lookback period is 365 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 7 days. The default is 1 hour.
            object_type: [optional] The object type for which analytics will be retrieved. The
              default object type is person. The available types are [person, vehicle].

        """
        if object_type is not None:
            options = ["person", "vehicle"]
            assert object_type in options, (
                f'"object_type" cannot be "{object_type}", & must be set to one of: {options}'
            )

        metadata = {
            "tags": ["camera", "monitor", "analytics", "overview"],
            "operation": "get_device_camera_analytics_overview",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/camera/analytics/overview"

        params = {}
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan
        if object_type is not None:
            params["objectType"] = object_type

        return self._session.get(metadata, resource, params)

    def get_device_camera_analytics_recent(
        self, *, serial: str, object_type: str | None = None
    ) -> dict[str, Any] | None:
        """Returns most recent record for analytics zones.

        https://developer.cisco.com/meraki/api-v1/#!get-device-camera-analytics-recent

        Args:
            serial: Serial.
            object_type: [optional] The object type for which analytics will be retrieved. The
              default object type is person. The available types are [person, vehicle].

        """
        if object_type is not None:
            options = ["person", "vehicle"]
            assert object_type in options, (
                f'"object_type" cannot be "{object_type}", & must be set to one of: {options}'
            )

        metadata = {
            "tags": ["camera", "monitor", "analytics", "recent"],
            "operation": "get_device_camera_analytics_recent",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/camera/analytics/recent"

        params = {}
        if object_type is not None:
            params["objectType"] = object_type

        return self._session.get(metadata, resource, params)

    def get_device_camera_analytics_zones(self, *, serial: str) -> dict[str, Any] | None:
        """Returns all configured analytic zones for this camera.

        https://developer.cisco.com/meraki/api-v1/#!get-device-camera-analytics-zones

        Args:
            serial: Serial.

        """
        metadata = {
            "tags": ["camera", "monitor", "analytics", "zones"],
            "operation": "get_device_camera_analytics_zones",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/camera/analytics/zones"

        return self._session.get(metadata, resource)

    def get_device_camera_analytics_zone_history(
        self,
        *,
        serial: str,
        zone_id: str,
        t0: str | None = None,
        t1: str | None = None,
        timespan: float | None = None,
        resolution: int | None = None,
        object_type: str | None = None,
    ) -> dict[str, Any] | None:
        """Return historical records for analytic zones.

        https://developer.cisco.com/meraki/api-v1/#!get-device-camera-analytics-zone-history

        Args:
            serial: Serial.
            zone_id: Zone ID.
            t0: The beginning of the timespan for the data. The maximum lookback period is 365 days
              from today.
            t1: The end of the timespan for the data. t1 can be a maximum of 14 hours after t0.
            timespan: The timespan for which the information will be fetched. If specifying
              timespan, do not specify parameters t0 and t1. The value must be in
              seconds and be less than or equal to 14 hours. The default is 1 hour.
            resolution: The time resolution in seconds for returned data. The valid resolutions are:
              60. The default is 60.
            object_type: [optional] The object type for which analytics will be retrieved. The
              default object type is person. The available types are [person, vehicle].

        """
        if object_type is not None:
            options = ["person", "vehicle"]
            assert object_type in options, (
                f'"object_type" cannot be "{object_type}", & must be set to one of: {options}'
            )

        metadata = {
            "tags": ["camera", "monitor", "analytics", "zones", "history"],
            "operation": "get_device_camera_analytics_zone_history",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        zone_id = urllib.parse.quote(str(zone_id), safe="")
        resource = f"/devices/{serial}/camera/analytics/zones/{zone_id}/history"

        params = {}
        if t0 is not None:
            params["t0"] = t0
        if t1 is not None:
            params["t1"] = t1
        if timespan is not None:
            params["timespan"] = timespan
        if resolution is not None:
            params["resolution"] = resolution
        if object_type is not None:
            params["objectType"] = object_type

        return self._session.get(metadata, resource, params)

    def get_device_camera_custom_analytics(self, *, serial: str) -> dict[str, Any] | None:
        """Return custom analytics settings for a camera.

        https://developer.cisco.com/meraki/api-v1/#!get-device-camera-custom-analytics

        Args:
            serial: Serial.

        """
        metadata = {
            "tags": ["camera", "configure", "customAnalytics"],
            "operation": "get_device_camera_custom_analytics",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/camera/customAnalytics"

        return self._session.get(metadata, resource)

    def update_device_camera_custom_analytics(
        self,
        *,
        serial: str,
        enabled: bool | None = None,
        artifact_id: str | None = None,
        parameters: list | None = None,
    ) -> dict[str, Any] | None:
        """Update custom analytics settings for a camera.

        https://developer.cisco.com/meraki/api-v1/#!update-device-camera-custom-analytics

        Args:
            serial: Serial.
            enabled: Enable custom analytics.
            artifact_id: The ID of the custom analytics artifact.
            parameters: Parameters for the custom analytics workload.

        """
        metadata = {
            "tags": ["camera", "configure", "customAnalytics"],
            "operation": "update_device_camera_custom_analytics",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/camera/customAnalytics"

        payload = {}
        if enabled is not None:
            payload["enabled"] = enabled
        if artifact_id is not None:
            payload["artifactId"] = artifact_id
        if parameters is not None:
            payload["parameters"] = parameters

        return self._session.put(metadata, resource, payload)

    def generate_device_camera_snapshot(
        self, *, serial: str, timestamp: str | None = None, fullframe: bool | None = None
    ) -> dict[str, Any] | None:
        """Generate a snapshot of what the camera sees at the specified time and return a link to that image.

        https://developer.cisco.com/meraki/api-v1/#!generate-device-camera-snapshot

        Args:
            serial: Serial.
            timestamp: [optional] The snapshot will be taken from this time on the camera. The
              timestamp is expected to be in ISO 8601 format. If no timestamp is
              specified, we will assume current time.
            fullframe: [optional] If set to "true" the snapshot will be taken at full sensor
              resolution. This will error if used with timestamp.

        """
        metadata = {"tags": ["camera", "monitor"], "operation": "generate_device_camera_snapshot"}
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/camera/generateSnapshot"

        payload = {}
        if timestamp is not None:
            payload["timestamp"] = timestamp
        if fullframe is not None:
            payload["fullframe"] = fullframe

        return self._session.post(metadata, resource, payload)

    def get_device_camera_quality_and_retention(self, *, serial: str) -> dict[str, Any] | None:
        """Returns quality and retention settings for the given camera.

        https://developer.cisco.com/meraki/api-v1/#!get-device-camera-quality-and-retention

        Args:
            serial: Serial.

        """
        metadata = {
            "tags": ["camera", "configure", "qualityAndRetention"],
            "operation": "get_device_camera_quality_and_retention",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/camera/qualityAndRetention"

        return self._session.get(metadata, resource)

    def update_device_camera_quality_and_retention(
        self,
        *,
        serial: str,
        profile_id: str | None = None,
        motion_based_retention_enabled: bool | None = None,
        audio_recording_enabled: bool | None = None,
        restricted_bandwidth_mode_enabled: bool | None = None,
        quality: str | None = None,
        resolution: str | None = None,
        motion_detector_version: int | None = None,
    ) -> dict[str, Any] | None:
        """Update quality and retention settings for the given camera.

        https://developer.cisco.com/meraki/api-v1/#!update-device-camera-quality-and-retention

        Args:
            serial: Serial.
            profile_id: The ID of a quality and retention profile to assign to the camera. The
              profile's settings will override all of the per-camera quality and
              retention settings. If the value of this parameter is null, any existing
              profile will be unassigned from the camera.
            motion_based_retention_enabled: Boolean indicating if motion-based retention is
              enabled(true) or disabled(false) on the camera.
            audio_recording_enabled: Boolean indicating if audio recording is enabled(true) or
              disabled(false) on the camera.
            restricted_bandwidth_mode_enabled: Boolean indicating if restricted bandwidth is
              enabled(true) or disabled(false) on the camera. This setting does not
              apply to MV2 cameras.
            quality: Quality of the camera. Can be one of 'Standard', 'High', 'Enhanced' or 'Ultra'.
              Not all qualities are supported by every camera model.
            resolution: Resolution of the camera. Can be one of '1280x720', '1920x1080',
              '1080x1080', '2112x2112', '2880x2880', '2688x1512' or '3840x2160'.Not all
              resolutions are supported by every camera model.
            motion_detector_version: The version of the motion detector that will be used by the
              camera. Only applies to Gen 2 cameras. Defaults to v2.

        """
        if quality is not None:
            options = ["Enhanced", "High", "Standard", "Ultra"]
            assert quality in options, (
                f'"quality" cannot be "{quality}", & must be set to one of: {options}'
            )
        if resolution is not None:
            options = [
                "1080x1080",
                "1280x720",
                "1920x1080",
                "2112x2112",
                "2688x1512",
                "2880x2880",
                "3840x2160",
            ]
            assert resolution in options, (
                f'"resolution" cannot be "{resolution}", & must be set to one of: {options}'
            )
        if motion_detector_version is not None:
            options = [1, 2]
            assert motion_detector_version in options, (
                f'"motion_detector_version" cannot be "{motion_detector_version}", & must be set to one of: {options}'
            )

        metadata = {
            "tags": ["camera", "configure", "qualityAndRetention"],
            "operation": "update_device_camera_quality_and_retention",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/camera/qualityAndRetention"

        payload = {}
        if profile_id is not None:
            payload["profileId"] = profile_id
        if motion_based_retention_enabled is not None:
            payload["motionBasedRetentionEnabled"] = motion_based_retention_enabled
        if audio_recording_enabled is not None:
            payload["audioRecordingEnabled"] = audio_recording_enabled
        if restricted_bandwidth_mode_enabled is not None:
            payload["restrictedBandwidthModeEnabled"] = restricted_bandwidth_mode_enabled
        if quality is not None:
            payload["quality"] = quality
        if resolution is not None:
            payload["resolution"] = resolution
        if motion_detector_version is not None:
            payload["motionDetectorVersion"] = motion_detector_version

        return self._session.put(metadata, resource, payload)

    def get_device_camera_sense(self, *, serial: str) -> dict[str, Any] | None:
        """Returns sense settings for a given camera.

        https://developer.cisco.com/meraki/api-v1/#!get-device-camera-sense

        Args:
            serial: Serial.

        """
        metadata = {
            "tags": ["camera", "configure", "sense"],
            "operation": "get_device_camera_sense",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/camera/sense"

        return self._session.get(metadata, resource)

    def update_device_camera_sense(
        self,
        *,
        serial: str,
        sense_enabled: bool | None = None,
        mqtt_broker_id: str | None = None,
        audio_detection: dict | None = None,
        detection_model_id: str | None = None,
    ) -> dict[str, Any] | None:
        """Update sense settings for the given camera.

        https://developer.cisco.com/meraki/api-v1/#!update-device-camera-sense

        Args:
            serial: Serial.
            sense_enabled: Boolean indicating if sense(license) is enabled(true) or disabled(false)
              on the camera.
            mqtt_broker_id: The ID of the MQTT broker to be enabled on the camera. A value of null
              will disable MQTT on the camera.
            audio_detection: The details of the audio detection config.
            detection_model_id: The ID of the object detection model.

        """
        metadata = {
            "tags": ["camera", "configure", "sense"],
            "operation": "update_device_camera_sense",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/camera/sense"

        payload = {}
        if sense_enabled is not None:
            payload["senseEnabled"] = sense_enabled
        if mqtt_broker_id is not None:
            payload["mqttBrokerId"] = mqtt_broker_id
        if audio_detection is not None:
            payload["audioDetection"] = audio_detection
        if detection_model_id is not None:
            payload["detectionModelId"] = detection_model_id

        return self._session.put(metadata, resource, payload)

    def get_device_camera_sense_object_detection_models(
        self, *, serial: str
    ) -> dict[str, Any] | None:
        """Returns the MV Sense object detection model list for the given camera.

        https://developer.cisco.com/meraki/api-v1/#!get-device-camera-sense-object-detection-models

        Args:
            serial: Serial.

        """
        metadata = {
            "tags": ["camera", "configure", "sense", "objectDetectionModels"],
            "operation": "get_device_camera_sense_object_detection_models",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/camera/sense/objectDetectionModels"

        return self._session.get(metadata, resource)

    def get_device_camera_video_settings(self, *, serial: str) -> dict[str, Any] | None:
        """Returns video settings for the given camera.

        https://developer.cisco.com/meraki/api-v1/#!get-device-camera-video-settings

        Args:
            serial: Serial.

        """
        metadata = {
            "tags": ["camera", "configure", "video", "settings"],
            "operation": "get_device_camera_video_settings",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/camera/video/settings"

        return self._session.get(metadata, resource)

    def update_device_camera_video_settings(
        self, *, serial: str, external_rtsp_enabled: bool | None = None
    ) -> dict[str, Any] | None:
        """Update video settings for the given camera.

        https://developer.cisco.com/meraki/api-v1/#!update-device-camera-video-settings

        Args:
            serial: Serial.
            external_rtsp_enabled: Boolean indicating if external rtsp stream is exposed.

        """
        metadata = {
            "tags": ["camera", "configure", "video", "settings"],
            "operation": "update_device_camera_video_settings",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/camera/video/settings"

        payload = {}
        if external_rtsp_enabled is not None:
            payload["externalRtspEnabled"] = external_rtsp_enabled

        return self._session.put(metadata, resource, payload)

    def get_device_camera_video_link(
        self, *, serial: str, timestamp: str | None = None
    ) -> dict[str, Any] | None:
        """Returns video link to the specified camera.

        https://developer.cisco.com/meraki/api-v1/#!get-device-camera-video-link

        Args:
            serial: Serial.
            timestamp: [optional] The video link will start at this time. The timestamp should be a
              string in ISO8601 format. If no timestamp is specified, we will assume
              current time.

        """
        metadata = {
            "tags": ["camera", "configure", "videoLink"],
            "operation": "get_device_camera_video_link",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/camera/videoLink"

        params = {}
        if timestamp is not None:
            params["timestamp"] = timestamp

        return self._session.get(metadata, resource, params)

    def get_device_camera_wireless_profiles(self, *, serial: str) -> dict[str, Any] | None:
        """Returns wireless profile assigned to the given camera.

        https://developer.cisco.com/meraki/api-v1/#!get-device-camera-wireless-profiles

        Args:
            serial: Serial.

        """
        metadata = {
            "tags": ["camera", "configure", "wirelessProfiles"],
            "operation": "get_device_camera_wireless_profiles",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/camera/wirelessProfiles"

        return self._session.get(metadata, resource)

    def update_device_camera_wireless_profiles(
        self, *, serial: str, ids: dict
    ) -> dict[str, Any] | None:
        """Assign wireless profiles to the given camera.

        https://developer.cisco.com/meraki/api-v1/#!update-device-camera-wireless-profiles

        Args:
            serial: Serial.
            ids: The ids of the wireless profile to assign to the given camera.

        """
        metadata = {
            "tags": ["camera", "configure", "wirelessProfiles"],
            "operation": "update_device_camera_wireless_profiles",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/camera/wirelessProfiles"

        payload = {}
        if ids is not None:
            payload["ids"] = ids

        return self._session.put(metadata, resource, payload)

    def get_network_camera_quality_retention_profiles(
        self, *, network_id: str
    ) -> dict[str, Any] | None:
        """List the quality retention profiles for this network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-camera-quality-retention-profiles

        Args:
            network_id: Network ID.

        """
        metadata = {
            "tags": ["camera", "configure", "qualityRetentionProfiles"],
            "operation": "get_network_camera_quality_retention_profiles",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/camera/qualityRetentionProfiles"

        return self._session.get(metadata, resource)

    def create_network_camera_quality_retention_profile(
        self,
        *,
        network_id: str,
        name: str,
        motion_based_retention_enabled: bool | None = None,
        restricted_bandwidth_mode_enabled: bool | None = None,
        audio_recording_enabled: bool | None = None,
        cloud_archive_enabled: bool | None = None,
        motion_detector_version: int | None = None,
        smart_retention: dict | None = None,
        schedule_id: str | None = None,
        max_retention_days: int | None = None,
        video_settings: dict | None = None,
    ) -> dict[str, Any] | None:
        """Creates new quality retention profile for this network.

        https://developer.cisco.com/meraki/api-v1/#!create-network-camera-quality-retention-profile

        Args:
            network_id: Network ID.
            name: The name of the new profile. Must be unique. This parameter is required.
            motion_based_retention_enabled: Deletes footage older than 3 days in which no motion was
              detected. Can be either true or false. Defaults to false. This setting
              does not apply to MV2 cameras.
            restricted_bandwidth_mode_enabled: Disable features that require additional bandwidth
              such as Motion Recap. Can be either true or false. Defaults to false. This
              setting does not apply to MV2 cameras.
            audio_recording_enabled: Whether or not to record audio. Can be either true or false.
              Defaults to false.
            cloud_archive_enabled: Create redundant video backup using Cloud Archive. Can be either
              true or false. Defaults to false.
            motion_detector_version: The version of the motion detector that will be used by the
              camera. Only applies to Gen 2 cameras. Defaults to v2.
            smart_retention: Smart Retention records footage in two qualities and intelligently
              retains higher quality when motion, people or vehicles are detected.
            schedule_id: Schedule for which this camera will record video, or 'null' to always
              record.
            max_retention_days: The maximum number of days for which the data will be stored, or
              'null' to keep data until storage space runs out. If the former, it can be
              in the range of one to ninety days.
            video_settings: Video quality and resolution settings for all the camera models.

        """
        metadata = {
            "tags": ["camera", "configure", "qualityRetentionProfiles"],
            "operation": "create_network_camera_quality_retention_profile",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/camera/qualityRetentionProfiles"

        payload = {}
        if name is not None:
            payload["name"] = name
        if motion_based_retention_enabled is not None:
            payload["motionBasedRetentionEnabled"] = motion_based_retention_enabled
        if restricted_bandwidth_mode_enabled is not None:
            payload["restrictedBandwidthModeEnabled"] = restricted_bandwidth_mode_enabled
        if audio_recording_enabled is not None:
            payload["audioRecordingEnabled"] = audio_recording_enabled
        if cloud_archive_enabled is not None:
            payload["cloudArchiveEnabled"] = cloud_archive_enabled
        if motion_detector_version is not None:
            payload["motionDetectorVersion"] = motion_detector_version
        if smart_retention is not None:
            payload["smartRetention"] = smart_retention
        if schedule_id is not None:
            payload["scheduleId"] = schedule_id
        if max_retention_days is not None:
            payload["maxRetentionDays"] = max_retention_days
        if video_settings is not None:
            payload["videoSettings"] = video_settings

        return self._session.post(metadata, resource, payload)

    def get_network_camera_quality_retention_profile(
        self, *, network_id: str, quality_retention_profile_id: str
    ) -> dict[str, Any] | None:
        """Retrieve a single quality retention profile.

        https://developer.cisco.com/meraki/api-v1/#!get-network-camera-quality-retention-profile

        Args:
            network_id: Network ID.
            quality_retention_profile_id: Quality retention profile ID.

        """
        metadata = {
            "tags": ["camera", "configure", "qualityRetentionProfiles"],
            "operation": "get_network_camera_quality_retention_profile",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        quality_retention_profile_id = urllib.parse.quote(
            str(quality_retention_profile_id), safe=""
        )
        resource = (
            f"/networks/{network_id}/camera/qualityRetentionProfiles/{quality_retention_profile_id}"
        )

        return self._session.get(metadata, resource)

    def update_network_camera_quality_retention_profile(
        self,
        *,
        network_id: str,
        quality_retention_profile_id: str,
        name: str | None = None,
        motion_based_retention_enabled: bool | None = None,
        restricted_bandwidth_mode_enabled: bool | None = None,
        audio_recording_enabled: bool | None = None,
        cloud_archive_enabled: bool | None = None,
        motion_detector_version: int | None = None,
        smart_retention: dict | None = None,
        schedule_id: str | None = None,
        max_retention_days: int | None = None,
        video_settings: dict | None = None,
    ) -> dict[str, Any] | None:
        """Update an existing quality retention profile for this network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-camera-quality-retention-profile

        Args:
            network_id: Network ID.
            quality_retention_profile_id: Quality retention profile ID.
            name: The name of the new profile. Must be unique.
            motion_based_retention_enabled: Deletes footage older than 3 days in which no motion was
              detected. Can be either true or false. Defaults to false. This setting
              does not apply to MV2 cameras.
            restricted_bandwidth_mode_enabled: Disable features that require additional bandwidth
              such as Motion Recap. Can be either true or false. Defaults to false. This
              setting does not apply to MV2 cameras.
            audio_recording_enabled: Whether or not to record audio. Can be either true or false.
              Defaults to false.
            cloud_archive_enabled: Create redundant video backup using Cloud Archive. Can be either
              true or false. Defaults to false.
            motion_detector_version: The version of the motion detector that will be used by the
              camera. Only applies to Gen 2 cameras. Defaults to v2.
            smart_retention: Smart Retention records footage in two qualities and intelligently
              retains higher quality when motion, people or vehicles are detected.
            schedule_id: Schedule for which this camera will record video, or 'null' to always
              record.
            max_retention_days: The maximum number of days for which the data will be stored, or
              'null' to keep data until storage space runs out. If the former, it can be
              in the range of one to ninety days.
            video_settings: Video quality and resolution settings for all the camera models.

        """
        metadata = {
            "tags": ["camera", "configure", "qualityRetentionProfiles"],
            "operation": "update_network_camera_quality_retention_profile",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        quality_retention_profile_id = urllib.parse.quote(
            str(quality_retention_profile_id), safe=""
        )
        resource = (
            f"/networks/{network_id}/camera/qualityRetentionProfiles/{quality_retention_profile_id}"
        )

        payload = {}
        if name is not None:
            payload["name"] = name
        if motion_based_retention_enabled is not None:
            payload["motionBasedRetentionEnabled"] = motion_based_retention_enabled
        if restricted_bandwidth_mode_enabled is not None:
            payload["restrictedBandwidthModeEnabled"] = restricted_bandwidth_mode_enabled
        if audio_recording_enabled is not None:
            payload["audioRecordingEnabled"] = audio_recording_enabled
        if cloud_archive_enabled is not None:
            payload["cloudArchiveEnabled"] = cloud_archive_enabled
        if motion_detector_version is not None:
            payload["motionDetectorVersion"] = motion_detector_version
        if smart_retention is not None:
            payload["smartRetention"] = smart_retention
        if schedule_id is not None:
            payload["scheduleId"] = schedule_id
        if max_retention_days is not None:
            payload["maxRetentionDays"] = max_retention_days
        if video_settings is not None:
            payload["videoSettings"] = video_settings

        return self._session.put(metadata, resource, payload)

    def delete_network_camera_quality_retention_profile(
        self, *, network_id: str, quality_retention_profile_id: str
    ) -> None:
        """Delete an existing quality retention profile for this network.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-camera-quality-retention-profile

        Args:
            network_id: Network ID.
            quality_retention_profile_id: Quality retention profile ID.

        """
        metadata = {
            "tags": ["camera", "configure", "qualityRetentionProfiles"],
            "operation": "delete_network_camera_quality_retention_profile",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        quality_retention_profile_id = urllib.parse.quote(
            str(quality_retention_profile_id), safe=""
        )
        resource = (
            f"/networks/{network_id}/camera/qualityRetentionProfiles/{quality_retention_profile_id}"
        )

        return self._session.delete(metadata, resource)

    def get_network_camera_schedules(self, *, network_id: str) -> dict[str, Any] | None:
        """Returns a list of all camera recording schedules.

        https://developer.cisco.com/meraki/api-v1/#!get-network-camera-schedules

        Args:
            network_id: Network ID.

        """
        metadata = {
            "tags": ["camera", "configure", "schedules"],
            "operation": "get_network_camera_schedules",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/camera/schedules"

        return self._session.get(metadata, resource)

    def get_network_camera_wireless_profiles(self, *, network_id: str) -> dict[str, Any] | None:
        """List the camera wireless profiles for this network.

        https://developer.cisco.com/meraki/api-v1/#!get-network-camera-wireless-profiles

        Args:
            network_id: Network ID.

        """
        metadata = {
            "tags": ["camera", "configure", "wirelessProfiles"],
            "operation": "get_network_camera_wireless_profiles",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/camera/wirelessProfiles"

        return self._session.get(metadata, resource)

    def create_network_camera_wireless_profile(
        self, *, network_id: str, name: str, ssid: dict, identity: dict | None = None
    ) -> dict[str, Any] | None:
        """Creates a new camera wireless profile for this network.

        https://developer.cisco.com/meraki/api-v1/#!create-network-camera-wireless-profile

        Args:
            network_id: Network ID.
            name: The name of the camera wireless profile. This parameter is required.
            ssid: The details of the SSID config.
            identity: The identity of the wireless profile. Required for creating wireless profiles
              in 8021x-radius auth mode.

        """
        metadata = {
            "tags": ["camera", "configure", "wirelessProfiles"],
            "operation": "create_network_camera_wireless_profile",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        resource = f"/networks/{network_id}/camera/wirelessProfiles"

        payload = {}
        if name is not None:
            payload["name"] = name
        if ssid is not None:
            payload["ssid"] = ssid
        if identity is not None:
            payload["identity"] = identity

        return self._session.post(metadata, resource, payload)

    def get_network_camera_wireless_profile(
        self, *, network_id: str, wireless_profile_id: str
    ) -> dict[str, Any] | None:
        """Retrieve a single camera wireless profile.

        https://developer.cisco.com/meraki/api-v1/#!get-network-camera-wireless-profile

        Args:
            network_id: Network ID.
            wireless_profile_id: Wireless profile ID.

        """
        metadata = {
            "tags": ["camera", "configure", "wirelessProfiles"],
            "operation": "get_network_camera_wireless_profile",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        wireless_profile_id = urllib.parse.quote(str(wireless_profile_id), safe="")
        resource = f"/networks/{network_id}/camera/wirelessProfiles/{wireless_profile_id}"

        return self._session.get(metadata, resource)

    def update_network_camera_wireless_profile(
        self,
        *,
        network_id: str,
        wireless_profile_id: str,
        name: str | None = None,
        ssid: dict | None = None,
        identity: dict | None = None,
    ) -> dict[str, Any] | None:
        """Update an existing camera wireless profile in this network.

        https://developer.cisco.com/meraki/api-v1/#!update-network-camera-wireless-profile

        Args:
            network_id: Network ID.
            wireless_profile_id: Wireless profile ID.
            name: The name of the camera wireless profile.
            ssid: The details of the SSID config.
            identity: The identity of the wireless profile. Required for creating wireless profiles
              in 8021x-radius auth mode.

        """
        metadata = {
            "tags": ["camera", "configure", "wirelessProfiles"],
            "operation": "update_network_camera_wireless_profile",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        wireless_profile_id = urllib.parse.quote(str(wireless_profile_id), safe="")
        resource = f"/networks/{network_id}/camera/wirelessProfiles/{wireless_profile_id}"

        payload = {}
        if name is not None:
            payload["name"] = name
        if ssid is not None:
            payload["ssid"] = ssid
        if identity is not None:
            payload["identity"] = identity

        return self._session.put(metadata, resource, payload)

    def delete_network_camera_wireless_profile(
        self, *, network_id: str, wireless_profile_id: str
    ) -> None:
        """Delete an existing camera wireless profile for this network.

        https://developer.cisco.com/meraki/api-v1/#!delete-network-camera-wireless-profile

        Args:
            network_id: Network ID.
            wireless_profile_id: Wireless profile ID.

        """
        metadata = {
            "tags": ["camera", "configure", "wirelessProfiles"],
            "operation": "delete_network_camera_wireless_profile",
        }
        network_id = urllib.parse.quote(str(network_id), safe="")
        wireless_profile_id = urllib.parse.quote(str(wireless_profile_id), safe="")
        resource = f"/networks/{network_id}/camera/wirelessProfiles/{wireless_profile_id}"

        return self._session.delete(metadata, resource)

    def get_organization_camera_boundaries_areas_by_device(
        self, *, organization_id: str, serials: list | None = None
    ) -> dict[str, Any] | None:
        """Returns all configured area boundaries of cameras.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-camera-boundaries-areas-by-device

        Args:
            organization_id: Organization ID.
            serials: A list of serial numbers. The returned cameras will be filtered to only include
              these serials.

        """
        metadata = {
            "tags": ["camera", "configure", "boundaries", "areas", "byDevice"],
            "operation": "get_organization_camera_boundaries_areas_by_device",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/camera/boundaries/areas/byDevice"

        params = {}
        if serials is not None:
            params["serials[]"] = serials

        return self._session.get(metadata, resource, params)

    def get_organization_camera_boundaries_lines_by_device(
        self, *, organization_id: str, serials: list | None = None
    ) -> dict[str, Any] | None:
        """Returns all configured crossingline boundaries of cameras.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-camera-boundaries-lines-by-device

        Args:
            organization_id: Organization ID.
            serials: A list of serial numbers. The returned cameras will be filtered to only include
              these serials.

        """
        metadata = {
            "tags": ["camera", "configure", "boundaries", "lines", "byDevice"],
            "operation": "get_organization_camera_boundaries_lines_by_device",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/camera/boundaries/lines/byDevice"

        params = {}
        if serials is not None:
            params["serials[]"] = serials

        return self._session.get(metadata, resource, params)

    def get_organization_camera_custom_analytics_artifacts(
        self, *, organization_id: str
    ) -> dict[str, Any] | None:
        """List Custom Analytics Artifacts.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-camera-custom-analytics-artifacts

        Args:
            organization_id: Organization ID.

        """
        metadata = {
            "tags": ["camera", "configure", "customAnalytics", "artifacts"],
            "operation": "get_organization_camera_custom_analytics_artifacts",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/camera/customAnalytics/artifacts"

        return self._session.get(metadata, resource)

    def create_organization_camera_custom_analytics_artifact(
        self, *, organization_id: str, name: str | None = None
    ) -> dict[str, Any] | None:
        """Create custom analytics artifact.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-camera-custom-analytics-artifact

        Args:
            organization_id: Organization ID.
            name: Unique name of the artifact.

        """
        metadata = {
            "tags": ["camera", "configure", "customAnalytics", "artifacts"],
            "operation": "create_organization_camera_custom_analytics_artifact",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/camera/customAnalytics/artifacts"

        payload = {}
        if name is not None:
            payload["name"] = name

        return self._session.post(metadata, resource, payload)

    def get_organization_camera_custom_analytics_artifact(
        self, *, organization_id: str, artifact_id: str
    ) -> dict[str, Any] | None:
        """Get Custom Analytics Artifact.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-camera-custom-analytics-artifact

        Args:
            organization_id: Organization ID.
            artifact_id: Artifact ID.

        """
        metadata = {
            "tags": ["camera", "configure", "customAnalytics", "artifacts"],
            "operation": "get_organization_camera_custom_analytics_artifact",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        artifact_id = urllib.parse.quote(str(artifact_id), safe="")
        resource = (
            f"/organizations/{organization_id}/camera/customAnalytics/artifacts/{artifact_id}"
        )

        return self._session.get(metadata, resource)

    def delete_organization_camera_custom_analytics_artifact(
        self, *, organization_id: str, artifact_id: str
    ) -> None:
        """Delete Custom Analytics Artifact.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-camera-custom-analytics-artifact

        Args:
            organization_id: Organization ID.
            artifact_id: Artifact ID.

        """
        metadata = {
            "tags": ["camera", "configure", "customAnalytics", "artifacts"],
            "operation": "delete_organization_camera_custom_analytics_artifact",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        artifact_id = urllib.parse.quote(str(artifact_id), safe="")
        resource = (
            f"/organizations/{organization_id}/camera/customAnalytics/artifacts/{artifact_id}"
        )

        return self._session.delete(metadata, resource)

    def get_organization_camera_detections_history_by_boundary_by_interval(
        self,
        *,
        organization_id: str,
        boundary_ids: list,
        ranges: list,
        duration: int | None = None,
        per_page: int | None = None,
        boundary_types: list | None = None,
        total_pages: str = 1,
        direction: str = "next",
    ) -> Generator[Any, None, None]:
        """Returns analytics data for timespans.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-camera-detections-history-by-boundary-by-interval

        Args:
            organization_id: Organization ID.
            boundary_ids: A list of boundary ids. The returned cameras will be filtered to only
              include these ids.
            ranges: A list of time ranges with intervals.
            duration: The minimum time, in seconds, that the person or car remains in the area to be
              counted. Defaults to boundary configuration or 60.
            per_page: The number of entries per page returned. Acceptable range is 1 - 1000.
              Defaults to 1000.
            boundary_types: The detection types. Defaults to 'person'.
            total_pages: use with perPage to get total results up to total_pages*perPage; -1 or
              "all" for all pages.
            direction: direction to paginate, either "next" (default) or "prev" page.

        """
        metadata = {
            "tags": ["camera", "configure", "detections", "history", "byBoundary", "byInterval"],
            "operation": "get_organization_camera_detections_history_by_boundary_by_interval",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = (
            f"/organizations/{organization_id}/camera/detections/history/byBoundary/byInterval"
        )

        params = {}
        if boundary_ids is not None:
            params["boundaryIds[]"] = boundary_ids
        if ranges is not None:
            params["ranges[]"] = ranges
        if duration is not None:
            params["duration"] = duration
        if per_page is not None:
            params["perPage"] = per_page
        if boundary_types is not None:
            params["boundaryTypes[]"] = boundary_types

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def get_organization_camera_onboarding_statuses(
        self, *, organization_id: str, serials: list | None = None, network_ids: list | None = None
    ) -> dict[str, Any] | None:
        """Fetch onboarding status of cameras.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-camera-onboarding-statuses

        Args:
            organization_id: Organization ID.
            serials: A list of serial numbers. The returned cameras will be filtered to only include
              these serials.
            network_ids: A list of network IDs. The returned cameras will be filtered to only
              include these networks.

        """
        metadata = {
            "tags": ["camera", "configure", "onboarding", "statuses"],
            "operation": "get_organization_camera_onboarding_statuses",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/camera/onboarding/statuses"

        params = {}
        if serials is not None:
            params["serials[]"] = serials
        if network_ids is not None:
            params["networkIds[]"] = network_ids

        return self._session.get(metadata, resource, params)

    def update_organization_camera_onboarding_statuses(
        self,
        *,
        organization_id: str,
        serial: str | None = None,
        wireless_credentials_sent: bool | None = None,
    ) -> dict[str, Any] | None:
        """Notify that credential handoff to camera has completed.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-camera-onboarding-statuses

        Args:
            organization_id: Organization ID.
            serial: Serial of camera.
            wireless_credentials_sent: Note whether credentials were sent successfully.

        """
        metadata = {
            "tags": ["camera", "configure", "onboarding", "statuses"],
            "operation": "update_organization_camera_onboarding_statuses",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/camera/onboarding/statuses"

        payload = {}
        if serial is not None:
            payload["serial"] = serial
        if wireless_credentials_sent is not None:
            payload["wirelessCredentialsSent"] = wireless_credentials_sent

        return self._session.put(metadata, resource, payload)

    def get_organization_camera_permissions(self, *, organization_id: str) -> dict[str, Any] | None:
        """List the permissions scopes for this organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-camera-permissions

        Args:
            organization_id: Organization ID.

        """
        metadata = {
            "tags": ["camera", "configure", "permissions"],
            "operation": "get_organization_camera_permissions",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/camera/permissions"

        return self._session.get(metadata, resource)

    def get_organization_camera_permission(
        self, *, organization_id: str, permission_scope_id: str
    ) -> dict[str, Any] | None:
        """Retrieve a single permission scope.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-camera-permission

        Args:
            organization_id: Organization ID.
            permission_scope_id: Permission scope ID.

        """
        metadata = {
            "tags": ["camera", "configure", "permissions"],
            "operation": "get_organization_camera_permission",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        permission_scope_id = urllib.parse.quote(str(permission_scope_id), safe="")
        resource = f"/organizations/{organization_id}/camera/permissions/{permission_scope_id}"

        return self._session.get(metadata, resource)

    def get_organization_camera_roles(self, *, organization_id: str) -> dict[str, Any] | None:
        """List all the roles in this organization.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-camera-roles

        Args:
            organization_id: Organization ID.

        """
        metadata = {
            "tags": ["camera", "configure", "roles"],
            "operation": "get_organization_camera_roles",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/camera/roles"

        return self._session.get(metadata, resource)

    def create_organization_camera_role(
        self,
        *,
        organization_id: str,
        name: str,
        applied_on_devices: list | None = None,
        applied_on_networks: list | None = None,
        applied_org_wide: list | None = None,
    ) -> dict[str, Any] | None:
        """Creates new role for this organization.

        https://developer.cisco.com/meraki/api-v1/#!create-organization-camera-role

        Args:
            organization_id: Organization ID.
            name: The name of the new role. Must be unique. This parameter is required.
            applied_on_devices: Device tag on which this specified permission is applied.
            applied_on_networks: Network tag on which this specified permission is applied.
            applied_org_wide: Permissions to be applied org wide.

        """
        metadata = {
            "tags": ["camera", "configure", "roles"],
            "operation": "create_organization_camera_role",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        resource = f"/organizations/{organization_id}/camera/roles"

        payload = {}
        if name is not None:
            payload["name"] = name
        if applied_on_devices is not None:
            payload["appliedOnDevices"] = applied_on_devices
        if applied_on_networks is not None:
            payload["appliedOnNetworks"] = applied_on_networks
        if applied_org_wide is not None:
            payload["appliedOrgWide"] = applied_org_wide

        return self._session.post(metadata, resource, payload)

    def get_organization_camera_role(
        self, *, organization_id: str, role_id: str
    ) -> dict[str, Any] | None:
        """Retrieve a single role.

        https://developer.cisco.com/meraki/api-v1/#!get-organization-camera-role

        Args:
            organization_id: Organization ID.
            role_id: Role ID.

        """
        metadata = {
            "tags": ["camera", "configure", "roles"],
            "operation": "get_organization_camera_role",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        role_id = urllib.parse.quote(str(role_id), safe="")
        resource = f"/organizations/{organization_id}/camera/roles/{role_id}"

        return self._session.get(metadata, resource)

    def update_organization_camera_role(
        self,
        *,
        organization_id: str,
        role_id: str,
        name: str | None = None,
        applied_on_devices: list | None = None,
        applied_on_networks: list | None = None,
        applied_org_wide: list | None = None,
    ) -> dict[str, Any] | None:
        """Update an existing role in this organization.

        https://developer.cisco.com/meraki/api-v1/#!update-organization-camera-role

        Args:
            organization_id: Organization ID.
            role_id: Role ID.
            name: The name of the new role. Must be unique.
            applied_on_devices: Device tag on which this specified permission is applied.
            applied_on_networks: Network tag on which this specified permission is applied.
            applied_org_wide: Permissions to be applied org wide.

        """
        metadata = {
            "tags": ["camera", "configure", "roles"],
            "operation": "update_organization_camera_role",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        role_id = urllib.parse.quote(str(role_id), safe="")
        resource = f"/organizations/{organization_id}/camera/roles/{role_id}"

        payload = {}
        if name is not None:
            payload["name"] = name
        if applied_on_devices is not None:
            payload["appliedOnDevices"] = applied_on_devices
        if applied_on_networks is not None:
            payload["appliedOnNetworks"] = applied_on_networks
        if applied_org_wide is not None:
            payload["appliedOrgWide"] = applied_org_wide

        return self._session.put(metadata, resource, payload)

    def delete_organization_camera_role(self, *, organization_id: str, role_id: str) -> None:
        """Delete an existing role for this organization.

        https://developer.cisco.com/meraki/api-v1/#!delete-organization-camera-role

        Args:
            organization_id: Organization ID.
            role_id: Role ID.

        """
        metadata = {
            "tags": ["camera", "configure", "roles"],
            "operation": "delete_organization_camera_role",
        }
        organization_id = urllib.parse.quote(str(organization_id), safe="")
        role_id = urllib.parse.quote(str(role_id), safe="")
        resource = f"/organizations/{organization_id}/camera/roles/{role_id}"

        return self._session.delete(metadata, resource)
