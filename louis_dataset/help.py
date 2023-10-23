from .type_completion import Completions

def get_completions() -> Completions:
  completions = get_completions_for_help_basic() +\
    get_completions_for_add() +\
    get_completions_for_search()
  return completions

def get_completions_for_help_basic() -> Completions:
  user_input_variants = [
    "help",
    "What can I do here?",
    "how to proceed?",
  ]
  assistant_reply = '''```python
help()
```
'''
  return [{
    "user": user_input,
    "assistant": assistant_reply,
  } for user_input in user_input_variants]

def get_completions_for_add() -> Completions:
  user_input_variants = [
    "how to add a task?",
    "How to configure a newly created task?",
    "show examples of how to add a task",
  ]
  assistant_reply = '''```python
help("add_task")
```
'''
  return [{
    "user": user_input,
    "assistant": assistant_reply,
  } for user_input in user_input_variants]

def get_completions_for_search() -> Completions:
  user_input_variants = [
    "how to search tasks?",
    "How to configure search filters?",
    "Show examples of how to use search",
  ]
  assistant_reply = '''```python
help("search_tasks")
```
'''
  return [{
    "user": user_input,
    "assistant": assistant_reply,
  } for user_input in user_input_variants]
