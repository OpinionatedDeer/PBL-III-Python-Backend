# POST /login

## Method

**POST**

## Auth

None

## Request

```json
{
  "email": "user@example.com",
  "password": "mypassword123"
}
```

## Response `200`

```json
{
  "token": "eyJhbGciOiJIUzI1NiIs..."
}
```

## Response `401`

```json
{
  "detail": "Invalid credentials"
}
```

## Notes

- Password must be 8-64 characters
- Token expires in 200 minutes
- Only accounts with `status = "active"` can log in
- Token payload includes `sub` (user id), `username`, `role`
