language/move-core/types/src/state.rs
=====================================

Last edited: 2023-08-11 19:18:44

Contents:

.. code-block:: rs

    // Copyright (c) The Diem Core Contributors
// Copyright (c) The Move Contributors
// SPDX-License-Identifier: Apache-2.0

use std::cell::RefCell;

#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub enum VMState {
    DESERIALIZER,
    VERIFIER,
    RUNTIME,
    OTHER,
}

thread_local! {
    static STATE: RefCell<VMState> = RefCell::new(VMState::OTHER);
}

pub fn set_state(state: VMState) -> VMState {
    STATE.with(|s| s.replace(state))
}

pub fn get_state() -> VMState {
    STATE.with(|s| *s.borrow())
}


