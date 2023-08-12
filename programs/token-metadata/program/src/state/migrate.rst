programs/token-metadata/program/src/state/migrate.rs
====================================================

Last edited: 2023-08-11 07:39:15

Contents:

.. code-block:: rs

    use super::*;

#[repr(C)]
#[cfg_attr(feature = "serde-feature", derive(Serialize, Deserialize))]
#[derive(Clone, BorshSerialize, BorshDeserialize, Debug, PartialEq, Eq)]
pub enum MigrationType {
    CollectionV1,
    ProgrammableV1,
}


