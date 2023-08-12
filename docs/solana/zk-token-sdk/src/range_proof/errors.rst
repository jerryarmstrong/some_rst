zk-token-sdk/src/range_proof/errors.rs
======================================

Last edited: 2023-08-11 21:38:33

Contents:

.. code-block:: rs

    //! Errors related to proving and verifying range proofs.
use {
    crate::errors::{ProofVerificationError, TranscriptError},
    thiserror::Error,
};

#[derive(Error, Clone, Debug, Eq, PartialEq)]
#[error("range proof verification failed: {0}")]
pub struct RangeProofError(#[from] pub(crate) ProofVerificationError);
impl_from_transcript_error!(RangeProofError);


