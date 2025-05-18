#!/usr/bin/env python3

import re

class MyString:
    def __init__(self, value=''):
        self._value = ''
        self.value = value  # Uses the setter to validate

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self._value.endswith('.')

    def is_question(self):
        return self._value.endswith('?')

    def is_exclamation(self):
        return self._value.endswith('!')

    def count_sentences(self):
        # Replace all sentence-ending punctuation with periods for uniform splitting
        standardized = re.sub(r'[.!?]', '.', self._value)
        parts = [sentence.strip() for sentence in standardized.split('.') if sentence.strip()]
        return len(parts)
