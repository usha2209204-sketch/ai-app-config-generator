def generate_schema(design):

    return {

        "ui": {
            "pages": [
                "dashboard",
                "contacts"
            ]
        },

        "api": {
            "endpoints": [
                "/login",
                "/contacts"
            ]
        },

        "database": {
            "tables": [
                "users",
                "contacts"
            ]
        },

        "auth": {
            "roles": [
                "admin",
                "user"
            ]
        }
    }
