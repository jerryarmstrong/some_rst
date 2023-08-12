tests/ui/mir/mir_detects_invalid_ops.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-fail

fn main() {
    divide_by_zero();
    mod_by_zero();
    oob_error_for_slices();
}

fn divide_by_zero() {
    let y = 0;
    let _z = 1 / y; //~ ERROR this operation will panic at runtime [unconditional_panic]
}

fn mod_by_zero() {
    let y = 0;
    let _z = 1 % y; //~ ERROR this operation will panic at runtime [unconditional_panic]
}

fn oob_error_for_slices() {
    let a: *const [_] = &[1, 2, 3];
    unsafe {
        let _b = (*a)[3];
    }
}


