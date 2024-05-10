"""Aggiunge i link nella documentazione"""

import os


class DocLinker:
    def __init__(self, files):
        self.files = files
        self.link_names = [file.removesuffix(".md") for file in files]

    def link_files(self):
        for file in self.files:
            self.link_file(file)

    def link_file(self, file: str):
        with open(file, encoding="utf8") as file_descriptor:
            content = file_descriptor.read()

        linked_content = self.link_content(content, [file.removesuffix(".md")])

        with open(file, "w", encoding="utf8") as file_descriptor:
            file_descriptor.write(linked_content)

    def link_content(self, content, excluded_links) -> str:
        for link_name in self.link_names:
            if link_name in excluded_links:
                continue
            if f"`{link_name}`" not in content:
                continue
            content = self.add_links(content, link_name)

        return content

    @staticmethod
    def add_links(content: str, link_name):
        fmt_link = f"`{link_name}`"
        start = 0
        new_content = ""
        while True:
            new_start = content.find(fmt_link, start)
            if new_start == -1:
                new_content += content[start:]
                break
            new_content += content[start:new_start]
            start = new_start + len(fmt_link)
            if new_content[-1] == "[":  # if it has already a link
                new_content += fmt_link
                continue
            new_content += f"[{fmt_link}]({link_name}.md)"

        return new_content


if __name__ == "__main__":
    exclude_files = ["README.md", "add_links.py"]
    doc_files = [file for file in os.listdir() if file not in exclude_files]
    linker = DocLinker(doc_files)
    linker.link_files()
