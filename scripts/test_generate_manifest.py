"""Contract tests for the public release updater manifests."""
import hashlib
import importlib.util
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

SOURCE=Path(__file__).parent/"generate_manifest.py"
spec=importlib.util.spec_from_file_location("generate_manifest",SOURCE)
module=importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class ManifestTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.old=os.getcwd()
        os.chdir(self.temp.name)
        for app in module.APPS:
            for channel in module.CHANNELS:
                path=Path("updates")/app/(channel+".json")
                path.parent.mkdir(parents=True,exist_ok=True)
                path.write_text(json.dumps({"schema_version":1,"app_id":app,"channel":channel,"available":False}),encoding="utf-8")
        Path("source.exe").write_bytes(b"MZ"+b"0"*(1024*1024+100))

    def tearDown(self):
        os.chdir(self.old)
        self.temp.cleanup()

    def invoke(self,app="cultoflow",channel="preview",version="0.5.2",source_tag="agent-v0.5.2-build-34"):
        args=["prog","--app",app,"--channel",channel,"--version",version,
              "--source-tag",source_tag,"--source-installer","source.exe",
              "--public-installer",f"publish/{app}-{version}.exe"]
        with patch("sys.argv",args):
            module.main()

    def test_manifest_has_public_url_and_verified_hash(self):
        self.invoke()
        manifest=json.loads(Path("updates/cultoflow/preview.json").read_text())
        self.assertEqual(manifest["app_id"],"cultoflow")
        self.assertTrue(manifest["available"])
        self.assertEqual(manifest["release_tag"],"cultoflow-preview-v0.5.2")
        self.assertIn("github.com/pedrosamuelfeijao/public-donwloads/releases/download",manifest["installer"]["url"])
        self.assertEqual(manifest["installer"]["sha256"],hashlib.sha256(Path("source.exe").read_bytes()).hexdigest())

    def test_reject_prerelease_in_stable(self):
        with self.assertRaises(ValueError):
            self.invoke(channel="stable",version="0.4.0rc20")
        self.assertFalse(json.loads(Path("updates/cultoflow/stable.json").read_text())["available"])

    def test_no_downgrade_or_replace_same_version(self):
        self.invoke()
        with self.assertRaises(ValueError):
            self.invoke(version="0.5.2")
        with self.assertRaises(ValueError):
            self.invoke(version="0.5.1")

    def test_version_order(self):
        self.assertLess(module.sort_key("0.4.0rc19"),module.sort_key("0.4.0rc20"))
        self.assertLess(module.sort_key("0.4.0rc20"),module.sort_key("0.4.0"))
        self.assertLess(module.sort_key("0.5.1"),module.sort_key("0.5.2"))
if __name__ == "__main__":
    unittest.main()
