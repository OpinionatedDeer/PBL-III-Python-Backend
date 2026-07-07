# GET /admin/get_userinfo_at_channel

## Method

**GET**

## Auth

Requires `sys_admin` role

## Request

No body. Auth token only.

## Response `200`

```json
{
  "UserInfo": [
    {
      "channel_id": 1,
      "channel_name": "general",
      "user_id": 2,
      "username": "student1",
      "status": "active",
      "permission": 255
    }
  ]
}
```

## Notes

- Returns all user-channel relationships across every channel
- Joins `channel_user`, `channel`, and `user_account` tables
