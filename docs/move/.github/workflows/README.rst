.github/workflows/README.md
===========================

Last edited: 2023-08-11 19:18:44

Contents:

.. code-block:: md

    Workflows/ contain [github actions](https://github.com/features/actions) that can run on specific events.

Below is a list of all actions implemented in this directory:

* `hyperjump-*`. These are backend hyperjump workflows to trigger specific
  actions that come via hyperjumps routed through `repository_dispatch`
  triggers.
* [dep-summaries](dep-summaries.yml). This workflow monitors dependency
  changes to special subsets and flags them in the PR.


