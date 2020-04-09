# Example python code to access SAP EWM system using odata

This package contains python3 example code for accessing an SAP EWM system.

## Setup

Download the EWM cloud robotics package from https://github.com/SAP/ewm-cloud-robotics, for instance using
```
git clone https://github.com/SAP/ewm-cloud-robotics.git
```

Install the python modules `robcoewminterface` and `robcoewmtypes` using the following commands:

```
(cd python-modules/robcoewminterface && sudo pip3 install .)
(cd python-modules/robcoewmtypes && sudo pip3 install .)
```

In order to provide the credentials to the EWM system, you have to set the following environment variables:
* `EWM_HOST`: the host name of your EWM system; if your system only support http, you have to specify the protocol part as well, otherwise the hostname itself is sufficient. Examples: `vhcalx19ci.dummy.nodomain:4300` or `http://vhcalx19ci.dummy.nodomain:8000`.
* `EWM_BASEPATH`: this is the path to the root of your OData service, which is appended to the host address in the resulting odata url; example `/sap/opu/odata/sap/zewm_robco_srv/`.
* `EWM_AUTH`: either `Basic` or `OAuth`; depending on this setting, you have to provide different environment variables:
  * for `Basic` authentication you need to set `EWM_USER` and `EWM_PASSWORD`
  * for `OAuth` authentication you need to set `EWM_CLIENTID`, `EWM_CLIENTSECRET`, and `EWM_TOKENENDPOINT`.


You should be able to use the code provided in this collection.
