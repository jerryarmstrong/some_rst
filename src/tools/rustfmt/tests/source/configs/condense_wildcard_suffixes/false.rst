src/tools/rustfmt/tests/source/configs/condense_wildcard_suffixes/false.rs
==========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-condense_wildcard_suffixes: false
// Condense wildcard suffixes

fn main() {
    let (lorem, ipsum, _, _) = (1, 2, 3, 4);
}


