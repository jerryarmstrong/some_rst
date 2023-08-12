tests/rustdoc/inline_cross/auxiliary/renamed-via-module.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "foo"]

pub mod iter {
    mod range {
        pub struct StepBy;
    }
    pub use self::range::StepBy as DeprecatedStepBy;
    pub struct StepBy;
}


