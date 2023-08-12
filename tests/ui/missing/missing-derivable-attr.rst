tests/ui/missing/missing-derivable-attr.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait MyEq {
    fn eq(&self, other: &Self) -> bool;
}

struct A {
    x: isize
}

impl MyEq for isize {
    fn eq(&self, other: &isize) -> bool { *self == *other }
}

impl MyEq for A {}  //~ ERROR not all trait items implemented, missing: `eq`

fn main() {
}


