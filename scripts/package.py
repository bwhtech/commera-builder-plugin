"""Build dist/<publisher>-<name>-<version>.builderplugin, the asset a GitHub release must carry for Builder Hub."""

import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FILES = ("manifest.json", "main.js", "icon.svg")

manifest = json.loads((ROOT / "manifest.json").read_text())
package = ROOT / "dist" / f"{manifest['name'].replace('/', '-')}-{manifest['version']}.builderplugin"
package.parent.mkdir(exist_ok=True)
with zipfile.ZipFile(package, "w", zipfile.ZIP_DEFLATED) as archive:
	for name in FILES:
		archive.write(ROOT / name, name)
print(package)
