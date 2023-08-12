types/src/unit_tests/language_storage_test.rs
=============================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    use crate::language_storage::ModuleId;
use proptest::prelude::*;
use solana_libra_canonical_serialization::test_helper::assert_canonical_encode_decode;
use solana_libra_prost_ext::test_helpers::assert_protobuf_encode_decode;

proptest! {
    #[test]
    fn test_module_id_protobuf_roundtrip(module_id in any::<ModuleId>()) {
        assert_protobuf_encode_decode::<crate::proto::types::ModuleId, ModuleId>(&module_id);
    }

    #[test]
    fn test_module_id_canonical_roundtrip(module_id in any::<ModuleId>()) {
        assert_canonical_encode_decode(&module_id);
    }
}


