tests/ui/self/point-at-arbitrary-self-type-trait-method.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait B { fn foo(self: Box<Self>); }
struct A;

impl B for A {
    fn foo(self: Box<Self>) {}
}

fn main() {
    A.foo() //~ ERROR E0599
}


