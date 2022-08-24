""" Copyright (c) 2022 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at
           https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""

from tkinter import wantobjects
import meraki
import xlrd
import credentials
import logging
import sys
import json

# function to return the networkid based of the name
def return_network_id(name):
    global networks

    for network in networks:
        if network["name"] == name:
            return network["id"]

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("meraki_script.log"),
        logging.StreamHandler()
    ]
)

log_str = '*'*15 + ' New Script Run ' + '*'*15
logging.info('')
logging.info('*' * len(log_str))
logging.info(log_str)
logging.info('*' * len(log_str))
logging.info('')

# get the file name
excel_file = "file.xlsx"

dashboard = meraki.DashboardAPI(api_key=credentials.meraki_api_key, print_console=False,output_log=False)

my_orgs = dashboard.organizations.getOrganizations()

for org in my_orgs:
    print("Org name: ", org["name"],"Org ID: ", org["id"])

input_org_id = input("Enter Organization ID: ")

networks = dashboard.organizations.getOrganizationNetworks(organizationId=input_org_id)



# read the workbook, we'll just use the first sheet only
wb = xlrd.open_workbook(excel_file)
sheet = wb.sheet_by_index(0)

# find the column numbers for the serial, network, and tags

for i in range(sheet.ncols):
    if sheet.cell_value(0, i).lower() == "serial":
        sn_col = i
    elif sheet.cell_value(0, i).lower() == "staticip":
        ip_col = i
    elif sheet.cell_value(0, i).lower() == "staticsubnetmask":
        subnet_col = i
    elif sheet.cell_value(0, i).lower() == "staticgatewayip":
        gateway_col = i
    elif sheet.cell_value(0, i).lower() == "vlan":
        vlan_col = i
    elif sheet.cell_value(0, i).lower() == "staticdns":
        dns_col = i

# add all the entries to a list of dictionaries to reference later
ap_list = []

for i in range(1, sheet.nrows):
    ap = {}

    ap["serial"] = sheet.cell_value(i, sn_col)
    ap["staticIp"] = sheet.cell_value(i, ip_col)
    ap["staticSubnetMask"] = sheet.cell_value(i, subnet_col)
    ap["staticGatewayIp"] = sheet.cell_value(i, gateway_col)
    ap["vlan"] = sheet.cell_value(i, vlan_col)
    ap["staticDns"] = sheet.cell_value(i, dns_col)


    ap_list.append(ap)

for row in ap_list:
    # update the device's tags
    print(row)
    if row["vlan"] == "None":
        row["vlan"] = None
    else:
        row["vlan"] = int(row["vlan"])

    
    wan1={
            'wanEnabled': 'enabled', 
            'usingStaticIp': True, 
            'staticIp': row["staticIp"], 
            'staticSubnetMask': row["staticSubnetMask"], 
            'staticGatewayIp': row["staticGatewayIp"], 
            'staticDns': [row["staticDns"]], 
            'vlan': row["vlan"]
        } 

    try:
        resp = dashboard.devices.updateDeviceManagementInterface(serial=row["serial"],wan1=wan1)
        print(resp)
        logging.info(resp)

        rb = dashboard.devices.rebootDevice(serial=row["serial"])
    except Exception as e:
        logging.error('e')
        print(e)
