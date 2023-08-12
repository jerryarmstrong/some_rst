admission_control/admission_control_proto/src/proto/mod.rs
==========================================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

#![allow(bare_trait_objects)]

use ::solana_libra_types::proto::*;
use solana_libra_mempool_shared_proto::proto::mempool_status;

pub mod admission_control {
    include!(concat!(env!("OUT_DIR"), "/admission_control.rs"));
}

pub use self::admission_control::{
    AdmissionControlMsg, SubmitTransactionRequest, SubmitTransactionResponse,
};


