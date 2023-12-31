language/tools/test-generation/tests/arithmetic_instructions.rs
===============================================================

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
fn bytecode_add() {
    let mut state1 = AbstractState::new();
    state1.stack_push(AbstractValue::new_primitive(SignatureToken::U64));
    state1.stack_push(AbstractValue::new_primitive(SignatureToken::U64));
    let state2 = common::run_instruction(Bytecode::Add, state1);
    assert_eq!(
        state2.stack_peek(0),
        Some(AbstractValue::new_primitive(SignatureToken::U64)),
        "stack type postcondition not met"
    );
}

#[test]
fn bytecode_sub() {
    let mut state1 = AbstractState::new();
    state1.stack_push(AbstractValue::new_primitive(SignatureToken::U64));
    state1.stack_push(AbstractValue::new_primitive(SignatureToken::U64));
    let state2 = common::run_instruction(Bytecode::Sub, state1);
    assert_eq!(
        state2.stack_peek(0),
        Some(AbstractValue::new_primitive(SignatureToken::U64)),
        "stack type postcondition not met"
    );
}

#[test]
fn bytecode_mul() {
    let mut state1 = AbstractState::new();
    state1.stack_push(AbstractValue::new_primitive(SignatureToken::U64));
    state1.stack_push(AbstractValue::new_primitive(SignatureToken::U64));
    let state2 = common::run_instruction(Bytecode::Mul, state1);
    assert_eq!(
        state2.stack_peek(0),
        Some(AbstractValue::new_primitive(SignatureToken::U64)),
        "stack type postcondition not met"
    );
}

#[test]
fn bytecode_div() {
    let mut state1 = AbstractState::new();
    state1.stack_push(AbstractValue::new_primitive(SignatureToken::U64));
    state1.stack_push(AbstractValue::new_primitive(SignatureToken::U64));
    let state2 = common::run_instruction(Bytecode::Div, state1);
    assert_eq!(
        state2.stack_peek(0),
        Some(AbstractValue::new_primitive(SignatureToken::U64)),
        "stack type postcondition not met"
    );
}

#[test]
fn bytecode_mod() {
    let mut state1 = AbstractState::new();
    state1.stack_push(AbstractValue::new_primitive(SignatureToken::U64));
    state1.stack_push(AbstractValue::new_primitive(SignatureToken::U64));
    let state2 = common::run_instruction(Bytecode::Mod, state1);
    assert_eq!(
        state2.stack_peek(0),
        Some(AbstractValue::new_primitive(SignatureToken::U64)),
        "stack type postcondition not met"
    );
}


