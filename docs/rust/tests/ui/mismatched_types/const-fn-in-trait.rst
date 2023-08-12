tests/ui/mismatched_types/const-fn-in-trait.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Foo {
    fn f() -> u32;
    const fn g(); //~ ERROR cannot be declared const
}

impl Foo for u32 {
    const fn f() -> u32 { 22 } //~ ERROR cannot be declared const
    fn g() {}
}

fn main() { }


