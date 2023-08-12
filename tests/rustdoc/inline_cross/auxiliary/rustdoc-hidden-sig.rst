tests/rustdoc/inline_cross/auxiliary/rustdoc-hidden-sig.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub struct Bar;

impl Bar {
    pub fn bar(_: u8) -> hidden::Hidden {
        hidden::Hidden
    }
}

#[doc(hidden)]
pub mod hidden {
    pub struct Hidden;
}


