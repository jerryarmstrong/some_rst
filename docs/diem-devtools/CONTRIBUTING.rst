CONTRIBUTING.md
===============

Last edited: 2022-02-01 05:13:53

Contents:

.. code-block:: md

    Our goal is to make contributing to the diem-devtools project easy and transparent.

## Pull Requests

We actively welcome your pull requests. If you have a new feature in mind, please discuss the feature in an issue to
ensure that your contributions will be accepted.

1. Fork the repo and create your branch from `main`.
2. If you've added code that should be tested, add tests.
3. If you've changed APIs, update the documentation.
4. Ensure the test suite passes with `cargo test --all-features`.
5. Run `cargo xfmt` to automatically format your changes (CI will let you know if you missed this).
6. If you haven't already, complete the Contributor License Agreement ("CLA").

## Logically Separate Commits

Commits should be
[atomic](https://en.wikipedia.org/wiki/Atomic_commit#Atomic_commit_convention)
and broken down into logically separate changes. Diffs should also be made easy
for reviewers to read and review so formatting fixes or code moves should not
be included in commits with actual code changes.

## Bisect-able History

It is important that the project history is bisect-able so that when
regressions are identified we can easily use `git bisect` to be able to
pin-point the exact commit which introduced the regression. This requires that
every commit is able to be built and passes all lints and tests. So if your
pull request includes multiple commits be sure that each and every commit is
able to be built and passes all checks performed by CI.

## Contributor License Agreement

For pull request to be accepted by any Diem projects, a CLA must be signed.
You will only need to do this once to work on any of Diem's open source
projects. Individuals contributing on their own behalf can sign the [Individual
CLA](https://github.com/diem/diem/blob/main/documentation/contributing/individual-cla.pdf).
If you are contributing on behalf of your employer, please ask them to sign the
[Corporate
CLA](https://github.com/diem/diem/blob/main/documentation/contributing/corporate-cla.pdf).

## Issues

Diem uses [GitHub issues](https://github.com/diem/diem-devtools/issues) to track
bugs. Please include necessary information and instructions to reproduce your
issue.

## License

By contributing to `diem-devtools`, you agree that your contributions will be dual-licensed under the terms of the
[`LICENSE-MIT`](LICENSE-MIT) and [`LICENSE-APACHE`](LICENSE-APACHE) files in the root directory of this source
tree.


