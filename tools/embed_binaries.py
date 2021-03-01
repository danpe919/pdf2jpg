import re
import sys
from glob import glob
from typing import List


def find_binaries(path: str):
    ret = []
    for f in glob(f"{path}*"):
        if f.endswith("exe") or f.endswith("dll"):
            f = f.replace("\\", "/")
            ret.append(f)
    return ret


def replace_bundles(spec_file: str, bundles: List):
    with open(spec_file) as fp:
        data = fp.read()

    binaries = ",".join(bundles)
    data = re.sub(r"binaries=\[[^\[\]]*\]", f"binaries=[{binaries}]", data)
    print(data)

    with open(spec_file, "w") as fp:
        fp.write(data)


def main():
    binaries = find_binaries("./bin/")
    bundles = [f"('{f}', './bin')" for f in binaries]
    replace_bundles("./main.spec", bundles)


if __name__ == "__main__":
    main()
