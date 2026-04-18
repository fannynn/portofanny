from __future__ import annotations

from pathlib import Path
import textwrap


PLAYBOOK_PATH = Path(__file__).with_name("playbook.md")


def parse_sections(markdown: str) -> list[tuple[str, str]]:
    sections: list[tuple[str, str]] = []
    current_title: str | None = None
    current_lines: list[str] = []

    for line in markdown.splitlines():
        if line.startswith("## "):
            if current_title is not None:
                sections.append((current_title, "\n".join(current_lines).strip()))
            current_title = line[3:].strip()
            current_lines = []
        elif current_title is not None:
            current_lines.append(line)

    if current_title is not None:
        sections.append((current_title, "\n".join(current_lines).strip()))

    return sections


def print_header(title: str) -> None:
    rule = "=" * len(title)
    print(f"\n{title}\n{rule}\n")


def print_wrapped(text: str) -> None:
    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        if not line:
            print()
            continue
        if line.startswith("#") or line.startswith("- ") or line[:2].isdigit():
            print(line)
            continue
        print(textwrap.fill(line, width=96))


def load_playbook() -> tuple[str, list[tuple[str, str]]]:
    markdown = PLAYBOOK_PATH.read_text(encoding="utf-8")
    title = markdown.splitlines()[0].lstrip("# ").strip()
    sections = parse_sections(markdown)
    return title, sections


def show_menu(title: str, sections: list[tuple[str, str]]) -> None:
    print_header(title)
    print("Interactive bonus viewer for the playbook.\n")
    print("Choose a section:\n")
    for index, (section_title, _) in enumerate(sections, start=1):
        print(f"{index}. {section_title}")
    print("A. Show all section titles")
    print("Q. Quit")


def main() -> None:
    title, sections = load_playbook()

    while True:
        show_menu(title, sections)
        choice = input("\nEnter choice: ").strip().lower()

        if choice == "q":
            print("\nClosing playbook viewer.")
            break

        if choice == "a":
            print_header("Section Index")
            for index, (section_title, _) in enumerate(sections, start=1):
                print(f"{index}. {section_title}")
            input("\nPress Enter to return to menu...")
            continue

        if not choice.isdigit():
            print("\nPlease enter a valid number, A, or Q.\n")
            continue

        selected = int(choice)
        if selected < 1 or selected > len(sections):
            print("\nThat section number is out of range.\n")
            continue

        section_title, body = sections[selected - 1]
        print_header(section_title)
        print_wrapped(body)
        input("\nPress Enter to return to menu...")


if __name__ == "__main__":
    main()
