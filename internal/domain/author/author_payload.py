from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class ListPayload:
    name: Optional[str] = None
    start_birth_date: Optional[datetime] = None
    end_birth_date: Optional[datetime] = None
    page: Optional[int] = None
    limit: Optional[int] = None