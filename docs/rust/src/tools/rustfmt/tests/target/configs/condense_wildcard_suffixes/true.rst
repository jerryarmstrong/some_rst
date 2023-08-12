src/tools/rustfmt/tests/target/configs/condense_wildcard_suffixes/true.rs
=========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-condense_wildcard_suffixes: true
// Condense wildcard suffixes

fn main() {
    let (lorem, ipsum, ..) = (1, 2, 3, 4);
}


