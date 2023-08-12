src/interfaces/mod.rs
=====================

Last edited: 2022-08-04 13:38:52

Contents:

.. code-block:: rs

    pub mod asset;
use crate::api::DigitalAssetProtocolError;
use crate::lifecycle::Lifecycle;


pub trait ContextAction {
    fn lifecycle(&self) -> &Lifecycle;
    fn run(&self) -> Result<(), DigitalAssetProtocolError>;
}

