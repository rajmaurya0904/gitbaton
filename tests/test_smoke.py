"""Smoke test: package imports cleanly. Replace/extend as modules land."""

import gitbaton


def test_version_is_set() -> None:
    assert gitbaton.__version__
