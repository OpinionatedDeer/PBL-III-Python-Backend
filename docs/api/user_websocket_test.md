# WS /user/{user_id}/websocketTest

## Method

**WebSocket**

## Auth

JWT token passed in the `Authorization` header or as a query param `token`

Requires `user_id` in path to match `sub` in the token payload.

## Connection

```
ws://host/user/{user_id}/websocketTest?token=<JWT>
```

or with `Authorization` header:

```
ws://host/user/{user_id}/websocketTest2
```

## Messages

### Echo (one-to-one)

Server sends back whatever the client sends:

```json
{
  "id": 123,
  "message": "hello"
}
```

Sent to all connected users except the sender.

## Notes

- Two variants: `websocketTest` (token as query param) and `websocketTest2` (token in header)
- Disconnect closes with code `4001` if token user_id doesn't match
