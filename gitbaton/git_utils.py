"""Git utility functions for gitbaton.

Provides helpers to locate the root of a git repository.
"""

from __future__ import annotations

from pathlib import Path

__all__ = ["find_git_root"]


def find_git_root(start_path: Path | None = None) -> Path:
    """Return the path to the root of the git repository containing *start_path*.

    The function walks up the directory tree from *start_path* (or the current
    working directory if ``None``) looking for a ``.git`` entry. If found, the
    directory containing ``.git`` is returned. If the search reaches the file
    system root without finding a ``.git`` directory, a :class:`RuntimeError`
    is raised.

    Parameters
    ----------
    start_path:
        The directory to start the search from. If ``None`` the current working
        directory is used.

    Returns
    -------
    pathlib.Path
        The absolute path to the git repository root.

    Raises
    ------
    RuntimeError
        If *start_path* is not inside a git repository.
    """
    if start_path is None:
        start_path = Path.cwd()
    else:
        start_path = Path(start_path)

    # Ensure we work with absolute paths for consistency.
    start_path = start_path.resolve()

    for directory in (start_path, *list(start_path.parents)):
        git_path = directory / ".git"
        if git_path.exists():
            return directory
    raise RuntimeError("Current directory is not inside a git repository")
