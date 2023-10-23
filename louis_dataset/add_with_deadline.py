from .type_completion import Completions

def get_completions() -> Completions:
  user_input_variants = [
    "add a task to file 2020 taxes by Friday",
    "Remind me to file 2020 taxes on Friday",
    "I need to file 2020 taxes by Friday",
  ]
  assistant_reply = '''```python
add_task(title="File 2020 taxes",deadline="Friday")
```
'''
  return [{
    "user": user_input,
    "assistant": assistant_reply,
  } for user_input in user_input_variants]
