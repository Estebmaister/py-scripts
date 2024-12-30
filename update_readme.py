import os
import re


def get_folder_list(repo_path):
    """
    Get a list of subfolders in the specified repository path.
    Excludes hidden folders.
    """
    return [
        folder for folder in os.listdir(repo_path)
        if os.path.isdir(os.path.join(repo_path, folder)) and not folder.startswith(".")
    ]


def generate_folder_list_markdown(folder_list):
    """
    Generate a markdown list from the folder names.
    """
    return "\n".join([f"- {folder}" for folder in sorted(folder_list)])


def read_readme(readme_path):
    """
    Read the content of the README file if it exists, else return None.
    """
    if os.path.exists(readme_path):
        with open(readme_path, "r") as file:
            return file.read()
    return None


def write_readme(readme_path, content):
    """
    Write the given content to the README file.
    """
    with open(readme_path, "w") as file:
        file.write(content)


def update_readme_content(existing_content, folder_list_md):
    """
    Update the README content with the scripts categories.
    Preserves the main description if present.
    """
    folder_list_section = f"## Scripts Categories\n{folder_list_md}\n"

    if existing_content:
        if "## Scripts Categories" in existing_content:
            # Replace the scripts categories section
            updated_content = re.sub(
                r"(## Scripts Categories\s*\n)(- .*\n)*",
                folder_list_section,
                existing_content
            )
        else:
            # Append the scripts categories section
            updated_content = f"{existing_content.strip()}\n\n{folder_list_section}"
    else:
        # Create a new README with a basic structure
        updated_content = f"# Py Scripts\n\n{folder_list_section}"

    return updated_content


def update_readme(repo_path):
    """
    Main function to update the README.md file with the scripts categories.
    """
    readme_path = os.path.join(repo_path, "README.md")
    folder_list = get_folder_list(repo_path)
    folder_list_md = generate_folder_list_markdown(folder_list)

    # Read the existing README content
    existing_content = read_readme(readme_path)

    # Update the README content
    updated_content = update_readme_content(existing_content, folder_list_md)

    # Write the updated content back to the README
    write_readme(readme_path, updated_content)

    print("README.md has been updated.")


if __name__ == "__main__":
    repo_path = input("Enter the path to the repository: ").strip()
    if os.path.isdir(repo_path):
        update_readme(repo_path)
    else:
        print("Invalid path to the repository.")
