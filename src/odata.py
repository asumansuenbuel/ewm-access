# encoding: utf-8
#
# Copyright (c) 2019 SAP SE or an SAP affiliate company. All rights reserved.
#
# This file is licensed under the Apache Software License, v. 2 except as noted
# otherwise in the LICENSE file (https://github.com/SAP/ewm-cloud-robotics/blob/master/LICENSE)
#
"""Specialized/patched version of the OData connector class"""

import os
from typing import Optional, Dict

from robcoewminterface.types import ODataConfig
from robcoewminterface.odata import ODataHandler as ODataHandlerOrig
from robcoewminterface.odata import prepare_ids_str, prepare_params_dict

class ODataHandler(ODataHandlerOrig):

    def __init__(self):
        odata_config = self._get_config_from_env()
        super().__init__(config=odata_config)

    def _get_config_from_env(self):
        """Get the OData settings from environment variables"""
        # Read environment variables
        envvar = {}
        envvar['EWM_HOST'] = os.environ.get('EWM_HOST')
        envvar['EWM_BASEPATH'] = os.environ.get('EWM_BASEPATH')
        envvar['EWM_AUTH'] = os.environ.get('EWM_AUTH')
        if envvar['EWM_AUTH'] == ODataConfig.AUTH_BASIC:
            envvar['EWM_USER'] = os.environ.get('EWM_USER')
            envvar['EWM_PASSWORD'] = os.environ.get('EWM_PASSWORD')
        else:
            envvar['EWM_CLIENTID'] = os.environ.get('EWM_CLIENTID')
            envvar['EWM_CLIENTSECRET'] = os.environ.get('EWM_CLIENTSECRET')
            envvar['EWM_TOKENENDPOINT'] = os.environ.get('EWM_TOKENENDPOINT')

        # Check if complete
        for var, val in envvar.items():
            if val is None:
                raise ValueError(
                    'Environment variable "{}" is not set'.format(var))

        if envvar['EWM_AUTH'] == ODataConfig.AUTH_BASIC:
            odataconfig = ODataConfig(
                host=envvar['EWM_HOST'],
                basepath=envvar['EWM_BASEPATH'],
                authorization=envvar['EWM_AUTH'],
                user=envvar['EWM_USER'],
                password=envvar['EWM_PASSWORD'],
                )
        else:
            odataconfig = ODataConfig(
                host=envvar['EWM_HOST'],
                basepath=envvar['EWM_BASEPATH'],
                authorization=envvar['EWM_AUTH'],
                clientid=envvar['EWM_CLIENTID'],
                clientsecret=envvar['EWM_CLIENTSECRET'],
                tokenendpoint=envvar['EWM_TOKENENDPOINT'],
                )

        return odataconfig

    def prepare_uri(
            self, endpoint: str, ids: Optional[Dict], navigation: Optional[str] = None) -> str:
        """Prepare URI for OData call; patched version to allow http calls"""
        # Create IDs string for endpoint
        ids_str = prepare_ids_str(ids)

        if self._config.host.startswith('http'):
            ph = self._config.host
        else:
            ph = 'https://{h}'.format(h=self._config.host)
            
        if ids_str is None:
            # Create URI without ID string
            uri = '{h}{bp}{ep}'.format(
                h=ph, bp=self._config.basepath, ep=endpoint)
        else:
            # Create URI with ID string
            uri = '{h}{bp}{ep}{id}'.format(
                h=ph, bp=self._config.basepath, ep=endpoint, id=ids_str)

        if navigation is not None:
            uri = uri + navigation

        return uri
