tests/ui/borrowck/borrowck-borrow-immut-deref-of-box-as-mut.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct A;

impl A {
    fn foo(&mut self) {
    }
}



pub fn main() {
    let a: Box<_> = Box::new(A);
    a.foo();
    //~^ ERROR cannot borrow `*a` as mutable, as `a` is not declared as mutable [E0596]
}


