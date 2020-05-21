import pytest
from pkg_resources import resource_filename

yaml_file = resource_filename('tdd_tutorial', 'hands-on/currenty_things.yml')


@pytest.fixture
def example_yaml():
    return yaml_file
