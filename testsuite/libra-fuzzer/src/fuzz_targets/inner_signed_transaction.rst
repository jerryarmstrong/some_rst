testsuite/libra-fuzzer/src/fuzz_targets/inner_signed_transaction.rs
===================================================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

use crate::FuzzTargetImpl;
use failure::prelude::Result;
use proptest::prelude::*;
use solana_libra_canonical_serialization::{SimpleDeserializer, SimpleSerializer};
use solana_libra_proptest_helpers::ValueGenerator;
use solana_libra_types::transaction::SignedTransaction;

#[derive(Clone, Debug, Default)]
pub struct SignedTransactionTarget;

impl FuzzTargetImpl for SignedTransactionTarget {
    fn name(&self) -> &'static str {
        module_name!()
    }

    fn description(&self) -> &'static str {
        "SignedTransaction (LCS deserializer)"
    }

    fn generate(&self, _idx: usize, gen: &mut ValueGenerator) -> Option<Vec<u8>> {
        let value = gen.generate(any_with::<SignedTransaction>(()));
        Some(SimpleSerializer::serialize(&value).expect("serialization should work"))
    }

    fn fuzz(&self, data: &[u8]) {
        let _: Result<SignedTransaction> = SimpleDeserializer::deserialize(&data);
    }
}


