import unittest

import responses

from query import (
    query_endpoint,
)


class QueryEndpointTests(unittest.TestCase):

    def setUp(self):
        self.test_url = "https://something/1"

    @responses.activate
    def test_query_calls_passed_uri(self):
        responses.add(responses.GET, self.test_url)

        query_endpoint(self.test_url)

        self.assertEqual(1, len(responses.calls))
        self.assertEqual(self.test_url, responses.calls[0].request.url)

    @responses.activate
    def test_query_returns_response_body_if_status_is_200(self):
        responses.add(responses.GET, self.test_url,
                      status=200, json={"a": "1"})

        result = query_endpoint(self.test_url)

        self.assertEqual(result, {"a": "1"})

    @responses.activate
    def test_query_returns_error_if_status_other_than_200(self):
        responses.add(responses.GET, self.test_url, status=500)

        result = query_endpoint(self.test_url)

        self.assertEqual("error", result)

    @responses.activate
    def test_query_returns_error_if_status_is_200_but_non_json_body(self):
        responses.add(responses.GET, self.test_url,
                      status=200, body='just a normal string')

        result = query_endpoint(self.test_url)

        self.assertEqual("error", result)
