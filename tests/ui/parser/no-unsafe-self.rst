tests/ui/parser/no-unsafe-self.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait A {
    fn foo(*mut self); //~ ERROR cannot pass `self` by raw pointer
    fn baz(*const self); //~ ERROR cannot pass `self` by raw pointer
    fn bar(*self); //~ ERROR cannot pass `self` by raw pointer
}

struct X;
impl A for X {
    fn foo(*mut self) { } //~ ERROR cannot pass `self` by raw pointer
    fn baz(*const self) { } //~ ERROR cannot pass `self` by raw pointer
    fn bar(*self) { } //~ ERROR cannot pass `self` by raw pointer
}

fn main() { }


