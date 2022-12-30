# Introduction
* Follow the guide on https://www.bitdefender.com/business/support/en/77211-204098-azure-sentinel.html
* Get the information needed
    * Get the workspace id from the Log analytics workspace (you can find it under Agents management - Log Analytics agent instructions)
        * Type: UUID - Example: ab15c085-9126-7b22-9af2-000161ddd915
    * Get the workspace secret from the Log analytics workspace
        * Type: str - Example: c1DDZdCWYo676w2rzCHoGvGZ0psF8C3qdPcsQPlXzhC+fFne0QmU6dwM7bWDWxGbLVzdifnJWWSp0tBQ+TGqPv==
    * Create the bitdefender API key as described in the guide (You need to append : to the key)
        * Type: str - Example: 67127ca91ga01a350442d3d093d1235298c001a8db76b38ce995dd8cf6d1ab02:

* The BitDefenderSettings config.ini file should look like this:

```
[BitDefenderSettings]
_workspace_id = ab15c085-9126-7b22-9af2-000161ddd915
_workspace_secret = c1DDZdCWYo676w2rzCHoGvGZ0psF8C3qdPcsQPlXzhC+fFne0QmU6dwM7bWDWxGbLVzdifnJWWSp0tBQ+TGqPv==
_bitdefender_key = 67127ca91ga01a350442d3d093d1235298c001a8db76b38ce995dd8cf6d1ab02:
_workspace_url = https://{workspaceid}.ods.opinsights.azure.com/api/logs?api-version=2016-04-01
```

* Then you can run python bitdefender.py and it will automatically use the variables in the config.ini file.
* If you want to change event that is subscribed to change the subscribeToEventTypes in the create_payload() method located in bitdefender.py