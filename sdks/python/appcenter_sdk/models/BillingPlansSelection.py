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


class BillingPlansSelection(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    Build = "Build"
    Test = "Test"
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'build_service': '',
        'test_service': ''
    }

    attribute_map = {
        'build_service': 'build_service',
        'test_service': 'test_service'
    }

    def __init__(self, build_service=None, test_service=None):  # noqa: E501
        """BillingPlansSelection - a model defined in Swagger"""  # noqa: E501
        self._build_service = None
        self._test_service = None
        self.discriminator = None
        if build_service is not None:
            self.build_service = build_service
        if test_service is not None:
            self.test_service = test_service

    @property
    def build_service(self):
        """Gets the build_service of this BillingPlansSelection.  # noqa: E501

        Selection of a billing plan  # noqa: E501

        :return: The build_service of this BillingPlansSelection.  # noqa: E501
        :rtype: 
        """
        return self._build_service

    @build_service.setter
    def build_service(self, build_service):
        """Sets the build_service of this BillingPlansSelection.

        Selection of a billing plan  # noqa: E501

        :param build_service: The build_service of this BillingPlansSelection.  # noqa: E501
        :type: 
        """

        self._build_service = build_service

    @property
    def test_service(self):
        """Gets the test_service of this BillingPlansSelection.  # noqa: E501

        Selection of a billing plan  # noqa: E501

        :return: The test_service of this BillingPlansSelection.  # noqa: E501
        :rtype: 
        """
        return self._test_service

    @test_service.setter
    def test_service(self, test_service):
        """Sets the test_service of this BillingPlansSelection.

        Selection of a billing plan  # noqa: E501

        :param test_service: The test_service of this BillingPlansSelection.  # noqa: E501
        :type: 
        """

        self._test_service = test_service

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
        if not isinstance(other, BillingPlansSelection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
