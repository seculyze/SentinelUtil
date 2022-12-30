import base64
import requests
from pprint import pprint
import json
import configparser


def read_config(
    config_file: str = "config.ini"
    ):

    config = configparser.ConfigParser()
    config.read(config_file)
    return config


def config_fetcher(
    config_get: str
    ):

    config = read_config()
    return config["BitDefenderSettings"][config_get]


def base64_enc(
    key: str
    ):

    data_bytes = key.encode("ascii")
    encoded_key = base64.b64encode(data_bytes)
    base64_string = encoded_key.decode('ascii')

    return base64_string


def create_headers(
    bitdefender_key=config_fetcher(config_get="_bitdefender_key")
    ):

    auth_string = "Basic {authparams}".format(
        authparams=base64_enc(bitdefender_key)
        )

    headers = {
        "Authorization": auth_string,
        "cache-control": "no-cache",
        "content-type": "application/json"
    }

    return headers


def create_payload(
    workspace_id: str = config_fetcher(config_get="_workspace_id"),
    workspace_secret: str = config_fetcher(config_get="_workspace_secret"),
    workspace_url: str = config_fetcher(config_get="_workspace_url")
    ):

    workspace_url = workspace_url.format(workspaceid=workspace_id)

    payload = {
        "params": {
            "status": 1,
            "serviceType": "azureSentinel",
            "serviceSettings": {
                "workspaceId": workspace_id,
                "sharedKey": workspace_secret,
                "logType": "GZevent",
                "requireValidSslCertificate": False,
                "url": workspace_url
            },
            "subscribeToEventTypes": {
                "hwid-change": True,
                "modules": True,
                "sva": True,
                "registration": True,
                "supa-update-status": True,
                "av": True,
                "aph": True,
                "fw": True,
                "avc": True,
                "uc": True,
                "dp": True,
                "device-control": True,
                "sva-load": True,
                "task-status": True,
                "exchange-malware": True,
                "network-sandboxing": True,
                "malware-outbreak": True,
                "adcloud": True,
                "exchange-user-credentials": True,
                "exchange-organization-info": True,
                "hd": True,
                "antiexploit": True
            }
        },
        "jsonrpc": "2.0",
        "method": "setPushEventSettings",
        "id": "1"
    }

    return payload


def post_bitdefender():
    _BITDEFENDER_JSONRPC_PUSH_URL = "https://cloudgz.gravityzone.bitdefender.com/api/v1.0/jsonrpc/push"
    headers = create_headers()
    payload = create_payload()
    response = requests.post(url=_BITDEFENDER_JSONRPC_PUSH_URL, data=json.dumps(payload), headers=headers)
    pprint(response.text)

if __name__ == "__main__":
    post_bitdefender()
