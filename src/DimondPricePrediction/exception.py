class CustomException(Exception):
    def __init__(self, message="A custom exception occurred"):
        self.message = message
        super().__init__(self.message)

# Example usage of the custom exception
try:
    # Some code that might raise the custom exception
    raise CustomException("This is a custom exception message")
except CustomException as e:
    print(f"Caught an exception: {e}")
