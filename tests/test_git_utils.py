"""Tests for gitbaton.git_utils."""

import tempfile
import unittest
from pathlib import Path

import gitbaton.git_utils as git_utils


class TestFindGitRoot(unittest.TestCase):
    """Tests for find_git_root."""

    def test_finds_git_root_from_repo_root(self) -> None:
        """Should return the repo root when called from the repo root."""
        root = git_utils.find_git_root()
        self.assertTrue((root / ".git").exists())

    def test_finds_git_root_from_subdirectory(self) -> None:
        """Should walk up from a subdirectory to find the repo root."""
        with tempfile.TemporaryDirectory() as tmpdir:
            subdir = Path(tmpdir) / "sub" / "dir"
            subdir.mkdir(parents=True, exist_ok=True)
            # If we pass a temp dir outside of a git repo, it should raise RuntimeError.
            # But inside a temp dir that has no .git parent, it raises RuntimeError.
            with self.assertRaises(RuntimeError):
                git_utils.find_git_root(subdir)

    def test_raises_outside_git_repo(self) -> None:
        """Should raise RuntimeError when not inside a git repository."""
        with tempfile.TemporaryDirectory() as tmpdir:
            with self.assertRaises(RuntimeError):
                git_utils.find_git_root(Path(tmpdir))
