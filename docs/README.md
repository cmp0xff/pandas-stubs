# Development paradigm with pandas-stubs

For any update to the stubs, we require an associated test case that should fail without
a proposed change, and works with a proposed change.  See <https://github.com/pandas-dev/pandas-stubs/tree/main/tests/> for examples.

The stubs are developed with a certain [philosophy](philosophy.md) that should be 
understood by developers proposing changes to the stubs.

Instructions for working with the code are found here:

- [How to set up the environment](setup.md)
- [How to test the project](tests.md)
- [How to make a release](release_procedure.md)
- [Type architecture](type-architecture/README.md)

## Issues and discussions

- We do not assign issues. To work on one, open a PR; there is no need to ask first or to check whether someone else is working on it.
- We review code, not plans. Post a plan only when a maintainer asks for one.
- Comment on an issue when you add something new: a reproducer, a measured type-checker or runtime result, or a link to your PR. Comments that restate the issue or ask for general guidance may go unanswered.
- Keep comments short. If AI drafts them, check every claim yourself and cut anything that does not add information.

## After a review round

When you have addressed a round of review comments:

1. If your branch conflicts with `main`, merge the latest `main` of pandas-dev/pandas-stubs into it and push. Once review has started, merge rather than rebase: a rebase rewrites the history, and reviewers' comments lose their link to the code.
2. Wait until CI is green.
3. Re-request review from each reviewer whose comments you addressed (the re-request button next to their name in the PR's reviewer list).
