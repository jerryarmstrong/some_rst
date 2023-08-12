tests/ui/span/borrowck-call-method-from-mut-aliasable.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo {
    x: isize,
}

impl Foo {
    pub fn f(&self) {}
    pub fn h(&mut self) {}
}

fn a(x: &mut Foo) {
    x.f();
    x.h();
}

fn b(x: &Foo) {
    x.f();
    x.h(); //~ ERROR cannot borrow
}

fn main() {
}


