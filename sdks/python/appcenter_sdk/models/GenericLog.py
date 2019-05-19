# coding: utf-8

"""
    App Center Client

    Microsoft Visual Studio App Center API  # noqa: E501

    OpenAPI spec version: preview
    Contact: benedetto.abbenanti@gmail.com
    Project Repository: https://github.com/b3nab/appcenter-sdks
"""

import pprint
import re  # noqa: F401

import six


class GenericLog(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    event = "event"
    page = "page"
    start_session = "start_session"
    error = "error"
    push_installation = "push_installation"
    start_service = "start_service"
    custom_properties = "custom_properties"
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'type': 'string',
        'timestamp': 'string',
        'install_id': 'string',
        'session_id': 'string',
        'event_id': 'string',
        'event_name': 'string',
        'message_id': 'string',
        'properties': 'object',
        'device': 'object'
    }

    attribute_map = {
        'type': 'type',
        'timestamp': 'timestamp',
        'install_id': 'install_id',
        'session_id': 'session_id',
        'event_id': 'event_id',
        'event_name': 'event_name',
        'message_id': 'message_id',
        'properties': 'properties',
        'device': 'device'
    }

    def __init__(self, type=None, timestamp=None, install_id=None, session_id=None, event_id=None, event_name=None, message_id=None, properties=None, device=None):  # noqa: E501
        """GenericLog - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._timestamp = None
        self._install_id = None
        self._session_id = None
        self._event_id = None
        self._event_name = None
        self._message_id = None
        self._properties = None
        self._device = None
        self.discriminator = None
        self.type = type
        self.timestamp = timestamp
        self.install_id = install_id
        if session_id is not None:
            self.session_id = session_id
        if event_id is not None:
            self.event_id = event_id
        if event_name is not None:
            self.event_name = event_name
        if message_id is not None:
            self.message_id = message_id
        if properties is not None:
            self.properties = properties
        self.device = device

    @property
    def type(self):
        """Gets the type of this GenericLog.  # noqa: E501

        Log type.
  # noqa: E501

        :return: The type of this GenericLog.  # noqa: E501
        :rtype: string
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GenericLog.

        Log type.
  # noqa: E501

        :param type: The type of this GenericLog.  # noqa: E501
        :type: string
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = [undefined, undefined, undefined, undefined, undefined, undefined, undefined, ]  # noqa: E501

        self._type = type

    @property
    def timestamp(self):
        """Gets the timestamp of this GenericLog.  # noqa: E501

        Log creation timestamp.
  # noqa: E501

        :return: The timestamp of this GenericLog.  # noqa: E501
        :rtype: string
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this GenericLog.

        Log creation timestamp.
  # noqa: E501

        :param timestamp: The timestamp of this GenericLog.  # noqa: E501
        :type: string
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def install_id(self):
        """Gets the install_id of this GenericLog.  # noqa: E501

        Install ID.
  # noqa: E501

        :return: The install_id of this GenericLog.  # noqa: E501
        :rtype: string
        """
        return self._install_id

    @install_id.setter
    def install_id(self, install_id):
        """Sets the install_id of this GenericLog.

        Install ID.
  # noqa: E501

        :param install_id: The install_id of this GenericLog.  # noqa: E501
        :type: string
        """
        if install_id is None:
            raise ValueError("Invalid value for `install_id`, must not be `None`")  # noqa: E501

        self._install_id = install_id

    @property
    def session_id(self):
        """Gets the session_id of this GenericLog.  # noqa: E501

        Session ID.
  # noqa: E501

        :return: The session_id of this GenericLog.  # noqa: E501
        :rtype: string
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this GenericLog.

        Session ID.
  # noqa: E501

        :param session_id: The session_id of this GenericLog.  # noqa: E501
        :type: string
        """

        self._session_id = session_id

    @property
    def event_id(self):
        """Gets the event_id of this GenericLog.  # noqa: E501

        Event ID.
  # noqa: E501

        :return: The event_id of this GenericLog.  # noqa: E501
        :rtype: string
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Sets the event_id of this GenericLog.

        Event ID.
  # noqa: E501

        :param event_id: The event_id of this GenericLog.  # noqa: E501
        :type: string
        """

        self._event_id = event_id

    @property
    def event_name(self):
        """Gets the event_name of this GenericLog.  # noqa: E501

        Event name.
  # noqa: E501

        :return: The event_name of this GenericLog.  # noqa: E501
        :rtype: string
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """Sets the event_name of this GenericLog.

        Event name.
  # noqa: E501

        :param event_name: The event_name of this GenericLog.  # noqa: E501
        :type: string
        """

        self._event_name = event_name

    @property
    def message_id(self):
        """Gets the message_id of this GenericLog.  # noqa: E501

        Message ID.
  # noqa: E501

        :return: The message_id of this GenericLog.  # noqa: E501
        :rtype: string
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        """Sets the message_id of this GenericLog.

        Message ID.
  # noqa: E501

        :param message_id: The message_id of this GenericLog.  # noqa: E501
        :type: string
        """

        self._message_id = message_id

    @property
    def properties(self):
        """Gets the properties of this GenericLog.  # noqa: E501

        event specific properties.
  # noqa: E501

        :return: The properties of this GenericLog.  # noqa: E501
        :rtype: object
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this GenericLog.

        event specific properties.
  # noqa: E501

        :param properties: The properties of this GenericLog.  # noqa: E501
        :type: object
        """

        self._properties = properties

    @property
    def device(self):
        """Gets the device of this GenericLog.  # noqa: E501

        Device characteristics.  # noqa: E501

        :return: The device of this GenericLog.  # noqa: E501
        :rtype: object
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this GenericLog.

        Device characteristics.  # noqa: E501

        :param device: The device of this GenericLog.  # noqa: E501
        :type: object
        """
        if device is None:
            raise ValueError("Invalid value for `device`, must not be `None`")  # noqa: E501

        self._device = device

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GenericLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
