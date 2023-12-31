language/tools/test-generation/tests/transaction_instructions.rs
================================================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

extern crate solana_libra_test_generation;
use solana_libra_test_generation::abstract_state::{AbstractState, AbstractValue};
use solana_libra_vm::file_format::{Bytecode, SignatureToken};

mod common;

#[test]
fn bytecode_gettxngasunitprice() {
    let state1 = AbstractState::new();
    let state2 = common::run_instruction(Bytecode::GetTxnGasUnitPrice, state1);
    assert_eq!(
        state2.stack_peek(0),
        Some(AbstractValue::new_primitive(SignatureToken::U64)),
        "stack type postcondition not met"
    );
}

#[test]
fn bytecode_gettxnmaxgasunits() {
    let state1 = AbstractState::new();
    let state2 = common::run_instruction(Bytecode::GetTxnMaxGasUnits, state1);
    assert_eq!(
        state2.stack_peek(0),
        Some(AbstractValue::new_primitive(SignatureToken::U64)),
        "stack type postcondition not met"
    );
}

#[test]
fn bytecode_gettxnsequencenumber() {
    let state1 = AbstractState::new();
    let state2 = common::run_instruction(Bytecode::GetTxnSequenceNumber, state1);
    assert_eq!(
        state2.stack_peek(0),
        Some(AbstractValue::new_primitive(SignatureToken::U64)),
        "stack type postcondition not met"
    );
}

#[test]
fn bytecode_getgasremaining() {
    let state1 = AbstractState::new();
    let state2 = common::run_instruction(Bytecode::GetGasRemaining, state1);
    assert_eq!(
        state2.stack_peek(0),
        Some(AbstractValue::new_primitive(SignatureToken::U64)),
        "stack type postcondition not met"
    );
}

#[test]
fn bytecode_gettxnsenderaddress() {
    let state1 = AbstractState::new();
    let state2 = common::run_instruction(Bytecode::GetTxnSenderAddress, state1);
    assert_eq!(
        state2.stack_peek(0),
        Some(AbstractValue::new_primitive(SignatureToken::Address)),
        "stack type postcondition not met"
    );
}

#[test]
fn bytecode_gettxnpublickey() {
    let state1 = AbstractState::new();
    let state2 = common::run_instruction(Bytecode::GetTxnPublicKey, state1);
    assert_eq!(
        state2.stack_peek(0),
        Some(AbstractValue::new_primitive(SignatureToken::ByteArray)),
        "stack type postcondition not met"
    );
}


