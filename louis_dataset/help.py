from .type_completion import Completions

def get_completions() -> Completions:
  user_input_variants = [
    "help",
    "What can I do here?",
    "how to proceed?"
  ]
  assistant_reply = '''```python
help()
```
'''
  return [{
    "user": user_input,
    "assistant": assistant_reply,
  } for user_input in user_input_variants]
