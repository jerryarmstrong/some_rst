language/vm/vm_runtime/vm_runtime_types/src/unit_tests/type_prop_tests.rs
=========================================================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

use crate::loaded_data::types::Type;
use proptest::prelude::*;
use solana_libra_canonical_serialization::*;

proptest! {
    #[test]
    fn roundtrip(ty in any::<Type>()) {
        let mut serializer = SimpleSerializer::new();
        ty.serialize(&mut serializer).expect("must serialize");
        let blob: Vec<u8> = serializer.get_output();

        let mut deserializer = SimpleDeserializer::new(&blob);
        let ty2 = Type::deserialize(&mut deserializer).expect("must deserialize");
        assert_eq!(ty, ty2);
    }
}


