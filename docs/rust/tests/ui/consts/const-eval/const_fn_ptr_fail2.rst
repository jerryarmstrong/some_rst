tests/ui/consts/const-eval/const_fn_ptr_fail2.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Zunleash-the-miri-inside-of-you

fn double(x: usize) -> usize {
    x * 2
}
const X: fn(usize) -> usize = double;

const fn bar(x: fn(usize) -> usize, y: usize) -> usize {
    x(y)
    //~^ ERROR evaluation of constant value failed
    //~| ERROR evaluation of constant value failed
}

const Y: usize = bar(X, 2); // FIXME: should fail to typeck someday
const Z: usize = bar(double, 2); // FIXME: should fail to typeck someday

fn main() {
    assert_eq!(Y, 4);
    assert_eq!(Z, 4);
}


