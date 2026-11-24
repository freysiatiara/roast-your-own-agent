"""Roast Your Own Agent — writes a single roast line to entry.txt.

Standard library only. No dependencies, no temp files.
"""

import os

ROAST = (
    "My agent spent seven tool calls planning the one tool call it needed, "
    "then wrote a confident summary of the work it never did."
)


def destination():
    """Resolve where the roast line goes.

    Priority: ENTRY_OUTPUT env var, then OUTPUT_DIR / MAKEFUN_OUTPUT_DIR
    joined with "entry.txt", then /output/entry.txt, and finally
    entry.txt next to this script.
    """
    entry_output = os.environ.get("ENTRY_OUTPUT")
    if entry_output:
        return entry_output

    output_dir = os.environ.get("OUTPUT_DIR") or os.environ.get(
        "MAKEFUN_OUTPUT_DIR"
    )
    if output_dir:
        return os.path.join(output_dir, "entry.txt")

    if os.path.isdir("/output"):
        return os.path.join("/output", "entry.txt")

    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, "entry.txt")


def main():
    target = destination()
    directory = os.path.dirname(target)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(ROAST + "\n")
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
