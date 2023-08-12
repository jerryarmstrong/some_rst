tests/ui/borrowck/borrowck-reinit.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let mut x = Box::new(0);
    let _u = x; // error shouldn't note this move
    x = Box::new(1);
    drop(x);
    let _ = (1,x); //~ ERROR use of moved value: `x`
}


