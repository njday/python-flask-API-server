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
        query_string = [('pageSize', 100),
                        ('pageNumber', 56)]
        response = self.client.open(
            '/openapi101/persons',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_persons_post(self):
        """Test case for persons_post
        Creates a person.
        """
        person = Person()
        person.username = "username_example"
        response = self.client.open(
            '/openapi101/persons',
            method='POST',
            data=json.dumps(person),
            content_type='application/json')
        self.assertStatus(response, 204,
                          'Response body is : ' + response.data.decode('utf-8'))

    def test_persons_username_delete(self):
        """Test case for persons_username_delete
        Deletes a person.
        """
        response = self.client.open(
            '/openapi101/persons/{username}'.format(username='username_example'),
            method='DELETE')
        self.assertStatus(response, 204,
                          'Response body is : ' + response.data.decode('utf-8'))

    def test_persons_username_get(self):
        """Test case for persons_username_get
        Gets a specific person
        """
        response = self.client.open(
            '/openapi101/persons/{username}'.format(username='username_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest

    unittest.main()
