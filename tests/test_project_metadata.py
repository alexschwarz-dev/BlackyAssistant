"""Checks for project setup and documentation consistency.

These tests deliberately do not import ``main`` because importing it currently
starts the Tkinter event loop.
"""

from pathlib import Path
import unittest


PROJECT_ROOT = Path(__file__).resolve().parents[1]


class ProjectMetadataTests(unittest.TestCase):
    def test_runtime_dependency_is_declared(self):
        requirements = (PROJECT_ROOT / "requirements.txt").read_text(encoding="utf-8")
        declared_packages = {
            line.split("=", 1)[0].split("<", 1)[0].split(">", 1)[0].strip().lower()
            for line in requirements.splitlines()
            if line.strip() and not line.lstrip().startswith("#")
        }
        self.assertIn("psutil", declared_packages)

    def test_readme_uses_current_documented_version(self):
        readme = (PROJECT_ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("**v0.4.0**", readme)

    def test_readme_installation_matches_repository_name(self):
        readme = (PROJECT_ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("cd BlackyAssisstant", readme)


if __name__ == "__main__":
    unittest.main()

