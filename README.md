# midas-review-bench

Public replay of 12 merged open-source pull requests, used to compare AI code
reviewers on the same diffs. Not affiliated with any project below. Nothing
here is sent upstream.

Each row `NN` has three branches:

- `rNN-base`: a snapshot of the project before the change.
- `rNN-head`: one commit on top of it with the change, so the diff is exactly the original one.
- `rNN-midas`: the same commit as `rNN-head`.

Snapshots drop `.github/`, so upstream CI does not run here. They add the same
`.coderabbit.yaml` as `main`, because CodeRabbit reads it from the PR branch. The
file is on both sides of each diff, so the diff is unchanged. Everything else is
the project's own files, including its license.

| Project | Upstream | License |
|---|---|---|
| scikit-learn | https://github.com/scikit-learn/scikit-learn | BSD-3-Clause |
| aiohttp | https://github.com/aio-libs/aiohttp | Apache-2.0 |
| httpx | https://github.com/encode/httpx | BSD-3-Clause |
| TanStack Query | https://github.com/TanStack/query | MIT |
| zod | https://github.com/colinhacks/zod | MIT |
| Poetry | https://github.com/python-poetry/poetry | MIT |
| pandas | https://github.com/pandas-dev/pandas | BSD-3-Clause |
| pytest | https://github.com/pytest-dev/pytest | MIT |
| Requests | https://github.com/psf/requests | Apache-2.0 |
| Flask | https://github.com/pallets/flask | BSD-3-Clause |
