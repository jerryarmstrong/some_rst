tests/ui/auxiliary/fancy-panic.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[macro_export]
macro_rules! fancy_panic {
    () => {
        panic!("{}");
    };
    ($msg:expr) => {
        panic!($msg)
    };
}


