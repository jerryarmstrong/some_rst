tests/ui/iterators/iter-step-overflow-ndebug.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// compile-flags: -C debug_assertions=no

fn main() {
    let mut it = u8::MAX..;
    assert_eq!(it.next().unwrap(), 255);
    assert_eq!(it.next().unwrap(), u8::MIN);

    let mut it = i8::MAX..;
    assert_eq!(it.next().unwrap(), 127);
    assert_eq!(it.next().unwrap(), i8::MIN);
}


