gossip/src/deprecated.rs
========================

Last edited: 2023-08-11 21:38:33

Contents:

.. code-block:: rs

    use solana_sdk::clock::Slot;

#[derive(Serialize, Deserialize, Clone, Debug, PartialEq, Eq, AbiExample, AbiEnumVisitor)]
enum CompressionType {
    Uncompressed,
    GZip,
    BZip2,
}

impl Default for CompressionType {
    fn default() -> Self {
        Self::Uncompressed
    }
}

#[derive(Serialize, Deserialize, Clone, Debug, Default, PartialEq, Eq, AbiExample)]
pub(crate) struct EpochIncompleteSlots {
    first: Slot,
    compression: CompressionType,
    compressed_list: Vec<u8>,
}


