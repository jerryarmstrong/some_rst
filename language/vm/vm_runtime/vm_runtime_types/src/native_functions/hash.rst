language/vm/vm_runtime/vm_runtime_types/src/native_functions/hash.rs
====================================================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

use super::dispatch::NativeReturnStatus;
use crate::value::Value;
use sha2::{Digest, Sha256};
use solana_libra_crypto::HashValue;
use solana_libra_types::byte_array::ByteArray;
use std::collections::VecDeque;

const SHA2_COST: u64 = 30;
const SHA3_COST: u64 = 30;

pub fn native_sha2_256(mut arguments: VecDeque<Value>) -> NativeReturnStatus {
    if arguments.len() != 1 {
        return NativeReturnStatus::InvalidArguments;
    }
    let hash_arg = pop_arg!(arguments, ByteArray);
    let cost = SHA2_COST * hash_arg.len() as u64;

    let hash_vec = Sha256::digest(hash_arg.as_bytes()).to_vec();
    let return_values = vec![Value::byte_array(ByteArray::new(hash_vec))];
    NativeReturnStatus::Success {
        cost,
        return_values,
    }
}

pub fn native_sha3_256(mut arguments: VecDeque<Value>) -> NativeReturnStatus {
    if arguments.len() != 1 {
        return NativeReturnStatus::InvalidArguments;
    }
    let hash_arg = pop_arg!(arguments, ByteArray);
    let cost = SHA3_COST * hash_arg.len() as u64;

    let hash_vec = HashValue::from_sha3_256(hash_arg.as_bytes()).to_vec();
    let return_values = vec![Value::byte_array(ByteArray::new(hash_vec))];
    NativeReturnStatus::Success {
        cost,
        return_values,
    }
}


