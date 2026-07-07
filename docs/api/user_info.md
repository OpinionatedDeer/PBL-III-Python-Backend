# GET /user/{user_id}/info

## Method

**GET**

## Auth

Requires valid JWT token

- Users can only view their own info
- `sys_admin` can view any user's info

## Request

Path param: `user_id` (int)

## Response `200`

```json
{
  "email": "user@example.com",
  "username": "someuser",
  "role": "student",
  "first_name": "John",
  "last_name": "Doe"
}
```

## Response `403`

```json
{
  "detail": "Forbidden"
}
```

## Response `404`

```json
{
  "detail": "User not found"
}
```

## Notes

- Joins `user_account` with `user_info` table
- `first_name` and `last_name` default to empty string if null in DB
