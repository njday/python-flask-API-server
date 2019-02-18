import connexion
import six

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.person import Person  # noqa: E501
from swagger_server.models.persons import Persons  # noqa: E501
from swagger_server import util
from flask import request, abort, Response, jsonify
import json

local_list_people = []


def persons_get(pageSize=None, pageNumber=None):  # noqa: E501
    """Return some persons

    Returns a list containing many persons # noqa: E501

    :param pageSize: number of persons returned
    :type pageSize: int
    :param pageNumber: Page number
    :type pageNumber: int

    :rtype: Persons
    """
    message = "No people exist"
    error = "500"

    if len(local_list_people) > 0:
        message = jsonify(items=local_list_people)
        error = "204"

    return Response(message, mimetype='application/json', status=204)


def persons_post(person=None):  # noqa: E501
    """create a person

    send a person to be made # noqa: E501
    :param person: person to create
    :type person: dict | bytes
    :rtype: None
    """
    message = "Could not create person: "
    error = "500"
    if person is None:
        message = +"No person specified"

    # if person == json.
    # handle the json
    if connexion.request.is_json:
        person = Person.from_dict(connexion.request.get_json())  # noqa: E501
        local_list_people.append(person)
        message = jsonify(item=person)
        error = "204"

    return Error(code=error, message=message)


def persons_username_delete(username):  # noqa: E501
    """persons_username_delete

     # noqa: E501

    :param username: the persons name
    :type username: str

    :rtype: None
    """
    message = str(username)
    error = '500'
    for x in local_list_people:
        if local_list_people[x].username == username:
            local_list_people.pop(x)
            error = '204'
            message = +" was deleted succesfully"

    return Response(message)


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
    message = username + " could not be deleted"
    error = '500'
    for x in local_list_people:
        if local_list_people[x].username == username:
            local_list_people.pop(x)
            error = '204'
            message = username + " was deleted succesfully"

    return Error(code=error, message=message)
