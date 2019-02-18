# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.person import Person  # noqa: E501
from swagger_server.models.persons import Persons  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_persons_get(self):
        """Test case for persons_get

        Gets some persons
        """
        query_string = [('pageSize', 56),
                        ('pageNumber', 56)]
        response = self.client.open(
            'openai/persons',
            method='GET',
            query_string=query_string)
        self.assert204(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_persons_post(self):
        """Test case for persons_post

        Creates a person
        """
        person = Person()
        person.username = "username_example"
        response = self.client.open(
            '/persons',
            method='POST',
            data=json.dumps(person),
            content_type='application/json')
        self.assertStatus(response, 204,
                          'Response body is : ' + response.data.decode('utf-8'))

    def test_persons_username_delete(self):
        """Test case for persons_username_delete

        Deletes a persons
        """
        response = self.client.open(
            '/persons/{username}'.format(username='username_example'),
            method='DELETE')
        self.assertStatus(response, 204,
                          'Response body is : ' + response.data.decode('utf-8'))

    def test_persons_username_friends_get(self):
        """Test case for persons_username_friends_get

        Gets a person's friends
        """
        query_string = [('pageSize', 56),
                        ('pageNumber', 56)]
        response = self.client.open(
            '/persons/{username}/friends'.format(username='username_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_persons_username_get(self):
        """Test case for persons_username_get

        Gets a person
        """
        person = Person()
        person.username = "username_example"
        response1 = self.client.open(
            '/persons',
            method='POST',
            data=json.dumps(person),
            content_type='application/json')
        self.assertStatus(response1, 204,
                          'Response body is : ' + response1.data.decode('utf-8'))

        response2 = self.client.open(
            '/persons/{username}'.format(username='username_example'),
            method='GET')
        self.assert200(response2,
                       'Response body is : ' + response2.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
