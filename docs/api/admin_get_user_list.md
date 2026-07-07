# GET /admin/get_user_list

## Method

**GET**

## Auth

Requires `sys_admin` role

## Request

No body. Auth token only.

## Response `200`

```json
{
  "users": [
    {
      "id": 1,
      "username": "admin",
      "email": "admin@gmail.com",
      "status": "active",
      "user_role": "sys_admin",
      "first_name": "System",
      "last_name": "Admin"
    }
  ]
}
```

## Notes

- Returns all users with their joined `user_info` data
