runtime/src/vote_sender_types.rs
================================

Last edited: 2023-08-11 21:38:33

Contents:

.. code-block:: rs

    use {
    crate::vote_parser::ParsedVote,
    crossbeam_channel::{Receiver, Sender},
};

pub type ReplayVoteSender = Sender<ParsedVote>;
pub type ReplayVoteReceiver = Receiver<ParsedVote>;


