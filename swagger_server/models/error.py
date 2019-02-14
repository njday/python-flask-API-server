# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Error(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, code: str=None, message: str=None):  # noqa: E501
        """Error - a model defined in Swagger

        :param code: The code of this Error.  # noqa: E501
        :type code: str
        :param message: The message of this Error.  # noqa: E501
        :type message: str
        """
        self.swagger_types = {
            'code': str,
            'message': str
        }

        self.attribute_map = {
            'code': 'code',
            'message': 'message'
        }

        self._code = code
        self._message = message

    @classmethod
    def from_dict(cls, dikt) -> 'Error':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Error of this Error.  # noqa: E501
        :rtype: Error
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self) -> str:
        """Gets the code of this Error.


        :return: The code of this Error.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code: str):
        """Sets the code of this Error.


        :param code: The code of this Error.
        :type code: str
        """
        allowed_values = ["DBERR", "NTERR", "UNERR"]  # noqa: E501
        if code not in allowed_values:
            raise ValueError(
                "Invalid value for `code` ({0}), must be one of {1}"
                .format(code, allowed_values)
            )

        self._code = code

    @property
    def message(self) -> str:
        """Gets the message of this Error.


        :return: The message of this Error.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this Error.


        :param message: The message of this Error.
        :type message: str
        """

        self._message = message
