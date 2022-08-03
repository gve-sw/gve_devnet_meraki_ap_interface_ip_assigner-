# gve_devnet_meraki_ap_interface_ip_assigner-
prototype script that reads information like serial # and IP address to assign from an Excel file then statically assigns the IP address for AP wan interfaces. 


## Contacts
* Jorge Banegas

## Solution Components
* Python
* Meraki
* MR

## Prerequisites
- **API Key**: In order to use the Meraki API, you need to enable the API for your organization first. After enabling API access, you can generate an API key. Follow these instructions to enable API access and generate an API key:
1. Login to the Meraki dashboard
2. In the left-hand menu, navigate to `Organization > Settings > Dashboard API access`
3. Click on `Enable access to the Cisco Meraki Dashboard API`
4. Go to `My Profile > API access`
5. Under API access, click on `Generate API key`
6. Save the API key in a safe place. The API key will only be shown once for security purposes, so it is very important to take note of the key then. In case you lose the key, then you have to revoke the key and a generate a new key. Moreover, there is a limit of only two API keys per profile.

> For more information on how to generate an API key, please click [here](https://developer.cisco.com/meraki/api-v1/#!authorization/authorization). 
> Note: You can add your account as Full Organization Admin to your organizations by following the instructions [here](https://documentation.meraki.com/General_Administration/Managing_Dashboard_Access/Managing_Dashboard_Administrators_and_Permissions).


## Installation/Configuration

(optional) This first step is optional if the user wants to leverage a virtual environment to install python packages

```shell
pip install virtualenv
virtualenv env
source env/bin/activate
```

Install python dependencies 

```shell
pip install -r requirements.txt
```

Enter API key inside the credentials.py file

```python
    meraki_api_key = ""
```

Make sure to properly include the required details inside file.xlsx. 
Required details include 
- Serial
- Static IP
- Static Subnet Mask
- Static GatewayIp 
- VLAN
- Static DNS

## Usage

To launch script write:


    $ python main.py

Once the script is launched, it will display all your Meraki organizations and prompt to enter one. Once entered, it will read the details from the Excel file and assign the static ip address to all the APs listed.

## Important Notes
Important to not edit any of the columns and their names. Script finds the column location by its column name. 

# Screenshots

![/IMAGES/0image.png](/IMAGES/0image.png)

### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.