# POST /admin/add_channel

## Method

**POST**

## Auth

Requires `sys_admin` role

## Request

```json
{
  "name": "general",
  "status": "active"
}
```

## Response `200`

```json
{
  "msg": "Channel general created successfully"
}
```

## Response `403`

```json
{
  "detail": "Channel Name already exists"
}
```

## Notes

- `status` must be one of: `active`, `banned`, `deleted`
