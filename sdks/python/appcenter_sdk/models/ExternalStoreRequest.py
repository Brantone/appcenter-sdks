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


class ExternalStoreRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    production = "production"
    alpha = "alpha"
    beta = "beta"
    testflight-internal = "testflight-internal"
    testflight-external = "testflight-external"
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'type': 'string',
        'name': 'string',
        'track': 'string',
        'intune_details': '',
        'service_connection_id': 'string'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'track': 'track',
        'intune_details': 'intune_details',
        'service_connection_id': 'service_connection_id'
    }

    def __init__(self, type=None, name=None, track=None, intune_details=None, service_connection_id=None):  # noqa: E501
        """ExternalStoreRequest - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._name = None
        self._track = None
        self._intune_details = None
        self._service_connection_id = None
        self.discriminator = None
        if type is not None:
            self.type = type
        if name is not None:
            self.name = name
        if track is not None:
            self.track = track
        if intune_details is not None:
            self.intune_details = intune_details
        if service_connection_id is not None:
            self.service_connection_id = service_connection_id

    @property
    def type(self):
        """Gets the type of this ExternalStoreRequest.  # noqa: E501

        store Type  # noqa: E501

        :return: The type of this ExternalStoreRequest.  # noqa: E501
        :rtype: string
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ExternalStoreRequest.

        store Type  # noqa: E501

        :param type: The type of this ExternalStoreRequest.  # noqa: E501
        :type: string
        """
        allowed_values = [undefined, undefined, undefined, undefined, undefined, ]  # noqa: E501

        self._type = type

    @property
    def name(self):
        """Gets the name of this ExternalStoreRequest.  # noqa: E501

        name of the store. In case of googleplay, and Apple store this is fixed to Production.  # noqa: E501

        :return: The name of this ExternalStoreRequest.  # noqa: E501
        :rtype: string
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ExternalStoreRequest.

        name of the store. In case of googleplay, and Apple store this is fixed to Production.  # noqa: E501

        :param name: The name of this ExternalStoreRequest.  # noqa: E501
        :type: string
        """

        self._name = name

    @property
    def track(self):
        """Gets the track of this ExternalStoreRequest.  # noqa: E501

        track of the store. Can be production, alpha & beta for googleplay. Can be production, testflight-internal & testflight-external for Apple Store.  # noqa: E501

        :return: The track of this ExternalStoreRequest.  # noqa: E501
        :rtype: string
        """
        return self._track

    @track.setter
    def track(self, track):
        """Sets the track of this ExternalStoreRequest.

        track of the store. Can be production, alpha & beta for googleplay. Can be production, testflight-internal & testflight-external for Apple Store.  # noqa: E501

        :param track: The track of this ExternalStoreRequest.  # noqa: E501
        :type: string
        """
        allowed_values = [undefined, undefined, undefined, undefined, undefined, ]  # noqa: E501

        self._track = track

    @property
    def intune_details(self):
        """Gets the intune_details of this ExternalStoreRequest.  # noqa: E501


        :return: The intune_details of this ExternalStoreRequest.  # noqa: E501
        :rtype: 
        """
        return self._intune_details

    @intune_details.setter
    def intune_details(self, intune_details):
        """Sets the intune_details of this ExternalStoreRequest.


        :param intune_details: The intune_details of this ExternalStoreRequest.  # noqa: E501
        :type: 
        """

        self._intune_details = intune_details

    @property
    def service_connection_id(self):
        """Gets the service_connection_id of this ExternalStoreRequest.  # noqa: E501

        Id for the shared service connection. In case of Apple AppStore, this connection will be used to create and connect to the Apple AppStore in Mobile Center.  # noqa: E501

        :return: The service_connection_id of this ExternalStoreRequest.  # noqa: E501
        :rtype: string
        """
        return self._service_connection_id

    @service_connection_id.setter
    def service_connection_id(self, service_connection_id):
        """Sets the service_connection_id of this ExternalStoreRequest.

        Id for the shared service connection. In case of Apple AppStore, this connection will be used to create and connect to the Apple AppStore in Mobile Center.  # noqa: E501

        :param service_connection_id: The service_connection_id of this ExternalStoreRequest.  # noqa: E501
        :type: string
        """

        self._service_connection_id = service_connection_id

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
        if not isinstance(other, ExternalStoreRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
