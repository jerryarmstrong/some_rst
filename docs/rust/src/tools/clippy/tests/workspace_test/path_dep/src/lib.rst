src/tools/clippy/tests/workspace_test/path_dep/src/lib.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(clippy::empty_loop)]

#[cfg(feature = "primary_package_test")]
pub fn lint_me() {
    loop {}
}


