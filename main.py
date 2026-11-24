"""One-line weather forecast for the fictional city of Umbrella Bay.

Entry for make.fun's "Charm the Commuter: Forecast a City That Isn't":
name a place that does not exist, give it weather, and make a bored
commuter smile on the way to work. The line is 128 characters.
"""

import os

TEXT = (
    "Good morning, Umbrella Bay: 16\u00b0C, light drizzle, and the "
    "8:04 ferry is on time for once \u2014 your umbrella finally "
    "gets its moment."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)
    print(TEXT)


if __name__ == "__main__":
    main()
