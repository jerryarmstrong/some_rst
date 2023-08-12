tests/ui/regions/regions-borrow-evec-fixed.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn foo(x: &[isize]) -> isize {
    x[0]
}

pub fn main() {
    let p = &[1,2,3,4,5];
    assert_eq!(foo(p), 1);
}


