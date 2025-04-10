from pydantic import ValidationError

def format_validation_error(e: ValidationError):
    errors = []
    for error in e.errors():
        errors.append({
            "message": error["msg"],
            "input_value": error.get("input"),
            "type": error["type"],
            "help_url": error.get("url", "https://errors.pydantic.dev/")
        })
    return {
        "error": "Invalid input data",
        "details": errors
    }