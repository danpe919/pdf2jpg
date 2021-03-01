import os
import sys
from pathlib import Path

from pdf2image import convert_from_path

DESKTOP = Path(os.getenv("HOMEDRIVE") + os.getenv("HOMEPATH")) / "Desktop"


def pdf2jpg(filename: str, output: str):
    p = Path(filename)
    base = p.stem

    libs = Path("./bin/")
    images = convert_from_path(Path(filename), poppler_path=libs)
    for i, image in enumerate(images):
        image.save(f"{output}/{base}-{i+1}.jpg", "jpeg")


def main():
    filename = sys.argv[1]
    target = Path(filename)

    output = DESKTOP / "output"
    print(f"{filename}: 変換中...")
    pdf2jpg(target, output)


if __name__ == "__main__":
    main()
    sys.exit(0)
