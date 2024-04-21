#!/usr/bin/env python3

import pytest
from log_analysis.ticky_check import find_error_message


def test_string():
    assert find_error_message(
        "Jan 31 00:21:30 ubuntu.local ticky: ERROR The ticket was modified while updating (breee)"
    ).groups(), ("ERROR", "The ticket was modified while updating",
                 "breee")

def test_not_log_message():
    assert find_error_message("") is None

def test_not_string():
    assert find_error_message(3.14), TypeError