def runtime_validate(schema):

    required = [
        "ui",
        "api",
        "database",
        "auth"
    ]

    for item in required:
        if item not in schema:
            raise Exception(
                f"{item} missing"
            )

    return True
