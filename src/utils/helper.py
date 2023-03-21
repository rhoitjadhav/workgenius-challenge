# Packages
import random
import string
from typing import Optional, Any
from dataclasses import dataclass, field


@dataclass
class ReturnValue:
    """
    ReturnValue class is responsible for holding returned value from operations

    Args:
        status: True if operation is successful otherwise False
        http_code: HTTP status code
        message: message after successful operation
        error: error message after failed operation
        data: resulted data after operation completion
    """
    status: bool = True
    http_code: Optional[int] = -1
    message: str = ""
    error: str = ""
    data: Any = field(default_factory=list)


class Helper:
    @staticmethod
    def random_str(length: int = 6) -> str:
        """
        Generates random string of specified length
        Args:
            length: number of characters in a string

        Returns:
            Random String
        """
        return ''.join(random.choices(string.ascii_uppercase +
                                      string.digits, k=length))
