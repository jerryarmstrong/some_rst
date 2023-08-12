src/lifecycle.rs
================

Last edited: 2022-08-04 13:38:52

Contents:

.. code-block:: rs

    pub enum Lifecycle {
    Invalid,
    Create,
    Transfer,
    Destroy,
    Update,
    Freeze,
    Thaw,
    Split,
    Combine,
    SupplyIncrease,
    SupplyDecrease,
    ActivateExtension,
    DeactivateExtension
}

