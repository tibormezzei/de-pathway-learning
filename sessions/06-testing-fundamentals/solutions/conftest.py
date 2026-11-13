def pytest_addoption(parser):
    parser.addoption("--buggy", action="store_true", help="test the exercise (buggy) module instead")
