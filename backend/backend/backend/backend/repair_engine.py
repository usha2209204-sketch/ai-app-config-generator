def repair_schema(schema, errors):

    if "ui missing" in errors:
        schema["ui"] = {}

    if "api missing" in errors:
        schema["api"] = {}

    return schema
