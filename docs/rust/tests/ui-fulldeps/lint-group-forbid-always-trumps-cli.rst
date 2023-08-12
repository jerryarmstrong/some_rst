tests/ui-fulldeps/lint-group-forbid-always-trumps-cli.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:lint-group-plugin-test.rs
// compile-flags: -F unused -A unused

fn main() {
    let x = 1;
    //~^ ERROR unused variable: `x`
}


