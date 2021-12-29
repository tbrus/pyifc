"""
Conftest file for tests of pyifc.compress module
-------------------------------

All data processing is implemented here. 
"""
import pytest


test_data_dir = "data"
test_data_files = ["test01.ifc", "test02.ifc", "test03.ifc"]

@pytest.fixture(params=test_data_files)
def data(request):
    return os.path.join(test_data_dir, request.param)