"""Download BAAI's official ONNX export of bge-small-en-v1.5 (pinned revision, checksums verified).

python scripts/fetch_onnx.py [target_dir]     (default: .cache/bge-onnx)
"""
import hashlib
import sys
import urllib.request
from pathlib import Path

REV = "5c38ec7c405ec4b44b94cc5a9bb96e735b38267a"
FILES = {
    "onnx/model.onnx": "828e1496d7fabb79cfa4dcd84fa38625c0d3d21da474a00f08db0f559940cf35",
    "tokenizer.json": "d241a60d5e8f04cc1b2b3e9ef7a4921b27bf526d9f6050ab90f9267a1f9e5c66",
}


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def main() -> None:
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1] / ".cache" / "bge-onnx"
    out.mkdir(parents=True, exist_ok=True)
    for remote, digest in FILES.items():
        dest = out / Path(remote).name
        if not (dest.exists() and sha256(dest) == digest):
            url = f"https://huggingface.co/BAAI/bge-small-en-v1.5/resolve/{REV}/{remote}"
            print("downloading", url)
            urllib.request.urlretrieve(url, dest)
        if sha256(dest) != digest:
            sys.exit(f"checksum mismatch for {dest}")
        print("ok", dest)


if __name__ == "__main__":
    main()
