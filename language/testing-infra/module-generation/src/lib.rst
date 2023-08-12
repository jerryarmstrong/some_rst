language/testing-infra/module-generation/src/lib.rs
===================================================

Last edited: 2023-08-11 19:18:44

Contents:

.. code-block:: rs

    // Copyright (c) The Diem Core Contributors
// Copyright (c) The Move Contributors
// SPDX-License-Identifier: Apache-2.0

mod generator;
mod options;
mod padding;
mod utils;

pub use generator::{
    generate_module, generate_modules, generate_verified_modules, ModuleGenerator,
};
pub use options::ModuleGeneratorOptions;
pub use padding::Pad;


