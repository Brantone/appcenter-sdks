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


class SubmitDsrOperationResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    NotStarted = "NotStarted"
    InProgress = "InProgress"
    Completed = "Completed"
    Failure = "Failure"
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'status': 'string'
    }

    attribute_map = {
        'status': 'status'
    }

    def __init__(self, status=None):  # noqa: E501
        """SubmitDsrOperationResponse - a model defined in Swagger"""  # noqa: E501
        self._status = None
        self.discriminator = None
        if status is not None:
            self.status = status

    @property
    def status(self):
        """Gets the status of this SubmitDsrOperationResponse.  # noqa: E501

        The status of the DSR operation  # noqa: E501

        :return: The status of this SubmitDsrOperationResponse.  # noqa: E501
        :rtype: string
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SubmitDsrOperationResponse.

        The status of the DSR operation  # noqa: E501

        :param status: The status of this SubmitDsrOperationResponse.  # noqa: E501
        :type: string
        """
        allowed_values = [undefinedundefinedundefinedundefined]  # noqa: E501

        self._status = status

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
        if not isinstance(other, SubmitDsrOperationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
