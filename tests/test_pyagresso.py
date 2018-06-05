import os
import pytest
from pyagresso.queryengineservice import QueryEngineService, AgressoRequestType
import sys

from collections import namedtuple


class TestPyAgresso(object):
    username = os.getenv('AGRESSO_USERNAME')
    password = os.getenv('AGRESSO_PASSWORD')
    client = os.getenv('AGRESSO_CLIENT')
    instance_url = os.getenv('AGRESSO_INSTANCE_URL')

    def test_constructor(self):
        ag = QueryEngineService(username=self.username, password=self.password,
                                client=self.client, instance_url=self.instance_url)
        # returns object when compulsory args values are given
        assert ag is not None
        # throws exception if one of username, password or client is missing
        with pytest.raises(ValueError) as te:
            ag = QueryEngineService(
                password=self.password, client=self.client, instance_url=self.instance_url)

    def test_request_builder_about(self):
        ag = QueryEngineService(username=self.username, password=self.password, client=self.client,
                                instance_url=self.instance_url)
        well_formed_request = ag._request_builder('About', '<quer:About/>')
        expected_headers = {'Content-Type': 'text/xml;charset=UTF-8', 'Accept-Encoding': 'gzip,deflate',
                            'SOAPAction': 'https://services.agresso.com/QueryEngineService/QueryEngineV201101/About'}
        expected_data = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:quer="http://services.agresso.com/QueryEngineService/QueryEngineV201101">
                                <soapenv:Header/>
                                <soapenv:Body>
                                    <quer:About/>
                                </soapenv:Body>
                            </soapenv:Envelope>"""
        assert well_formed_request.data is not None, "request_builder didn't return valid data"
        assert well_formed_request.headers is not None, "request_builder didn't return valid headers"
        assert well_formed_request.headers, expected_headers
        assert expected_data.strip().replace(
            '\n', '') in well_formed_request.data.strip().replace('\n', '')
