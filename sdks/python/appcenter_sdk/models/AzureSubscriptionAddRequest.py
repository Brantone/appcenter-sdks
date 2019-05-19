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


class AzureSubscriptionAddRequest(object):
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
        'subscription_id': 'string',
        'tenant_id': 'string',
        'subscription_name': 'string',
        'is_billing': 'boolean'
    }

    attribute_map = {
        'subscription_id': 'subscription_id',
        'tenant_id': 'tenant_id',
        'subscription_name': 'subscription_name',
        'is_billing': 'is_billing'
    }

    def __init__(self, subscription_id=None, tenant_id=None, subscription_name=None, is_billing=None):  # noqa: E501
        """AzureSubscriptionAddRequest - a model defined in Swagger"""  # noqa: E501
        self._subscription_id = None
        self._tenant_id = None
        self._subscription_name = None
        self._is_billing = None
        self.discriminator = None
        self.subscription_id = subscription_id
        self.tenant_id = tenant_id
        self.subscription_name = subscription_name
        if is_billing is not None:
            self.is_billing = is_billing

    @property
    def subscription_id(self):
        """Gets the subscription_id of this AzureSubscriptionAddRequest.  # noqa: E501

        The azure subscription id  # noqa: E501

        :return: The subscription_id of this AzureSubscriptionAddRequest.  # noqa: E501
        :rtype: string
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this AzureSubscriptionAddRequest.

        The azure subscription id  # noqa: E501

        :param subscription_id: The subscription_id of this AzureSubscriptionAddRequest.  # noqa: E501
        :type: string
        """
        if subscription_id is None:
            raise ValueError("Invalid value for `subscription_id`, must not be `None`")  # noqa: E501

        self._subscription_id = subscription_id

    @property
    def tenant_id(self):
        """Gets the tenant_id of this AzureSubscriptionAddRequest.  # noqa: E501

        The tenant id of the azure subscription belongs to  # noqa: E501

        :return: The tenant_id of this AzureSubscriptionAddRequest.  # noqa: E501
        :rtype: string
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this AzureSubscriptionAddRequest.

        The tenant id of the azure subscription belongs to  # noqa: E501

        :param tenant_id: The tenant_id of this AzureSubscriptionAddRequest.  # noqa: E501
        :type: string
        """
        if tenant_id is None:
            raise ValueError("Invalid value for `tenant_id`, must not be `None`")  # noqa: E501

        self._tenant_id = tenant_id

    @property
    def subscription_name(self):
        """Gets the subscription_name of this AzureSubscriptionAddRequest.  # noqa: E501

        The name of the azure subscription  # noqa: E501

        :return: The subscription_name of this AzureSubscriptionAddRequest.  # noqa: E501
        :rtype: string
        """
        return self._subscription_name

    @subscription_name.setter
    def subscription_name(self, subscription_name):
        """Sets the subscription_name of this AzureSubscriptionAddRequest.

        The name of the azure subscription  # noqa: E501

        :param subscription_name: The subscription_name of this AzureSubscriptionAddRequest.  # noqa: E501
        :type: string
        """
        if subscription_name is None:
            raise ValueError("Invalid value for `subscription_name`, must not be `None`")  # noqa: E501

        self._subscription_name = subscription_name

    @property
    def is_billing(self):
        """Gets the is_billing of this AzureSubscriptionAddRequest.  # noqa: E501

        If the subscription is used for billing  # noqa: E501

        :return: The is_billing of this AzureSubscriptionAddRequest.  # noqa: E501
        :rtype: boolean
        """
        return self._is_billing

    @is_billing.setter
    def is_billing(self, is_billing):
        """Sets the is_billing of this AzureSubscriptionAddRequest.

        If the subscription is used for billing  # noqa: E501

        :param is_billing: The is_billing of this AzureSubscriptionAddRequest.  # noqa: E501
        :type: boolean
        """

        self._is_billing = is_billing

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
        if not isinstance(other, AzureSubscriptionAddRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
