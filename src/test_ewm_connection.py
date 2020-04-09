#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2019 SAP SE or an SAP affiliate company. All rights reserved.
#
# This file is licensed under the Apache Software License, v. 2 except as noted
# otherwise in the LICENSE file (https://github.com/SAP/ewm-cloud-robotics/blob/master/LICENSE)
#
"""Test the OData connection to the EWM system"""

import json

from odata import ODataHandler

if __name__ == '__main__':

    odatahandler = ODataHandler()

    endpoint = '/StorageBinSet'
    #urlparams = { '$expand': 'StorageBins' }
    #urlparams = { '$expand': "StorageBins", '$filter': "(Lgnum eq '1010')" }
    urlparams = { '$filter': "(Lgnum eq '1710')" }

    resp = odatahandler.http_get(endpoint, urlparams=urlparams)
    print('status: %d' % resp.status_code)
    jsonobj = json.loads(resp.content)
    print(json.dumps(jsonobj,indent=2))

