tests/ui/editions/edition-imports-virtual-2015-ambiguity.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// edition:2018
// compile-flags:--extern edition_imports_2015
// aux-build:edition-imports-2015.rs

mod edition_imports_2015 {
    pub struct Path;
}

pub struct Ambiguous {}

mod check {
    pub struct Ambiguous {}

    fn check() {
        edition_imports_2015::gen_ambiguous!(); // OK
    }
}

fn main() {}


