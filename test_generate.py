import os

from template import template
from generate import generate_readme


def test_generates_readme():
    before = os.listdir()
    assert "GENERATED.md" not in before
    generate_readme()
    after = os.listdir()
    assert "GENERATED.md" in after
    os.remove("GENERATED.md")
