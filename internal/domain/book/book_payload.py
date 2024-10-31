from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class ListPayload:
    title: Optional[str] = None
    description: Optional[str] = None
    start_publish_date: Optional[datetime] = None
    end_publish_date: Optional[datetime] = None
    page: Optional[int] = None
    limit: Optional[int] = None