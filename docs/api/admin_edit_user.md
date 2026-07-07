# POST /admin/edit_user

## Method

**POST**

## Auth

Requires `sys_admin` role

## Request

```json
{
  "user_id": 1,
  "email": "updated@example.com",
  "username": "updateduser",
  "user_role": "teacher",
  "status": "active",
  "first_name": "Jane",
  "last_name": "Smith"
}
```

## Response `200`

```json
{
  "msg": "user updateduser edited successfully"
}
```

## Response `404`

```json
{
  "detail": "User not found"
}
```

## Notes

- `status` must be one of: `active`, `banned`, `deleted`
- `first_name` and `last_name` are optional
- Updates both `user_account` and `user_info` tables
