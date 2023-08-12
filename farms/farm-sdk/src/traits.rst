farms/farm-sdk/src/traits.rs
============================

Last edited: 2022-07-07 18:10:20

Contents:

.. code-block:: rs

    use crate::string::ArrayString64;

pub trait Named {
    fn name(&self) -> ArrayString64;
}

pub trait Versioned {
    fn version(&self) -> u16;
}


