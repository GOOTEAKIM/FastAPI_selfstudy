from datetime import datetime, time, timedelta
from typing import Annotated, Union
from uuid import UUID

from fastapi import Body, FastAPI

app = FastAPI()

@app.put('/items/{item_id}')
async def read_items(
    item_id: UUID,
    start_datetime: Annotated[datetime, Body()],
    end_datetime: Annotated[datetime, Body()],
    process_after: Annotated[timedelta, Body()],
    repeat_at: Annotated[Union[time,None], Body()] = None
):
    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return{
        'item_id':item_id,
        'start_datetime': start_datetime,
        'end_datetime': end_datetime,
        'process_after':process_after,
        'repeat_at':repeat_at,
        'start_process':start_process,
        'duration':duration
    }

# http://127.0.0.1:8000/items/123e4567-e89b-12d3-a456-426614174000

'''json
{
    "item_id": "123e4567-e89b-12d3-a456-426614174000",
    "start_datetime": "2023-09-04T10:00:00",
    "end_datetime": "2023-09-04T12:00:00",
    "process_after": "PT1H",  // ISO 8601 duration format
    "repeat_at": "15:30:00"
}
'''