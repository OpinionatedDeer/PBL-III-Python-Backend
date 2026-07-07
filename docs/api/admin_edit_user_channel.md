# POST /admin/edit_user_channel

## Method

**POST**

## Auth

Requires `sys_admin` role

## Request

```json
{
  "channel_id": 1,
  "user_id": 2,
  "status": "active",
  "permission": 255
}
```

## Response `200`

```json
{
  "msg": "Updated User Channel relation"
}
```

## Response `403`

```json
{
  "detail": "Check channel status"
}
```

## Response `403`

```json
{
  "detail": "Check user status"
}
```

## Notes

- Creates or updates the link between a user and a channel
- `status` must be one of: `active`, `banned`, `deleted`
- `permission` is a bitmask integer (see bit index table below)
- Channel must have `status = "active"` and user must have `status = "active"` to proceed

### Permission Bits

| Bit | Permission      |
| --- | --------------- |
| 1   | (reserved)      |
| 2   | Read messages   |
| 3   | Send messages   |
| 4   | Delete own      |
| 5   | (reserved)      |
| 6   | (reserved)      |
| 7   | View deleted    |
| 8   | View edit chain |
| 9   | Delete any      |
