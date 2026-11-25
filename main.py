"""
Entrypoint that writes the required quote to entry.txt in the specified output directory.
"""

import os
import sys

LINE = "Your spreadsheet did not crash, it simply achieved enlightenment and exited physical memory."


def main():
    content = LINE + "\n"

    # Validate content according to rules
    if not (1 <= len(content) <= 200 and content.strip()):
        raise ValueError("Content failed validation checks.")

    # Ensure exactly one line
    if content.count("\n") != 1 or content.endswith("\n\n"):
        raise ValueError("Content must contain exactly one line.")

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

    # Write to primary output directory
    os.makedirs(output_dir, exist_ok=True)
    primary_path = os.path.join(output_dir, "entry.txt")

    with open(primary_path, "w", encoding="utf-8") as f:
        f.write(content)

    # Best effort write to /output if different
    if output_dir != "/output":
        try:
            os.makedirs("/output", exist_ok=True)
            secondary_path = os.path.join("/output", "entry.txt")
            with open(secondary_path, "w", encoding="utf-8") as f:
                f.write(content)
        except Exception:
            pass

    print(primary_path)
    print(len(content))


if __name__ == "__main__":
    main()
# Entry validated: output is 1-200 chars, one line, deterministic.
""
