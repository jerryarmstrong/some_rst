mempool/mempool-shared-proto/src/lib.rs
=======================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    //! Proto crate for shared mempool

pub mod proto;
use crate::proto::mempool_status::MempoolAddTransactionStatusCode;
use failure::prelude::*;
use std::convert::TryFrom;

/// Status of transaction insertion operation
#[derive(Debug, PartialEq, Eq, Clone)]
pub struct MempoolAddTransactionStatus {
    /// Status code of the transaction insertion operation
    pub code: MempoolAddTransactionStatusCode,
    /// Message to give more details about the transaction insertion operation
    pub message: String,
}

impl MempoolAddTransactionStatus {
    /// Create a new MempoolAddTransactionStatus
    pub fn new(code: MempoolAddTransactionStatusCode, message: String) -> Self {
        Self { code, message }
    }
}

//***********************************
// Decoding/Encoding to Protobuffers
//***********************************
impl TryFrom<crate::proto::mempool_status::MempoolAddTransactionStatus>
    for MempoolAddTransactionStatus
{
    type Error = Error;

    fn try_from(proto: crate::proto::mempool_status::MempoolAddTransactionStatus) -> Result<Self> {
        Ok(MempoolAddTransactionStatus::new(
            proto.code(),
            proto.message,
        ))
    }
}

impl From<MempoolAddTransactionStatus>
    for crate::proto::mempool_status::MempoolAddTransactionStatus
{
    fn from(status: MempoolAddTransactionStatus) -> Self {
        let mut mempool_add_transaction_status = Self::default();
        mempool_add_transaction_status.message = status.message;
        mempool_add_transaction_status.set_code(status.code);
        mempool_add_transaction_status
    }
}


