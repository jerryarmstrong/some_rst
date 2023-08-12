language/vm/vm_runtime/vm_runtime_types/src/unit_tests/value_prop_tests.rs
==========================================================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

use crate::{loaded_data::types::Type, value::Value};

use proptest::prelude::*;

proptest! {
    #[test]
    fn flat_struct_test(value in Value::struct_strategy()) {
        let struct_def = match value.to_type_FOR_TESTING() {
            Type::Struct(struct_def) => struct_def,
            _ => panic!("Expected StructDef"),
        };
        let blob = value.simple_serialize().expect("must serialize");
        let value1 = Value::simple_deserialize(&blob, struct_def).expect("must deserialize");
        assert!(value.equals(&value1).unwrap());
    }
}


