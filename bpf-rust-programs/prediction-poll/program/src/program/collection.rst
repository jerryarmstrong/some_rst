bpf-rust-programs/prediction-poll/program/src/program/collection.rs
===================================================================

Last edited: 2020-06-24 17:49:11

Contents:

.. code-block:: rs

    use crate::result::PollError;
use prediction_poll_data::CollectionData;
use solana_sdk::{entrypoint::ProgramResult, pubkey::Pubkey};

pub fn add_poll(collection: &mut CollectionData, poll_pubkey: &Pubkey) -> ProgramResult {
    if collection.len() >= collection.capacity() {
        Err(PollError::MaxPollCapacity.into())
    } else if collection.contains(poll_pubkey) {
        Err(PollError::PollAlreadyCreated.into())
    } else {
        collection.add_poll(poll_pubkey);
        Ok(())
    }
}


