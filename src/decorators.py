"""module with decorator functions"""

from functools import wraps
from pathlib import Path
from typing import Callable, ParamSpec, TypeVar

P = ParamSpec("P")
T = TypeVar("T")


def log(filename: str | None = None) -> Callable:
    """decorator for logging function execution"""

    def decorator(function: Callable[P, T]) -> Callable[P, T]:
        @wraps(function)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            if filename is not None:
                file_path = Path(f"{Path(__file__).parent.parent}/logs/{filename}")
                file_path.parent.mkdir(parents=True, exist_ok=True)
            try:
                result = function(*args, **kwargs)
                log_msg = f"{function.__name__} ok"
                if filename is not None:
                    with open(file_path, "a", encoding="utf-8") as log_file:
                        log_file.write(f"{log_msg}\n")
                else:
                    print(log_msg)
                return result
            except Exception as e:
                log_msg = f"{function.__name__} error: {e}. Inputs: {args}, {kwargs}"
                if filename is not None:
                    with open(file_path, "a", encoding="utf-8") as log_file:
                        log_file.write(f"{log_msg}\n")
                else:
                    print(log_msg)
                raise e

        return wrapper

    return decorator
