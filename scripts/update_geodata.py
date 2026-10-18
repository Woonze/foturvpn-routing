#!/usr/bin/env python3
"""Refresh FoturVPN profile links when upstream GeoIP/Geosite releases change."""
from __future__ import annotations

import base64
import json
import re
import subprocess
import time
from urllib.request import Request, urlopen
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATASETS = {
    "geoip": "hydraponique/roscomvpn-geoip",
    "geosite": "hydraponique/roscomvpn-geosite",
}
PROFILES = ("DEFAULT", "WHITELIST", "JSONSUB")
CLIENTS = {"HAPP": "happ", "INCY": "incy"}


def latest_release_tag(repository: str) -> str:
    output = subprocess.check_output(
        ["git", "ls-remote", "--tags", f"https://github.com/{repository}.git"],
        text=True,
    )
    tags = {
        ref.removeprefix("refs/tags/").removesuffix("^{}")
        for _, ref in (line.split(maxsplit=1) for line in output.splitlines())
    }
    dated_tags = [tag for tag in tags if re.fullmatch(r"\d{12}", tag)]
    if not dated_tags:
        raise RuntimeError(f"No timestamped release tags found for {repository}")
    return max(dated_tags)


def main() -> None:
    tags = {name: latest_release_tag(repo) for name, repo in DATASETS.items()}
    urls = {
        "Geoipurl": f"https://cdn.jsdelivr.net/gh/{DATASETS['geoip']}@{tags['geoip']}/release/geoip.dat",
        "Geositeurl": f"https://cdn.jsdelivr.net/gh/{DATASETS['geosite']}@{tags['geosite']}/release/geosite.dat",
    }
    for url in urls.values():
        request = Request(url, method="HEAD")
        with urlopen(request, timeout=30) as response:
            if response.status != 200:
                raise RuntimeError(f"Dataset is unavailable: {url}")
    now = str(int(time.time()))

    for client, scheme in CLIENTS.items():
        for profile in PROFILES:
            config_path = ROOT / client / f"{profile}.JSON"
            config = json.loads(config_path.read_text())
            changed = any(config.get(key) != value for key, value in urls.items())
            if changed:
                config.update(urls)
                config["LastUpdated"] = now
                config_path.write_text(json.dumps(config, ensure_ascii=False, indent=2) + "\n")

            compact = json.dumps(config, ensure_ascii=False, separators=(",", ":")).encode()
            encoded = base64.b64encode(compact).decode()
            deeplink = ROOT / client / f"{profile}.DEEPLINK"
            deeplink.write_text(f"{scheme}://routing/onadd/{encoded}\n")


if __name__ == "__main__":
    main()
