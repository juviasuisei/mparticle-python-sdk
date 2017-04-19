# coding: utf-8

"""
    mParticle

    mParticle Event API

    OpenAPI spec version: 1.0.1
    Contact: support@mparticle.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re
from uuid import UUID


class DeviceInformation(object):

    def __init__(self, brand=None, product=None, device=None, android_uuid=None, device_manufacturer=None, platform=None, os_version=None, device_model=None, screen_height=None, screen_width=None, screen_dpi=None, device_country=None, locale_language=None, locale_country=None, network_country=None, network_carrier=None, network_code=None, network_mobile_country_code=None, timezone_offset=None, build_identifier=None, http_header_user_agent=None, ios_advertising_id=None, push_token=None, cpu_architecture=None, is_tablet=None, push_notification_sound_enabled=None, push_notification_vibrate_enabled=None, radio_access_technology=None, supports_telephony=None, has_nfc=None, bluetooth_enabled=None, bluetooth_version=None, ios_idfv=None, android_advertising_id=None):
        """
        DeviceInformation - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'brand': 'str',
            'product': 'str',
            'device': 'str',
            'android_uuid': 'str',
            'device_manufacturer': 'str',
            'platform': 'str',
            'os_version': 'str',
            'device_model': 'str',
            'screen_height': 'int',
            'screen_width': 'int',
            'screen_dpi': 'int',
            'device_country': 'str',
            'locale_language': 'str',
            'locale_country': 'str',
            'network_country': 'str',
            'network_carrier': 'str',
            'network_code': 'str',
            'network_mobile_country_code': 'str',
            'timezone_offset': 'int',
            'build_identifier': 'str',
            'http_header_user_agent': 'str',
            'ios_advertising_id': 'str',
            'push_token': 'str',
            'cpu_architecture': 'str',
            'is_tablet': 'bool',
            'push_notification_sound_enabled': 'bool',
            'push_notification_vibrate_enabled': 'bool',
            'radio_access_technology': 'str',
            'supports_telephony': 'bool',
            'has_nfc': 'bool',
            'bluetooth_enabled': 'bool',
            'bluetooth_version': 'str',
            'ios_idfv': 'str',
            'android_advertising_id': 'str'
        }

        self.attribute_map = {
            'brand': 'brand',
            'product': 'product',
            'device': 'device',
            'android_uuid': 'android_uuid',
            'device_manufacturer': 'device_manufacturer',
            'platform': 'platform',
            'os_version': 'os_version',
            'device_model': 'device_model',
            'screen_height': 'screen_height',
            'screen_width': 'screen_width',
            'screen_dpi': 'screen_dpi',
            'device_country': 'device_country',
            'locale_language': 'locale_language',
            'locale_country': 'locale_country',
            'network_country': 'network_country',
            'network_carrier': 'network_carrier',
            'network_code': 'network_code',
            'network_mobile_country_code': 'network_mobile_country_code',
            'timezone_offset': 'timezone_offset',
            'build_identifier': 'build_identifier',
            'http_header_user_agent': 'http_header_user_agent',
            'ios_advertising_id': 'ios_advertising_id',
            'push_token': 'push_token',
            'cpu_architecture': 'cpu_architecture',
            'is_tablet': 'is_tablet',
            'push_notification_sound_enabled': 'push_notification_sound_enabled',
            'push_notification_vibrate_enabled': 'push_notification_vibrate_enabled',
            'radio_access_technology': 'radio_access_technology',
            'supports_telephony': 'supports_telephony',
            'has_nfc': 'has_nfc',
            'bluetooth_enabled': 'bluetooth_enabled',
            'bluetooth_version': 'bluetooth_version',
            'ios_idfv': 'ios_idfv',
            'android_advertising_id': 'android_advertising_id'
        }

        self._brand = brand
        self._product = product
        self._device = device
        self._android_uuid = android_uuid
        self._device_manufacturer = device_manufacturer
        self._platform = platform
        self._os_version = os_version
        self._device_model = device_model
        self._screen_height = screen_height
        self._screen_width = screen_width
        self._screen_dpi = screen_dpi
        self._device_country = device_country
        self._locale_language = locale_language
        self._locale_country = locale_country
        self._network_country = network_country
        self._network_carrier = network_carrier
        self._network_code = network_code
        self._network_mobile_country_code = network_mobile_country_code
        self._timezone_offset = timezone_offset
        self._build_identifier = build_identifier
        self._http_header_user_agent = http_header_user_agent
        self.ios_advertising_id = ios_advertising_id
        self._push_token = push_token
        self._cpu_architecture = cpu_architecture
        self._is_tablet = is_tablet
        self._push_notification_sound_enabled = push_notification_sound_enabled
        self._push_notification_vibrate_enabled = push_notification_vibrate_enabled
        self._radio_access_technology = radio_access_technology
        self._supports_telephony = supports_telephony
        self._has_nfc = has_nfc
        self._bluetooth_enabled = bluetooth_enabled
        self._bluetooth_version = bluetooth_version
        self.ios_idfv = ios_idfv
        self.android_advertising_id = android_advertising_id

    def validateUUID(self, uuid_string):
        if uuid_string is not None:
            try:
                UUID(uuid_string)
            except ValueError as error:
                return error
        return None

    @property
    def brand(self):
        """
        Gets the brand of this DeviceInformation.


        :return: The brand of this DeviceInformation.
        :rtype: str
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        """
        Sets the brand of this DeviceInformation.


        :param brand: The brand of this DeviceInformation.
        :type: str
        """

        self._brand = brand

    @property
    def product(self):
        """
        Gets the product of this DeviceInformation.


        :return: The product of this DeviceInformation.
        :rtype: str
        """
        return self._product

    @product.setter
    def product(self, product):
        """
        Sets the product of this DeviceInformation.


        :param product: The product of this DeviceInformation.
        :type: str
        """

        self._product = product

    @property
    def device(self):
        """
        Gets the device of this DeviceInformation.


        :return: The device of this DeviceInformation.
        :rtype: str
        """
        return self._device

    @device.setter
    def device(self, device):
        """
        Sets the device of this DeviceInformation.


        :param device: The device of this DeviceInformation.
        :type: str
        """

        self._device = device

    @property
    def android_uuid(self):
        """
        Gets the android_uuid of this DeviceInformation.


        :return: The android_uuid of this DeviceInformation.
        :rtype: str
        """
        return self._android_uuid

    @android_uuid.setter
    def android_uuid(self, android_uuid):
        """
        Sets the android_uuid of this DeviceInformation.


        :param android_uuid: The android_uuid of this DeviceInformation.
        :type: str
        """

        self._android_uuid = android_uuid

    @property
    def device_manufacturer(self):
        """
        Gets the device_manufacturer of this DeviceInformation.


        :return: The device_manufacturer of this DeviceInformation.
        :rtype: str
        """
        return self._device_manufacturer

    @device_manufacturer.setter
    def device_manufacturer(self, device_manufacturer):
        """
        Sets the device_manufacturer of this DeviceInformation.


        :param device_manufacturer: The device_manufacturer of this DeviceInformation.
        :type: str
        """

        self._device_manufacturer = device_manufacturer

    @property
    def platform(self):
        """
        Gets the platform of this DeviceInformation.


        :return: The platform of this DeviceInformation.
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """
        Sets the platform of this DeviceInformation.


        :param platform: The platform of this DeviceInformation.
        :type: str
        """
        allowed_values = ["Unknown", "iOS", "Android", "tvOS"]
        if platform not in allowed_values:
            raise ValueError(
                "Invalid value for `platform` ({0}), must be one of {1}"
                .format(platform, allowed_values)
            )

        self._platform = platform

    @property
    def os_version(self):
        """
        Gets the os_version of this DeviceInformation.


        :return: The os_version of this DeviceInformation.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        """
        Sets the os_version of this DeviceInformation.


        :param os_version: The os_version of this DeviceInformation.
        :type: str
        """

        self._os_version = os_version

    @property
    def device_model(self):
        """
        Gets the device_model of this DeviceInformation.


        :return: The device_model of this DeviceInformation.
        :rtype: str
        """
        return self._device_model

    @device_model.setter
    def device_model(self, device_model):
        """
        Sets the device_model of this DeviceInformation.


        :param device_model: The device_model of this DeviceInformation.
        :type: str
        """

        self._device_model = device_model

    @property
    def screen_height(self):
        """
        Gets the screen_height of this DeviceInformation.


        :return: The screen_height of this DeviceInformation.
        :rtype: int
        """
        return self._screen_height

    @screen_height.setter
    def screen_height(self, screen_height):
        """
        Sets the screen_height of this DeviceInformation.


        :param screen_height: The screen_height of this DeviceInformation.
        :type: int
        """

        self._screen_height = screen_height

    @property
    def screen_width(self):
        """
        Gets the screen_width of this DeviceInformation.


        :return: The screen_width of this DeviceInformation.
        :rtype: int
        """
        return self._screen_width

    @screen_width.setter
    def screen_width(self, screen_width):
        """
        Sets the screen_width of this DeviceInformation.


        :param screen_width: The screen_width of this DeviceInformation.
        :type: int
        """

        self._screen_width = screen_width

    @property
    def screen_dpi(self):
        """
        Gets the screen_dpi of this DeviceInformation.


        :return: The screen_dpi of this DeviceInformation.
        :rtype: int
        """
        return self._screen_dpi

    @screen_dpi.setter
    def screen_dpi(self, screen_dpi):
        """
        Sets the screen_dpi of this DeviceInformation.


        :param screen_dpi: The screen_dpi of this DeviceInformation.
        :type: int
        """

        self._screen_dpi = screen_dpi

    @property
    def device_country(self):
        """
        Gets the device_country of this DeviceInformation.


        :return: The device_country of this DeviceInformation.
        :rtype: str
        """
        return self._device_country

    @device_country.setter
    def device_country(self, device_country):
        """
        Sets the device_country of this DeviceInformation.


        :param device_country: The device_country of this DeviceInformation.
        :type: str
        """

        self._device_country = device_country

    @property
    def locale_language(self):
        """
        Gets the locale_language of this DeviceInformation.


        :return: The locale_language of this DeviceInformation.
        :rtype: str
        """
        return self._locale_language

    @locale_language.setter
    def locale_language(self, locale_language):
        """
        Sets the locale_language of this DeviceInformation.


        :param locale_language: The locale_language of this DeviceInformation.
        :type: str
        """

        self._locale_language = locale_language

    @property
    def locale_country(self):
        """
        Gets the locale_country of this DeviceInformation.


        :return: The locale_country of this DeviceInformation.
        :rtype: str
        """
        return self._locale_country

    @locale_country.setter
    def locale_country(self, locale_country):
        """
        Sets the locale_country of this DeviceInformation.


        :param locale_country: The locale_country of this DeviceInformation.
        :type: str
        """

        self._locale_country = locale_country

    @property
    def network_country(self):
        """
        Gets the network_country of this DeviceInformation.


        :return: The network_country of this DeviceInformation.
        :rtype: str
        """
        return self._network_country

    @network_country.setter
    def network_country(self, network_country):
        """
        Sets the network_country of this DeviceInformation.


        :param network_country: The network_country of this DeviceInformation.
        :type: str
        """

        self._network_country = network_country

    @property
    def network_carrier(self):
        """
        Gets the network_carrier of this DeviceInformation.


        :return: The network_carrier of this DeviceInformation.
        :rtype: str
        """
        return self._network_carrier

    @network_carrier.setter
    def network_carrier(self, network_carrier):
        """
        Sets the network_carrier of this DeviceInformation.


        :param network_carrier: The network_carrier of this DeviceInformation.
        :type: str
        """

        self._network_carrier = network_carrier

    @property
    def network_code(self):
        """
        Gets the network_code of this DeviceInformation.


        :return: The network_code of this DeviceInformation.
        :rtype: str
        """
        return self._network_code

    @network_code.setter
    def network_code(self, network_code):
        """
        Sets the network_code of this DeviceInformation.


        :param network_code: The network_code of this DeviceInformation.
        :type: str
        """

        self._network_code = network_code

    @property
    def network_mobile_country_code(self):
        """
        Gets the network_mobile_country_code of this DeviceInformation.


        :return: The network_mobile_country_code of this DeviceInformation.
        :rtype: str
        """
        return self._network_mobile_country_code

    @network_mobile_country_code.setter
    def network_mobile_country_code(self, network_mobile_country_code):
        """
        Sets the network_mobile_country_code of this DeviceInformation.


        :param network_mobile_country_code: The network_mobile_country_code of this DeviceInformation.
        :type: str
        """

        self._network_mobile_country_code = network_mobile_country_code

    @property
    def timezone_offset(self):
        """
        Gets the timezone_offset of this DeviceInformation.


        :return: The timezone_offset of this DeviceInformation.
        :rtype: int
        """
        return self._timezone_offset

    @timezone_offset.setter
    def timezone_offset(self, timezone_offset):
        """
        Sets the timezone_offset of this DeviceInformation.


        :param timezone_offset: The timezone_offset of this DeviceInformation.
        :type: int
        """

        self._timezone_offset = timezone_offset

    @property
    def build_identifier(self):
        """
        Gets the build_identifier of this DeviceInformation.


        :return: The build_identifier of this DeviceInformation.
        :rtype: str
        """
        return self._build_identifier

    @build_identifier.setter
    def build_identifier(self, build_identifier):
        """
        Sets the build_identifier of this DeviceInformation.


        :param build_identifier: The build_identifier of this DeviceInformation.
        :type: str
        """

        self._build_identifier = build_identifier

    @property
    def http_header_user_agent(self):
        """
        Gets the http_header_user_agent of this DeviceInformation.


        :return: The http_header_user_agent of this DeviceInformation.
        :rtype: str
        """
        return self._http_header_user_agent

    @http_header_user_agent.setter
    def http_header_user_agent(self, http_header_user_agent):
        """
        Sets the http_header_user_agent of this DeviceInformation.


        :param http_header_user_agent: The http_header_user_agent of this DeviceInformation.
        :type: str
        """

        self._http_header_user_agent = http_header_user_agent

    @property
    def ios_advertising_id(self):
        """
        Gets the ios_advertising_id of this DeviceInformation.


        :return: The ios_advertising_id of this DeviceInformation.
        :rtype: str
        """
        return self._ios_advertising_id

    @ios_advertising_id.setter
    def ios_advertising_id(self, ios_advertising_id):
        """
        Sets the ios_advertising_id of this DeviceInformation.


        :param ios_advertising_id: The ios_advertising_id of this DeviceInformation.
        :type: str
        """

        error = self.validateUUID(ios_advertising_id)
        if (error is not None):
            raise ValueError("Error: \"{0}\", while setting ios_advertising_id with value: {1}"
                .format(error, ios_advertising_id))

        self._ios_advertising_id = ios_advertising_id

    @property
    def push_token(self):
        """
        Gets the push_token of this DeviceInformation.


        :return: The push_token of this DeviceInformation.
        :rtype: str
        """
        return self._push_token

    @push_token.setter
    def push_token(self, push_token):
        """
        Sets the push_token of this DeviceInformation.


        :param push_token: The push_token of this DeviceInformation.
        :type: str
        """

        self._push_token = push_token

    @property
    def cpu_architecture(self):
        """
        Gets the cpu_architecture of this DeviceInformation.


        :return: The cpu_architecture of this DeviceInformation.
        :rtype: str
        """
        return self._cpu_architecture

    @cpu_architecture.setter
    def cpu_architecture(self, cpu_architecture):
        """
        Sets the cpu_architecture of this DeviceInformation.


        :param cpu_architecture: The cpu_architecture of this DeviceInformation.
        :type: str
        """

        self._cpu_architecture = cpu_architecture

    @property
    def is_tablet(self):
        """
        Gets the is_tablet of this DeviceInformation.


        :return: The is_tablet of this DeviceInformation.
        :rtype: bool
        """
        return self._is_tablet

    @is_tablet.setter
    def is_tablet(self, is_tablet):
        """
        Sets the is_tablet of this DeviceInformation.


        :param is_tablet: The is_tablet of this DeviceInformation.
        :type: bool
        """

        self._is_tablet = is_tablet

    @property
    def push_notification_sound_enabled(self):
        """
        Gets the push_notification_sound_enabled of this DeviceInformation.


        :return: The push_notification_sound_enabled of this DeviceInformation.
        :rtype: bool
        """
        return self._push_notification_sound_enabled

    @push_notification_sound_enabled.setter
    def push_notification_sound_enabled(self, push_notification_sound_enabled):
        """
        Sets the push_notification_sound_enabled of this DeviceInformation.


        :param push_notification_sound_enabled: The push_notification_sound_enabled of this DeviceInformation.
        :type: bool
        """

        self._push_notification_sound_enabled = push_notification_sound_enabled

    @property
    def push_notification_vibrate_enabled(self):
        """
        Gets the push_notification_vibrate_enabled of this DeviceInformation.


        :return: The push_notification_vibrate_enabled of this DeviceInformation.
        :rtype: bool
        """
        return self._push_notification_vibrate_enabled

    @push_notification_vibrate_enabled.setter
    def push_notification_vibrate_enabled(self, push_notification_vibrate_enabled):
        """
        Sets the push_notification_vibrate_enabled of this DeviceInformation.


        :param push_notification_vibrate_enabled: The push_notification_vibrate_enabled of this DeviceInformation.
        :type: bool
        """

        self._push_notification_vibrate_enabled = push_notification_vibrate_enabled

    @property
    def radio_access_technology(self):
        """
        Gets the radio_access_technology of this DeviceInformation.


        :return: The radio_access_technology of this DeviceInformation.
        :rtype: str
        """
        return self._radio_access_technology

    @radio_access_technology.setter
    def radio_access_technology(self, radio_access_technology):
        """
        Sets the radio_access_technology of this DeviceInformation.


        :param radio_access_technology: The radio_access_technology of this DeviceInformation.
        :type: str
        """

        self._radio_access_technology = radio_access_technology

    @property
    def supports_telephony(self):
        """
        Gets the supports_telephony of this DeviceInformation.


        :return: The supports_telephony of this DeviceInformation.
        :rtype: bool
        """
        return self._supports_telephony

    @supports_telephony.setter
    def supports_telephony(self, supports_telephony):
        """
        Sets the supports_telephony of this DeviceInformation.


        :param supports_telephony: The supports_telephony of this DeviceInformation.
        :type: bool
        """

        self._supports_telephony = supports_telephony

    @property
    def has_nfc(self):
        """
        Gets the has_nfc of this DeviceInformation.


        :return: The has_nfc of this DeviceInformation.
        :rtype: bool
        """
        return self._has_nfc

    @has_nfc.setter
    def has_nfc(self, has_nfc):
        """
        Sets the has_nfc of this DeviceInformation.


        :param has_nfc: The has_nfc of this DeviceInformation.
        :type: bool
        """

        self._has_nfc = has_nfc

    @property
    def bluetooth_enabled(self):
        """
        Gets the bluetooth_enabled of this DeviceInformation.


        :return: The bluetooth_enabled of this DeviceInformation.
        :rtype: bool
        """
        return self._bluetooth_enabled

    @bluetooth_enabled.setter
    def bluetooth_enabled(self, bluetooth_enabled):
        """
        Sets the bluetooth_enabled of this DeviceInformation.


        :param bluetooth_enabled: The bluetooth_enabled of this DeviceInformation.
        :type: bool
        """

        self._bluetooth_enabled = bluetooth_enabled

    @property
    def bluetooth_version(self):
        """
        Gets the bluetooth_version of this DeviceInformation.


        :return: The bluetooth_version of this DeviceInformation.
        :rtype: str
        """
        return self._bluetooth_version

    @bluetooth_version.setter
    def bluetooth_version(self, bluetooth_version):
        """
        Sets the bluetooth_version of this DeviceInformation.


        :param bluetooth_version: The bluetooth_version of this DeviceInformation.
        :type: str
        """

        self._bluetooth_version = bluetooth_version

    @property
    def ios_idfv(self):
        """
        Gets the ios_idfv of this DeviceInformation.


        :return: The ios_idfv of this DeviceInformation.
        :rtype: str
        """
        return self._ios_idfv

    @ios_idfv.setter
    def ios_idfv(self, ios_idfv):
        """
        Sets the ios_idfv of this DeviceInformation.


        :param ios_idfv: The ios_idfv of this DeviceInformation.
        :type: str
        """
        error = self.validateUUID(ios_idfv)
        if (error is not None):
            raise ValueError("Error: \"{0}\", while setting ios_idfv with value: {1}"
                .format(error, ios_idfv))

        self._ios_idfv = ios_idfv

    @property
    def android_advertising_id(self):
        """
        Gets the android_advertising_id of this DeviceInformation.


        :return: The android_advertising_id of this DeviceInformation.
        :rtype: str
        """
        return self._android_advertising_id

    @android_advertising_id.setter
    def android_advertising_id(self, android_advertising_id):
        """
        Sets the android_advertising_id of this DeviceInformation.


        :param android_advertising_id: The android_advertising_id of this DeviceInformation.
        :type: str
        """
        error = self.validateUUID(android_advertising_id)
        if (error is not None):
            raise ValueError("Error: \"{0}\", while setting android_advertising_id with value: {1}"
                .format(error, android_advertising_id))

        self._android_advertising_id = android_advertising_id

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
