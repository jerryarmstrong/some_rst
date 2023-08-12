tests/ui/mut/mut-cant-alias.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::cell::RefCell;



fn main() {
    let m = RefCell::new(0);
    let mut b = m.borrow_mut();
    let b1 = &mut *b;
    let b2 = &mut *b; //~ ERROR cannot borrow
    b1.use_mut();
}

trait Fake { fn use_mut(&mut self) { } fn use_ref(&self) { }  }
impl<T> Fake for T { }


