tests/ui/rfc-2005-default-binding-mode/for.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo {}

pub fn main() {
    let mut tups = vec![(Foo {}, Foo {})];
    // The below desugars to &(ref n, mut m).
    for (n, mut m) in &tups {
        //~^ ERROR cannot move out of a shared reference
    }
}


