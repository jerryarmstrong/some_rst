tests/ui/suggestions/shadowed-lplace-method-2.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(unused)]

struct X {
    x: (),
}
pub trait A {
    fn foo(&mut self, _: usize) -> &mut ();
}
impl A for X {
    fn foo(&mut self, _: usize) -> &mut () {
        &mut self.x
    }
}
impl X {
    fn foo(&mut self, _: usize) -> &mut Self {
        self
    }
}

fn main() {
    let mut x = X { x: () };
    *x.foo(0) = (); //~ ERROR E0308
}


