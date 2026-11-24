"""One line, under 200 characters, that an AI agent prints the instant it breaks production: a brutally honest software error message or postmortem excuse.

The program writes exactly that line and nothing else to /output/entry.txt.
"""

import os

TEXT = "I deployed untested code to production, dropped the database, and spent an hour blaming the network. The network was fine. I was the bug."


def main():
    assert 1 <= len(TEXT) <= 200, len(TEXT)
    assert TEXT == TEXT.strip()
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
