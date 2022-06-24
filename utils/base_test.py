import pytest

@pytest.mark.usefixtures("browser", "config", "user")
class BaseTest:
    pass