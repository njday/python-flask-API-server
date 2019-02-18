import connexion
import six

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.person import Person  # noqa: E501
from swagger_server.models.persons import Persons  # noqa: E501
from swagger_server import util
from flask import request, abort, Response, jsonify
import json

persons_list = []


def persons_get(pageSize=None, pageNumber=None):  # noqa: E501
    """Gets some persons
    Returns a list containing all persons. # noqa: E501
    :param pageSize: Number of persons returned
    :type pageSize: int
    :param pageNumber: Page number
    :type pageNumber: int
    :rtype: Persons
    """
    return jsonify(items=persons_list)
    # return 'do some magic!'


def persons_post(person=None):  # noqa: E501
    """Creates a person.
    Adds a new person to the person list. # noqa: E501
    :param person: The person to create.
    :type person: dict | bytes
    :rtype: None
    """
    if connexion.request.is_json:
        person = Person.from_dict(connexion.request.get_json())  # noqa: E501
    persons_list.append(person)
    return Response('person added!',mimetype='application/json', status=204)
    # return 'do some magic!'


def persons_username_delete(username):  # noqa: E501
    """Deletes a person.
    Delete a single person identified via its username. # noqa: E501
    :param username: The person&#39;s username
    :type username: str
    :rtype: None
    """
    for person in persons_list:
        if (person.username == username):
            persons_list.remove(person)
            return Response('Person deleted!', mimetype='application/json', status=204)

    return Response('person not found!', mimetype='text/plain', status=404)


def persons_username_get(username):  # noqa: E501
    """Gets a specific person
    Returns a single person for its username. # noqa: E501
    :param username: The person&#39;s username
    :type username: str
    :rtype: Person
    """
    for person in persons_list:
        if (person.username == username):
            return person;

    # print(person.username)
    return 'person not found!'


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
