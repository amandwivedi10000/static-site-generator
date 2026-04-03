from pathlib import Path
import os
from markdown_to_html_node import markdown_to_html_node


def extract_title(markdown: str):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[1:].strip()
    raise Exception("It doesn't have a heading")


def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as file:
        from_path_content = file.read()

    with open(template_path, "r") as file:
        template_path_content = file.read()

    html_from_path_content = markdown_to_html_node(from_path_content).to_html()
    html_title_content = (
        template_path_content.replace("{{ Title }}", extract_title(from_path_content))
        .replace("{{ Content }}", html_from_path_content)
        .replace('href="/', f'href="{basepath}')
        .replace('src="/', f'src="{basepath}')
    )

    dest_dir = os.path.dirname(dest_path)
    os.makedirs(dest_dir, exist_ok=True)

    with open(dest_path, "w") as file:
        file.write(html_title_content)


def generate_pages_recursive(dest_path_content, template_path, dest_dir_path, basepath):
    entries = os.listdir(dest_path_content)
    for entry in entries:
        full_content_path = os.path.join(dest_path_content, entry)
        full_des_path = os.path.join(dest_dir_path, entry)
        if os.path.isfile(full_content_path):
            generate_page(
                full_content_path,
                template_path,
                Path(full_des_path).with_suffix(".html"),
                basepath,
            )
        else:
            generate_pages_recursive(
                full_content_path, template_path, full_des_path, basepath
            )
