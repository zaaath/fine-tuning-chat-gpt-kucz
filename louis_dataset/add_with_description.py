from .type_completion import Completions

def get_completions() -> Completions:
  user_input_variants = [
    'add a task to file 2020 taxes with the following description: "Collect all necessary financial documents such as W-2s, 1099s, and receipts for deductions. Decide whether to file manually... You got this!"',
    "Remind me to file 2020 taxes, and add the following to the task:\nCollect all necessary financial documents such as W-2s, 1099s, and receipts for deductions. Decide whether to file manually... You got this!",
    "I need to file 2020 taxes. Attach this:\nCollect all necessary financial documents such as W-2s, 1099s, and receipts for deductions. Decide whether to file manually... You got this!",
  ]
  assistant_reply = '''```python
add_task(title="File 2020 taxes",description="Collect all necessary financial documents such as W-2s, 1099s, and receipts for deductions. Decide whether to file manually... You got this!")
```
'''
  return [{
    "user": user_input,
    "assistant": assistant_reply,
  } for user_input in user_input_variants]
