from template import template

if __name__ == "__main__":
    title = "README.md generator"
    description = "this just generates README.md in this fashion"
    repo_name = "readme_generator"
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
    with open("./README.md", "w+") as f:
        f.write(readme)
