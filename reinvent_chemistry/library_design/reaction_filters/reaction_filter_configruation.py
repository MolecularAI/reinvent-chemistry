from dataclasses import dataclass
from typing import List, Dict


@dataclass
class ReactionFilterConfiguration:
    type: str
    reactions: Dict[str, List[str]]
    reaction_definition_file: str = None
