# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.paging import Paging  # noqa: F401,E501
from swagger_server.models.person import Person  # noqa: F401,E501
from swagger_server import util


class PagedPersons(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, items: List[Person]=None, paging: Paging=None):  # noqa: E501
        """PagedPersons - a model defined in Swagger

        :param items: The items of this PagedPersons.  # noqa: E501
        :type items: List[Person]
        :param paging: The paging of this PagedPersons.  # noqa: E501
        :type paging: Paging
        """
        self.swagger_types = {
            'items': List[Person],
            'paging': Paging
        }

        self.attribute_map = {
            'items': 'items',
            'paging': 'paging'
        }

        self._items = items
        self._paging = paging

    @classmethod
    def from_dict(cls, dikt) -> 'PagedPersons':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PagedPersons of this PagedPersons.  # noqa: E501
        :rtype: PagedPersons
        """
        return util.deserialize_model(dikt, cls)

    @property
    def items(self) -> List[Person]:
        """Gets the items of this PagedPersons.


        :return: The items of this PagedPersons.
        :rtype: List[Person]
        """
        return self._items

    @items.setter
    def items(self, items: List[Person]):
        """Sets the items of this PagedPersons.


        :param items: The items of this PagedPersons.
        :type items: List[Person]
        """

        self._items = items

    @property
    def paging(self) -> Paging:
        """Gets the paging of this PagedPersons.


        :return: The paging of this PagedPersons.
        :rtype: Paging
        """
        return self._paging

    @paging.setter
    def paging(self, paging: Paging):
        """Sets the paging of this PagedPersons.


        :param paging: The paging of this PagedPersons.
        :type paging: Paging
        """

        self._paging = paging