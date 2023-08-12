tests/ui/liveness/liveness-move-call-arg.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn take(_x: Box<isize>) {}


fn main() {

    let x: Box<isize> = Box::new(25);

    loop {
        take(x); //~ ERROR use of moved value: `x`
    }
}


