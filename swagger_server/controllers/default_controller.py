import connexion
import six

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.person import Person  # noqa: E501
from swagger_server.models.persons import Persons  # noqa: E501
from swagger_server import util


def persons_get(pageSize=None, pageNumber=None):  # noqa: E501
    """Return some persons

    Returns a list containing many persons # noqa: E501

    :param pageSize: number of persons returned
    :type pageSize: int
    :param pageNumber: Page number
    :type pageNumber: int

    :rtype: Persons
    """
    return 'do some magic!'


def persons_post(person=None):  # noqa: E501
    """create a person

    send a person to be made # noqa: E501

    :param person: person to create
    :type person: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        person = Person.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def persons_username_friends_get(username, pageSize=None, pageNumber=None):  # noqa: E501
    """Gets a person&#39;s friends

    Returns a list containing all persons. The list supports paging. # noqa: E501

    :param username: the persons name
    :type username: str
    :param pageSize: number of persons returned
    :type pageSize: int
    :param pageNumber: Page number
    :type pageNumber: int

    :rtype: None
    """
    return 'do some magic!'


def persons_username_get(username):  # noqa: E501
    """gets specific person

    returns a single person for its username # noqa: E501

    :param username: the persons name
    :type username: str

    :rtype: Person
    """
    return 'do some magic!'
