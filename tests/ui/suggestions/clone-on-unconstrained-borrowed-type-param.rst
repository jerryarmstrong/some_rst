tests/ui/suggestions/clone-on-unconstrained-borrowed-type-param.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
fn wat<T>(t: &T) -> T {
    t.clone() //~ ERROR E0308
}

struct Foo;

fn wut(t: &Foo) -> Foo {
    t.clone() //~ ERROR E0308
}

fn main() {
    wat(&42);
    wut(&Foo);
}


