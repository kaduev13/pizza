from lib.db.choice_enum import ChoiceEnum, IntChoiceEnum


class ChoiceIntChild(ChoiceEnum):
    VALUE1 = 1
    VALUE2 = 2


class ChoiceStrChild(ChoiceEnum):
    VALUE1 = '1'
    VALUE2 = '2'


class IntChoiceIntChild(IntChoiceEnum):
    VALUE1 = 1
    VALUE2 = 2


class TestChoiceEnum:
    as_str = (
        ('1', 'VALUE1'),
        ('2', 'VALUE2'),
    )

    as_int = (
        (1, 'VALUE1'),
        (2, 'VALUE2'),
    )

    def test_choices(self):
        assert self.as_str == ChoiceIntChild.choices()
        assert self.as_str == ChoiceStrChild.choices()
        assert self.as_int == IntChoiceIntChild.choices()
