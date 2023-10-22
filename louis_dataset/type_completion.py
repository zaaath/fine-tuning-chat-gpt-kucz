from typing import NamedTuple, List

class Completion(NamedTuple):
  user: str
  assistant: str

Completions = List[Completion]
