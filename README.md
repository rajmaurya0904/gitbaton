# GitBaton

**A tool designed for multi-agent coding sessions that cleanly orchestrates task handoffs, preventing concurrent merge conflicts on shared files.**

When multiple autonomous coding agents or developers edit the same repository simultaneously, they frequently step on each other's toes modifying shared configuration, entrypoints, or utility files. GitBaton replaces chaotic parallel edits with sequential batons and file locks, removing the endless cycle of rebase conflicts and broken builds.

## Example

<!-- A real command and its REAL pasted output. Run it first. -->

## Install

```bash
pip install -e ".[dev]"
```

## Usage

<!-- The 2-4 commands people actually need, one line each. -->

## How it works

<!-- 3-6 bullets: what it checks, computes or produces. -->

## Limitations

- **No locking or handoff logic yet.** GitBaton currently only locates the root of a git repository (`gitbaton.git_utils.find_git_root`). The baton-passing, file-locking, and task-orchestration features described above are not implemented, and there is no CLI entry point to run.
- **Git only.** It assumes the working directory is inside a git repository and shells out to the `git` executable; it does not understand other version-control systems, and it fails with `FileNotFoundError` if `git` is not on `PATH`.
- **No network, no remotes.** Nothing here pushes, pulls, or talks to a remote; all operations are local to the checked-out repository.
- **Untested on Windows.** The test suite runs on POSIX systems; the `git rev-parse` invocation is not verified on Windows shells.
- **Single repository.** It operates on one repository at a time; there is no support for monorepos spanning multiple git roots or for submodules.

## Development

```bash
pip install -e ".[dev]"
pytest -q
ruff check .
```

## License

MIT -- see [LICENSE](LICENSE).
