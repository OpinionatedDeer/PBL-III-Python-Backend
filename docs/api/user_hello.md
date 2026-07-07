# GET /user

## Method

**GET**

## Auth

Requires valid JWT token (any role)

## Request

No body. Auth token only.

## Response `200`

```json
{
  "msg": "Hello admin!"
}
```

## Notes

- Simple health-check / greeting endpoint
- Returns the username from the decoded token
