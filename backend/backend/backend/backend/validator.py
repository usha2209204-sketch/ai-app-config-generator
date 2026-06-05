def validate_schema(schema):

    errors = []

    required = [
        "ui",
        "api",
        "database",
        "auth"
    ]

    for field in required:
        if field not in schema:
            errors.append(f"{field} missing")

    return errors
