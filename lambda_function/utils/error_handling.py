def format_error_message(exception):
    return {
        "error": type(exception).__name__,
        "message": str(exception)
    }

class AthenaQueryError(Exception):
    """
    Custom exception for Athena-related operations.
    """
    def __init__(self, message, query_execution_id=None):
        """
        Initialize AthenaException.

        Parameters:
        - message: Description of the error.
        - query_execution_id: ID of the Athena query that caused the exception (if applicable).
        """
        self.message = message
        self.query_execution_id = query_execution_id
        super().__init__(self.message)

    def __str__(self):
        return f"[QueryExecutionId: {self.query_execution_id}] {self.message}" if self.query_execution_id else self.message

class InputValidationError(Exception):
    """
    Custom exception for input validation errors.
    """
    def __init__(self, message, input_name=None, expected_value=None, received_value=None):
        """
        Initialize InputValidationError.

        Parameters:
        - message: Description of the validation error.
        - input_name: Name of the input parameter that caused the error.
        - expected_value: What value or range was expected for the input.
        - received_value: The value that was actually received.
        """
        self.message = message
        self.input_name = input_name
        self.expected_value = expected_value
        self.received_value = received_value
        super().__init__(self.message)

    def __str__(self):
        base_msg = self.message
        if self.input_name:
            base_msg += f" | Input: {self.input_name}"
        if self.expected_value:
            base_msg += f" | Expected: {self.expected_value}"
        if self.received_value:
            base_msg += f" | Received: {self.received_value}"
        return base_msg


def validate_date_format(date_str):
    """
    Validates if the given string is in the 'YYYY-MM-DD' format.
    """
    if not isinstance(date_str, str) or not re.match(r'\d{4}-\d{2}-\d{2}', date_str):
        raise InputValidationError("Invalid date format", "date_str", "YYYY-MM-DD", date_str)
