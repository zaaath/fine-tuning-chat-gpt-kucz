from .type_completion import Completions

def get_completions() -> Completions:
  user_input_variants = [
    "add a task to file 2020 taxes",
    "Remind me to file 2020 taxes",
    "I need to file 2020 taxes",
  ]
  assistant_reply = '''```python
add('File 2020 taxes')
```
'''
  return [{
    "user": user_input,
    "assistant": assistant_reply,
  } for user_input in user_input_variants]
