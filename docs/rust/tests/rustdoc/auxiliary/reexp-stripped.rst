tests/rustdoc/auxiliary/reexp-stripped.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub use private::Quz;
pub use hidden::Bar;

mod private {
    pub struct Quz;
}

#[doc(hidden)]
pub mod hidden {
    pub struct Bar;
}


