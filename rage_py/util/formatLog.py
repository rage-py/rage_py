from typing import Literal
from datetime import datetime

def formatLog(content: str, type: Literal["config", "fetch", "push", "new", "warning", "error", "final"], logger: bool = True) -> None:
    flag = "[CONFIG]"
    
    if type == "config": flag = "(CONFIG)"
    elif type == "fetch": flag = "(FETCH)"
    elif type == "push": flag = "(PUSH)"
    elif type == "new": flag = "(NEW)"
    elif type == "warning": flag = "(WARNING)"
    elif type == "error": flag = "(ERROR)"
    elif type == "final": flag = "(FINAL)"

    # Get current time
    currentTime = datetime.now()
    formattedTime = currentTime.strftime("[%H:%M:%S]")

    print(f"{flag} {formattedTime} {content}")

    return
