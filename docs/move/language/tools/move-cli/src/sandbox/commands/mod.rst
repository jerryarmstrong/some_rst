language/tools/move-cli/src/sandbox/commands/mod.rs
===================================================

Last edited: 2023-08-11 19:18:44

Contents:

.. code-block:: rs

    // Copyright (c) The Diem Core Contributors
// Copyright (c) The Move Contributors
// SPDX-License-Identifier: Apache-2.0

pub mod doctor;
pub mod generate;
pub mod publish;
pub mod run;
pub mod test;
pub mod view;

pub use doctor::*;
pub use publish::*;
pub use run::*;
pub use test::*;
pub use view::*;


