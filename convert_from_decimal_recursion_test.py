import subprocess
import sys
from pathlib import Path

import pytest

SCRIPT = Path(__file__).with_name("convert_from_decimal_recursion.py")
DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def run(stdin: str) -> str:
    result = subprocess.run(
        [sys.executable, str(SCRIPT)],
        input=stdin, capture_output=True, text=True, check=True,
    )
    return result.stdout.strip()

def test_sample():
    assert run("60466175 36\n") == "ZZZZZ"