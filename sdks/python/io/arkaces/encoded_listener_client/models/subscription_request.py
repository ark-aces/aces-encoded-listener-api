# coding: utf-8

"""
    Aces Encoded Listener API

    API Specification for Encoded Listeners that read data on a blockchain and forward transaction events to registered subscribers. 

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class SubscriptionRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'callback_url': 'str',
        'min_confirmations': 'int'
    }

    attribute_map = {
        'callback_url': 'callbackUrl',
        'min_confirmations': 'minConfirmations'
    }

    def __init__(self, callback_url=None, min_confirmations=None):
        """
        SubscriptionRequest - a model defined in Swagger
        """

        self._callback_url = None
        self._min_confirmations = None
        self.discriminator = None

        self.callback_url = callback_url
        self.min_confirmations = min_confirmations

    @property
    def callback_url(self):
        """
        Gets the callback_url of this SubscriptionRequest.
        Target target URL to POST Encoded Listener events to.

        :return: The callback_url of this SubscriptionRequest.
        :rtype: str
        """
        return self._callback_url

    @callback_url.setter
    def callback_url(self, callback_url):
        """
        Sets the callback_url of this SubscriptionRequest.
        Target target URL to POST Encoded Listener events to.

        :param callback_url: The callback_url of this SubscriptionRequest.
        :type: str
        """
        if callback_url is None:
            raise ValueError("Invalid value for `callback_url`, must not be `None`")

        self._callback_url = callback_url

    @property
    def min_confirmations(self):
        """
        Gets the min_confirmations of this SubscriptionRequest.
        Confirmations required before event is sent to subscriber.

        :return: The min_confirmations of this SubscriptionRequest.
        :rtype: int
        """
        return self._min_confirmations

    @min_confirmations.setter
    def min_confirmations(self, min_confirmations):
        """
        Sets the min_confirmations of this SubscriptionRequest.
        Confirmations required before event is sent to subscriber.

        :param min_confirmations: The min_confirmations of this SubscriptionRequest.
        :type: int
        """
        if min_confirmations is None:
            raise ValueError("Invalid value for `min_confirmations`, must not be `None`")

        self._min_confirmations = min_confirmations

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
        if not isinstance(other, SubscriptionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
