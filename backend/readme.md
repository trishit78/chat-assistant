user:
id (uuid, pk)
email (unique)
password_hash
name
created_at


projects:
id
user_id
title
description
goals (jsonb)
references (jsonb)
created_at


chats:
id
project_id
created_at


messages:
id
chat_id
role (user/assistant/tool)
content
tool_call (jsonb)
created_at


memories:
id
project_id
key
value
embedding (optional if you want RAG)
created_at



images:
id
project_id
url
prompt
analysis
created_at

agent_runs:
id
project_id
status (pending/running/completed/failed)
result
logs
created_at
updated_at