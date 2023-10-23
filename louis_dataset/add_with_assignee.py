from .type_completion import Completions

def get_completions() -> Completions:
  user_input_variants = [
    "add a task to file 2020 taxes, assign it to John Doe",
    "Remind John Doe to file 2020 taxes",
    "tell John Doe to file 2020 taxes",
  ]
  assistant_reply = '''```python
add_task(title="File 2020 taxes",assignee_name="John Doe")
```
'''
  return [{
    "user": user_input,
    "assistant": assistant_reply,
  } for user_input in user_input_variants]
