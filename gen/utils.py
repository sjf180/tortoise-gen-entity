from typing import Any, Tuple


class colors:
    bs = '\033[1m'
    be = '\033[0;0m'
    yellow = "\u001b[33m"
    blue = "\u001b[34m"
    green = "\u001b[32m"


def tuple_to_str(x: Tuple[Any, Any]) -> str: return f"{x[0]}={x[1]}"
