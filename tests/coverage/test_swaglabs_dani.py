import pytest
from tests.testbase import *

class TestSuiteLogin:
	def test_login_success(self, beforeEach: Test):
		web, get = beforeEach
  

if __name__ == "__main__":
    pytest.main()