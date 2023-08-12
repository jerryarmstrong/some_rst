tests/ui/borrowck/borrowck-move-out-of-overloaded-deref.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::rc::Rc;

pub fn main() {
    let _x = *Rc::new("hi".to_string());
    //~^ ERROR cannot move out of an `Rc`
}


