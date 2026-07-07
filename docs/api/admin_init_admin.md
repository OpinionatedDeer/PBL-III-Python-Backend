# GET /admin/init_admin

## Method

**GET**

## Auth

None

## Request

No body. No auth required.

## Response `200`

```json
{
  "msg": "Admin user created successfully"
}
```

## Response `200` (already exists)

```json
{
  "msg": "Admin already exists"
}
```

## Notes

- Creates a default admin with:
  - Email: `admin@gmail.com`
  - Username: `admin`
  - Password: `admin@1234`
  - Role: `sys_admin`
- Idempotent — safe to call multiple times
- Intended for initial setup / emergency admin recovery
