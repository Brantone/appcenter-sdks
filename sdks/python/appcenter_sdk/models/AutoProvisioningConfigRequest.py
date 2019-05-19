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


class AutoProvisioningConfigRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'apple_developer_account_key': 'string',
        'apple_distribution_certificate_key': 'string',
        'allow_auto_provisioning': 'boolean'
    }

    attribute_map = {
        'apple_developer_account_key': 'apple_developer_account_key',
        'apple_distribution_certificate_key': 'apple_distribution_certificate_key',
        'allow_auto_provisioning': 'allow_auto_provisioning'
    }

    def __init__(self, apple_developer_account_key=None, apple_distribution_certificate_key=None, allow_auto_provisioning=None):  # noqa: E501
        """AutoProvisioningConfigRequest - a model defined in Swagger"""  # noqa: E501
        self._apple_developer_account_key = None
        self._apple_distribution_certificate_key = None
        self._allow_auto_provisioning = None
        self.discriminator = None
        if apple_developer_account_key is not None:
            self.apple_developer_account_key = apple_developer_account_key
        if apple_distribution_certificate_key is not None:
            self.apple_distribution_certificate_key = apple_distribution_certificate_key
        if allow_auto_provisioning is not None:
            self.allow_auto_provisioning = allow_auto_provisioning

    @property
    def apple_developer_account_key(self):
        """Gets the apple_developer_account_key of this AutoProvisioningConfigRequest.  # noqa: E501

        A key to a secret in customer-credential-store. apple_developer_account refers to the user's developer account that is used to log into https://developer.apple.com. Normally the user's email.  # noqa: E501

        :return: The apple_developer_account_key of this AutoProvisioningConfigRequest.  # noqa: E501
        :rtype: string
        """
        return self._apple_developer_account_key

    @apple_developer_account_key.setter
    def apple_developer_account_key(self, apple_developer_account_key):
        """Sets the apple_developer_account_key of this AutoProvisioningConfigRequest.

        A key to a secret in customer-credential-store. apple_developer_account refers to the user's developer account that is used to log into https://developer.apple.com. Normally the user's email.  # noqa: E501

        :param apple_developer_account_key: The apple_developer_account_key of this AutoProvisioningConfigRequest.  # noqa: E501
        :type: string
        """

        self._apple_developer_account_key = apple_developer_account_key

    @property
    def apple_distribution_certificate_key(self):
        """Gets the apple_distribution_certificate_key of this AutoProvisioningConfigRequest.  # noqa: E501

        A key to a secret in customer-credential-store. distribution_certificate refers to the customer's certificate (that holds the private key) that will be used to sign the app.  # noqa: E501

        :return: The apple_distribution_certificate_key of this AutoProvisioningConfigRequest.  # noqa: E501
        :rtype: string
        """
        return self._apple_distribution_certificate_key

    @apple_distribution_certificate_key.setter
    def apple_distribution_certificate_key(self, apple_distribution_certificate_key):
        """Sets the apple_distribution_certificate_key of this AutoProvisioningConfigRequest.

        A key to a secret in customer-credential-store. distribution_certificate refers to the customer's certificate (that holds the private key) that will be used to sign the app.  # noqa: E501

        :param apple_distribution_certificate_key: The apple_distribution_certificate_key of this AutoProvisioningConfigRequest.  # noqa: E501
        :type: string
        """

        self._apple_distribution_certificate_key = apple_distribution_certificate_key

    @property
    def allow_auto_provisioning(self):
        """Gets the allow_auto_provisioning of this AutoProvisioningConfigRequest.  # noqa: E501

        When *true* enables auto provisioning  # noqa: E501

        :return: The allow_auto_provisioning of this AutoProvisioningConfigRequest.  # noqa: E501
        :rtype: boolean
        """
        return self._allow_auto_provisioning

    @allow_auto_provisioning.setter
    def allow_auto_provisioning(self, allow_auto_provisioning):
        """Sets the allow_auto_provisioning of this AutoProvisioningConfigRequest.

        When *true* enables auto provisioning  # noqa: E501

        :param allow_auto_provisioning: The allow_auto_provisioning of this AutoProvisioningConfigRequest.  # noqa: E501
        :type: boolean
        """

        self._allow_auto_provisioning = allow_auto_provisioning

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
        if not isinstance(other, AutoProvisioningConfigRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
