tests/ui/borrowck/borrowck-move-from-unsafe-ptr.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    unsafe fn foo(x: *const Box<isize>) -> Box<isize> {
    let y = *x; //~ ERROR cannot move out of `*x` which is behind a raw pointer
    return y;
}

fn main() {
}


