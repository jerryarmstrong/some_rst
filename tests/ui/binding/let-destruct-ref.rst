tests/ui/binding/let-destruct-ref.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

pub fn main() {
    let x = 3_usize;
    let ref y = x;
    assert_eq!(x, *y);
}


