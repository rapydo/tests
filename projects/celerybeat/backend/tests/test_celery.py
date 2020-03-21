# -*- coding: utf-8 -*-

# import time
from restapi.tests import BaseTests, API_URI
from restapi.utilities.htmlcodes import hcodes
# from restapi.utilities.logs import log


class TestApp(BaseTests):

    def test_01_x(self, app, client):

        endpoint = API_URI + '/tests/1'
        r = client.get(endpoint)
        assert r.status_code == hcodes.HTTP_OK_BASIC

        endpoint = API_URI + '/tests/2'
        r = client.get(endpoint)
        assert r.status_code == hcodes.HTTP_OK_BASIC

        assert self.get_content(r) == "1"
