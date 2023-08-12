tests/ui/binding/ambiguity-item.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Identifier pattern referring to an ambiguity item is an error (issue #46079).

mod m {
    pub fn f() {}
}
use m::*;

mod n {
    pub fn f() {}
}
use n::*; // OK, no conflict with `use m::*;`

fn main() {
    let v = f; //~ ERROR `f` is ambiguous
    match v {
        f => {} //~ ERROR `f` is ambiguous
        mut f => {} // OK, unambiguously a fresh binding due to `mut`
    }
}


