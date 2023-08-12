tests/ui/binding/borrowed-ptr-pattern-infallible.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass


pub fn main() {
    let (&x, &y) = (&3, &'a');
    assert_eq!(x, 3);
    assert_eq!(y, 'a');
}


