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


class EstimatedPricingResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    USD = "USD"
    EUR = "EUR"
    GBP = "GBP"
    AUD = "AUD"
    INR = "INR"
    CAD = "CAD"
    ARS = "ARS"
    BRL = "BRL"
    DKK = "DKK"
    HKD = "HKD"
    IDR = "IDR"
    JPY = "JPY"
    KRW = "KRW"
    MYR = "MYR"
    MXN = "MXN"
    NZD = "NZD"
    NOK = "NOK"
    RUB = "RUB"
    SAR = "SAR"
    ZAR = "ZAR"
    SEK = "SEK"
    CHF = "CHF"
    TWD = "TWD"
    TRY = "TRY"
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'price_per_hour': 'number',
        'currency': 'string'
    }

    attribute_map = {
        'price_per_hour': 'price_per_hour',
        'currency': 'currency'
    }

    def __init__(self, price_per_hour=None, currency=None):  # noqa: E501
        """EstimatedPricingResponse - a model defined in Swagger"""  # noqa: E501
        self._price_per_hour = None
        self._currency = None
        self.discriminator = None
        if price_per_hour is not None:
            self.price_per_hour = price_per_hour
        if currency is not None:
            self.currency = currency

    @property
    def price_per_hour(self):
        """Gets the price_per_hour of this EstimatedPricingResponse.  # noqa: E501


        :return: The price_per_hour of this EstimatedPricingResponse.  # noqa: E501
        :rtype: number
        """
        return self._price_per_hour

    @price_per_hour.setter
    def price_per_hour(self, price_per_hour):
        """Sets the price_per_hour of this EstimatedPricingResponse.


        :param price_per_hour: The price_per_hour of this EstimatedPricingResponse.  # noqa: E501
        :type: number
        """

        self._price_per_hour = price_per_hour

    @property
    def currency(self):
        """Gets the currency of this EstimatedPricingResponse.  # noqa: E501


        :return: The currency of this EstimatedPricingResponse.  # noqa: E501
        :rtype: string
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this EstimatedPricingResponse.


        :param currency: The currency of this EstimatedPricingResponse.  # noqa: E501
        :type: string
        """
        allowed_values = [undefinedundefinedundefinedundefinedundefinedundefinedundefinedundefinedundefinedundefinedundefinedundefinedundefinedundefinedundefinedundefinedundefinedundefinedundefinedundefinedundefinedundefinedundefinedundefined]  # noqa: E501

        self._currency = currency

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
        if not isinstance(other, EstimatedPricingResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other