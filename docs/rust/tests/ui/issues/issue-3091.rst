tests/ui/issues/issue-3091.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

pub fn main() {
    let x = 1;
    let y = 1;
    assert_eq!(&x, &y);
}


