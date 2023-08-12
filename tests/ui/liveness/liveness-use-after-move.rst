tests/ui/liveness/liveness-use-after-move.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {

    let x: Box<_> = 5.into();
    let y = x;

    println!("{}", *x); //~ ERROR borrow of moved value: `x`
    y.clone();
}


