tests/ui/borrowck/borrowck-move-out-of-overloaded-auto-deref.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::rc::Rc;

pub fn main() {
    let _x = Rc::new(vec![1, 2]).into_iter();
    //~^ ERROR [E0507]
}


