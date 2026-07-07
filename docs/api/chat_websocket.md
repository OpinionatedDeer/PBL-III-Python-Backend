# WS /chats/{user_id}/ws

## Method

**WebSocket**

## Auth

JWT token passed as query param `token`

Requires `user_id` in path to match `sub` in the token payload.

## Connection

```
ws://host/chats/{user_id}/ws?token=<JWT>
```

## Protocol

All messages are JSON. Every request must include a `request` field identifying the action type.

---

### get_channels

Fetch channels the user belongs to.

#### Request

```json
{
  "request": "get_channels",
  "last_channel_id": null,
  "limit": 20
}
```

#### Response

```json
{
  "request": "get_channels",
  "channels": [
    {
      "channel_id": 1,
      "channel_name": "general",
      "last_message": null,
      "permission": 255
    }
  ]
}
```

---

### load_messages

Load paginated messages in a channel.

#### Request

```json
{
  "request": "load_messages",
  "channel_id": 1,
  "limit": 20,
  "prev_id": null
}
```

- `prev_id`: message ID to load older messages from (cursor-based pagination). Omit or `null` for newest messages.
- `limit`: max messages to return (default 20).

#### Response

```json
{
  "request": "load_messages",
  "messages": [
    {
      "channel_id": 1,
      "message_id": 42,
      "sender_id": 2,
      "sender_name": "john",
      "message": "Hello world",
      "timestamp": "2025-01-15 10:30:00",
      "status": "Normal"
    }
  ]
}
```

#### Status handling

- **Deleted**: Content hidden as `"Message deleted"` unless user has permission bit 7 (view deleted).
- **Edited**: Full edit chain shown if user has permission bit 8. Otherwise only latest version is returned.
- Messages with status `"Edit"` are intermediate versions in the chain (not directly returned).

---

### send_message

Send, edit, or delete a message.

#### Normal (new message)

##### Request

```json
{
  "request": "send_message",
  "channel_id": 1,
  "status": "Normal",
  "message": "Hello everyone"
}
```

##### Response

```json
{
  "type": "send_message",
  "status": "success",
  "id": 42
}
```

Broadcast to other channel members automatically.

#### Edited (edit message)

##### Request

```json
{
  "request": "send_message",
  "channel_id": 1,
  "status": "Edited",
  "message": "Updated text",
  "prev_id": 42
}
```

- `prev_id` is the ID of the message being edited.
- The original message gets `status = "Edited"` and a new message is inserted with `status = "Edit"` and `prev_message_id` pointing to the original.

##### Response

```json
{
  "type": "edited_message",
  "status": "success",
  "id": 43
}
```

#### Deleted (delete message)

##### Request

```json
{
  "request": "send_message",
  "channel_id": 1,
  "status": "Deleted",
  "prev_id": 42
}
```

- `prev_id` is the ID of the message to delete.
- Requires permission bit 4 (delete own) if you are the sender, or bit 9 (delete any) otherwise.
- The message's status is set to `"Deleted"` (soft delete).

##### Response

```json
{
  "type": "delete_message",
  "status": "success",
  "id": 42
}
```

---

### load_users

Fetch users in a channel.

#### Request

```json
{
  "request": "load_users",
  "channel_id": 1
}
```

#### Response

```json
{
  "request": "load_users",
  "users": [
    {
      "user_id": 2,
      "user_name": "john",
      "permission": 255,
      "channel_id": 1
    }
  ]
}
```

Requires read permission (bit 2) in the channel.

---

### Error format

```json
{
  "request": "load_messages",
  "error": "not_in_channel"
}
```

## Permission bits

| Bit | Permission      |
| --- | --------------- |
| 2   | Read messages   |
| 3   | Send messages   |
| 4   | Delete own      |
| 7   | View deleted    |
| 8   | View edit chain |
| 9   | Delete any      |
