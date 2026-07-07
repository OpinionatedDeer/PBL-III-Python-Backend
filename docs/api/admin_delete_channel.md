# POST /admin/delete_channel

## Method

**POST**

## Auth

Requires `sys_admin` role

## Request

```json
{
  "channel_id": 1,
  "name": "general"
}
```

## Response `200`

```json
{
  "msg": "Channel general Deleted successfully"
}
```

## Notes

- Soft delete — sets channel `status` to `"deleted"`
