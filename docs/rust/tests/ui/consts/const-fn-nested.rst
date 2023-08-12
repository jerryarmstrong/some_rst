tests/ui/consts/const-fn-nested.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Test a call whose argument is the result of another call.

const fn sub(x: u32, y: u32) -> u32 {
    x - y
}

const X: u32 = sub(sub(88, 44), 22);

fn main() {
    assert_eq!(X, 22);
}


