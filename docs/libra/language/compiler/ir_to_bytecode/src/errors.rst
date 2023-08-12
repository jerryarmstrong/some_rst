language/compiler/ir_to_bytecode/src/errors.rs
==============================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

use failure::Fail;
use solana_libra_types::vm_error::VMStatus;

#[derive(Clone, Debug, Eq, Fail, Ord, PartialEq, PartialOrd)]
pub enum InternalCompilerError {
    #[fail(display = "Post-compile bounds check errors: {:?}", _0)]
    BoundsCheckErrors(Vec<VMStatus>),
}


