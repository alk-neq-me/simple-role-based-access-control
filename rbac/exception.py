class NotFoundRole(Exception):
    """Exception not found role name"""


class NotFoundRepo(Exception):
    """Exception not found repo name"""


class FailedPermission(Exception):
    """Exception that failed action type"""


class Forbidden(Exception):
    """Exception not allowed"""
