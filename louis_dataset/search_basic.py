from .type_completion import Completions

def get_completions() -> Completions:
  user_input_variants = [
    "find tasks that mention taxes",
    "List all tasks related to taxes",
    "help me find all tasks related to taxes",
  ]
  assistant_reply = '''```python
search_tasks(task_title='tax')
```
'''
  return [{
    "user": user_input,
    "assistant": assistant_reply,
  } for user_input in user_input_variants]
