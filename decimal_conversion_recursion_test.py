import subprocess
import sys
from pathlib import Path

import pytest

SCRIPT = Path(__file__).with_name("decimal_conversion_recursion.py")


def run(stdin: str) -> str:
    result = subprocess.run(
        [sys.executable, str(SCRIPT)],
        input=stdin, capture_output=True, text=True, check=True,
    )
    return result.stdout.strip()

def test_sample():
    assert run("ZZZZZ 36\n") == "60466175"
