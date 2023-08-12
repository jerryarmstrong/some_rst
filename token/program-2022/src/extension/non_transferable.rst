token/program-2022/src/extension/non_transferable.rs
====================================================

Last edited: 2022-07-07 18:10:20

Contents:

.. code-block:: rs

    use {
    crate::extension::{Extension, ExtensionType},
    bytemuck::{Pod, Zeroable},
};

/// Indicates that the tokens from this mint can't be transfered
#[derive(Clone, Copy, Debug, Default, PartialEq, Pod, Zeroable)]
#[repr(transparent)]
pub struct NonTransferable;

impl Extension for NonTransferable {
    const TYPE: ExtensionType = ExtensionType::NonTransferable;
}


