import inspect
from enum import Enum


class ChoiceEnum(Enum):
    """ String-stored enums. """

    @classmethod
    def choices(cls) -> tuple:
        # get all members of the class
        members = inspect.getmembers(cls, lambda m: not (inspect.isroutine(m)))
        # filter down to just properties
        props = [m for m in members if not (m[0][:2] == '__')]
        # format into django choice tuple
        choices = tuple([(cls._value_representation(p[1].value), p[0]) for p in props])
        return choices

    @classmethod
    def _value_representation(cls, value: any) -> any:
        return str(value)


class IntChoiceEnum(ChoiceEnum):
    """ Int-stored enums """

    @classmethod
    def _value_representation(cls, value: any) -> int:
        return int(value)
