def response_ok_pattern(message):
    return {
        "status": "success",
        "message": message
    }

def response_error_pattern(message):
    return {
        "status": "error",
        "message": message
    }