tests/ui/pattern/usefulness/auxiliary/hidden.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub enum HiddenEnum {
    A,
    B,
    #[doc(hidden)]
    C,
}

#[derive(Default)]
pub struct HiddenStruct {
    pub one: u8,
    pub two: bool,
    #[doc(hidden)]
    pub hide: usize,
}


