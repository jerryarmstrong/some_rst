tests/ui-fulldeps/lint-group-denied-lint-allowed.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:lint-group-plugin-test.rs
// check-pass
// compile-flags: -D unused -A unused-variables

fn main() {
    let x = 1;
}


