#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2019 SAP SE or an SAP affiliate company. All rights reserved.
#
# This file is licensed under the Apache Software License, v. 2 except as noted
# otherwise in the LICENSE file (https://github.com/SAP/ewm-cloud-robotics/blob/master/LICENSE)
#
"""Test the OData connection to the EWM system

This is a very basic test script to test and explore the odata services available in the SAP system.


"""

import json

from odata import ODataHandler

def test_service_endpoint(service, endpoint="", urlparams={}, sap_client = '100', print_result=False):
    """Simple test function for odata service"""
    odatahandler = ODataHandler()
    slash = "" if endpoint == "" else "/"
    service_endpoint = "/%s%s%s" % (service, slash, endpoint)
    
    urlparams0 = { 'sap-client': sap_client }
    for p in urlparams:
        urlparams0[p] = urlparams[p]
        
    resp = odatahandler.http_get(service_endpoint, urlparams=urlparams0)
    #print('status: %d' % resp.status_code)
    jsonobj = json.loads(resp.content)
    if print_result:
        print(json.dumps(jsonobj,indent=2))
    return jsonobj;
    

if __name__ == '__main__':


    # some example calls:

    # get endpoints for robcoewm service
    test_service_endpoint("zewm_robco_srv");

    # get all open warehouse tasks
    test_service_endpoint("zewm_robco_srv", "OpenWarehouseTaskSet")

    # get all storage bins
    test_service_endpoint("zewm_robco_srv", "StorageBinSet", print_result = False)

    # get endpoint for the md_product_op_srv service
    test_service_endpoint("md_product_op_srv", print_result = False)

    # get information about products
    test_service_endpoint("md_product_op_srv", "C_Product",
                          urlparams = {
                              "$top" : 10,
                          }, print_result = False)

    
    test_service_endpoint("billofmaterialv2_srv","I_Material",
                          urlparams = {
                              "$top": 10,
                          }, print_result = True)

