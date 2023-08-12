tests/ui/mut-function-arguments.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn f(mut y: Box<isize>) {
    *y = 5;
    assert_eq!(*y, 5);
}

fn g() {
    let frob = |mut q: Box<isize>| { *q = 2; assert_eq!(*q, 2); };
    let w = Box::new(37);
    frob(w);

}

pub fn main() {
    let z = Box::new(17);
    f(z);
    g();
}


