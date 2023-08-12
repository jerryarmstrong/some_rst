types/src/unit_tests/block_metadata_test.rs
===========================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    use crate::block_metadata::BlockMetadata;
use proptest::prelude::*;
use solana_libra_canonical_serialization::test_helper::assert_canonical_encode_decode;

proptest! {
    #![proptest_config(ProptestConfig::with_cases(20))]

    #[test]
    fn test_block_metadata_canonical_serialization(data in any::<BlockMetadata>()) {
        assert_canonical_encode_decode(&data);
    }
}


