tests/xcrate.rs
===============

Last edited: 2021-03-09 06:50:06

Contents:

.. code-block:: rs

    cfg_if::cfg_if! {
    if #[cfg(foo)] {
        fn works() -> bool { false }
    } else if #[cfg(test)] {
        fn works() -> bool { true }
    } else {
        fn works() -> bool { false }
    }
}

#[test]
fn smoke() {
    assert!(works());
}


