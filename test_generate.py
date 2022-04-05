import os

from generate import generate_readme


def test_generates_readme():
    title = ""
    description = ""
    repo_name = ""
    before = os.listdir()
    assert "GENERATED.md" not in before
    generate_readme(title, description, repo_name)
    after = os.listdir()
    assert "GENERATED.md" in after
    os.remove("GENERATED.md")
