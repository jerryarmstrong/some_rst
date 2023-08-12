src/tools/rustfmt/tests/target/issue-2955.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-condense_wildcard_suffixes: true
fn main() {
    match (1, 2, 3) {
        (..) => (),
    }
}


