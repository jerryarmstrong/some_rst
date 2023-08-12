tests/ui/self/point-at-arbitrary-self-type-method.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct A;

impl A {
    fn foo(self: Box<Self>) {}
}

fn main() {
    A.foo(); //~ ERROR E0599
}


