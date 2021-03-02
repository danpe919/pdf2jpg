import os
import sys
from pathlib import Path

from pdf2image import convert_from_path

DESKTOP = Path(os.getenv("HOMEDRIVE") + os.getenv("HOMEPATH")) / "Desktop"


def resource_path(relative_path: str):
    """相対パスからPyInstallerでも読み込み可能なパス文字列を取得する
    Ref: https://lets-hack.tech/programming/languages/python/pyinstaller/
    Args:
        relative_path (str): 相対パス

    Returns:
        str: パス
    """
    base_path = getattr(sys, "_MEIPASS", str(Path(__file__).absolute().parent))
    return str(Path(base_path).joinpath(relative_path))


def pdf2jpg(filename: str, output: str):
    p = Path(filename)
    base = p.stem

    libs = resource_path("./bin/")
    images = convert_from_path(Path(filename), poppler_path=libs)
    for i, image in enumerate(images):
        image.save(f"{output}/{base}-{i+1}.jpg", "jpeg")


def main():
    filename = sys.argv[1]
    target = Path(filename)

    output = DESKTOP / "output"
    os.makedirs(output, exist_ok=True)

    print(f"{filename}: 変換中...")
    pdf2jpg(target, output)


if __name__ == "__main__":
    main()
    sys.exit(0)
