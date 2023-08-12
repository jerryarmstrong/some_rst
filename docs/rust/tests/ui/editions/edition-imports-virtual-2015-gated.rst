tests/ui/editions/edition-imports-virtual-2015-gated.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018
// aux-build:edition-imports-2015.rs

#[macro_use]
extern crate edition_imports_2015;

mod check {
    gen_gated!(); //~ ERROR unresolved import `E`
}

fn main() {}


