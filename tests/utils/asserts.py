import pytest
from time import sleep as wait
from selenium.webdriver.remote.webdriver import WebDriver
dataType = str | int | float | bool | list | tuple | set | dict


class Expect:
    # * Definición de funciones para realizar Asserciones con valores dados
    def __init__(self, actualValue: dataType):
        if not isinstance(actualValue, dataType):
            raise ValueError(f'DataType not supported. try: {dataType}')
        self.value = actualValue
        self.dataType = dataType

    def toBeEqual(self, expectedValue: dataType):
        if not isinstance(expectedValue, dataType):
            raise ValueError(f'DataType not supported. try: {dataType}')
        assert self.value == expectedValue
        wait(1)

    def toNotBeEqual(self, expectedValue: dataType):
        if not isinstance(expectedValue, dataType):
            raise ValueError(f'DataType not supported. try: {dataType}')
        assert self.value != expectedValue
        wait(1)

    def toContain(self, innerValue: str):
        if not isinstance(self.value, str):
            raise ValueError(f'Value type not supported. Use String type')
        assert innerValue in self.value
        wait(1)

    def isTrue(self):
        if not isinstance(self.value, bool):
            raise ValueError(f'Value type not supported. Use Boolean type')
        assert self.value == True
        wait(1)

    def isFalse(self):
        if not isinstance(self.value, bool):
            raise ValueError(f'Value type not supported. Use Boolean type')
        assert self.value == False
        wait(1)
