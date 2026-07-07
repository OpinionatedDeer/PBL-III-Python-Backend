# POST /admin/add_user

## Method

**POST**

## Auth

Requires `sys_admin` role

## Request

```json
{
  "email": "newuser@example.com",
  "username": "newuser",
  "password": "securepass123",
  "role": "student",
  "first_name": "John",
  "last_name": "Doe"
}
```

## Response `200`

```json
{
  "msg": "user newuser created successfully"
}
```

## Response `403`

```json
{
  "detail": "Email or username already exists"
}
```

## Notes

- `role` must be one of: `sys_admin`, `teacher`, `student`
- `username` must be 4-64 characters
- `password` must be 8-64 characters
- `first_name` and `last_name` must be 1-64 characters
