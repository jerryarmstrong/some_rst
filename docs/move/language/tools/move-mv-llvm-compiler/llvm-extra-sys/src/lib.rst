language/tools/move-mv-llvm-compiler/llvm-extra-sys/src/lib.rs
==============================================================

Last edited: 2023-08-11 19:18:44

Contents:

.. code-block:: rs

    // Copyright (c) The Diem Core Contributors
// Copyright (c) The Move Contributors
// SPDX-License-Identifier: Apache-2.0

//! Access to LLVM features not provided by the C API.

#![allow(non_snake_case)]

// These only exist in the Solana LLVM fork,
// and are not provided by the llvm-sys crate.
extern "C" {
    pub fn LLVMInitializeSBFTargetInfo();
    pub fn LLVMInitializeSBFTarget();
    pub fn LLVMInitializeSBFTargetMC();
    pub fn LLVMInitializeSBFAsmPrinter();
    pub fn LLVMInitializeSBFAsmParser();
    pub fn LLVMInitializeSBFDisassembler();
}


