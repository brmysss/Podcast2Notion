from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "scripts"
BLOCKED_HOSTS = (
    "wereadassets.malinkang.com",
    "i.malinkang.com",
    "notionhub.app",
    "heatmap.malinkang.com",
    "notion-icon.malinkang.com",
)


class FreeRuntimeTest(unittest.TestCase):
    def test_source_does_not_call_notionhub_services(self):
        source = "\n".join(
            path.read_text(encoding="utf-8")
            for path in SOURCE.rglob("*.py")
        )
        for host in BLOCKED_HOSTS:
            self.assertNotIn(host, source)

    def test_episode_links_use_https(self):
        source = (SOURCE / "podcast.py").read_text(encoding="utf-8")
        self.assertNotIn("hhttps://", source)


if __name__ == "__main__":
    unittest.main()
