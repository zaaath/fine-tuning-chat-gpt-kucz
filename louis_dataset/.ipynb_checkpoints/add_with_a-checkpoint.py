from .type_completion import Completions

def get_completions() -> Completions:
  user_input_variants = [
    "add a task to file 2020 taxes, assign it to John",
    "Remind John to file 2020 taxes",
    "tell John to file 2020 taxes",
  ]
  assistant_reply = '''
```python
add(task_name='File 2020 taxes',assignee_name="John")
```
'''
  return [{
    "user": user_input,
    "assistant": assistant_reply,
  } for user_input in user_input_variants]
