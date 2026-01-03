"""Contains all the exceptions used by the package"""
class TestFailed(Exception):
    """Exception raised when a test fails"""
    def __init__(self, message: str) -> None:
        self.message = message
    def __str__(self) -> str:
        return self.message