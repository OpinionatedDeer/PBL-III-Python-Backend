# GET /admin/get_channel_list

## Method

**GET**

## Auth

Requires `sys_admin` role

## Request

No body. Auth token only.

## Response `200`

```json
{
  "channel": [
    {
      "id": 1,
      "name": "general",
      "status": "active"
    }
  ]
}
```
