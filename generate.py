from template import template


def generate_readme(title: str, description: str, repo_name: str):
    readme = template.format(
        title,
        description,
        repo_name,
        repo_name,
        repo_name,
        repo_name,
        repo_name,
        repo_name,
        repo_name,
        repo_name,
    )
    with open("./GENERATED.md", "w+") as f:
        f.write(readme)
