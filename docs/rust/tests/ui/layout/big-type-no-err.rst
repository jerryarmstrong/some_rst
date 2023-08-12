tests/ui/layout/big-type-no-err.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Enormous types are allowed if they are never actually instantiated.
// run-pass
trait Foo {
    type Assoc;
}

impl Foo for [u16; usize::MAX] {
    type Assoc = u32;
}

fn main() {
    let _a: Option<<[u16; usize::MAX] as Foo>::Assoc> = None;
}


