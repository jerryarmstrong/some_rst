tests/ui/main-wrong-type.rs
===========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct S {
    x: isize,
    y: isize,
}

fn main(foo: S) {
//~^ ERROR: `main` function has wrong type [E0580]
}


