tests/ui/pattern/usefulness/auxiliary/empty.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "rlib"]
pub enum EmptyForeignEnum {}

pub struct VisiblyUninhabitedForeignStruct {
    pub field: EmptyForeignEnum,
}

pub struct SecretlyUninhabitedForeignStruct {
    _priv: EmptyForeignEnum,
}


