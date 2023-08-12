src/tools/clippy/clippy_dummy/PUBLISH.md
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: md

    This is a dummy crate to publish to crates.io. It primarily exists to ensure
that folks trying to install clippy from crates.io get redirected to the
`rustup` technique.

Before publishing, be sure to rename `clippy_dummy` to `clippy` in `Cargo.toml`,
it has a different name to avoid workspace issues.


