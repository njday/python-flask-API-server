# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.person import Person  # noqa: F401,E501
from swagger_server import util


class Persons(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, items: List[Person]=None):  # noqa: E501
        """Persons - a model defined in Swagger

        :param items: The items of this Persons.  # noqa: E501
        :type items: List[Person]
        """
        self.swagger_types = {
            'items': List[Person]
        }

        self.attribute_map = {
            'items': 'items'
        }

        self._items = items

    @classmethod
    def from_dict(cls, dikt) -> 'Persons':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Persons of this Persons.  # noqa: E501
        :rtype: Persons
        """
        return util.deserialize_model(dikt, cls)

    @property
    def items(self) -> List[Person]:
        """Gets the items of this Persons.


        :return: The items of this Persons.
        :rtype: List[Person]
        """
        return self._items

    @items.setter
    def items(self, items: List[Person]):
        """Sets the items of this Persons.


        :param items: The items of this Persons.
        :type items: List[Person]
        """

        self._items = items
