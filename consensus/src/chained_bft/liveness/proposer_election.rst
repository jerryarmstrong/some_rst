consensus/src/chained_bft/liveness/proposer_election.rs
=======================================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

use crate::chained_bft::{
    common::{Author, Round},
    consensus_types::block::Block,
};

/// ProposerElection incorporates the logic of choosing a leader among multiple candidates.
/// We are open to a possibility for having multiple proposers per round, the ultimate choice
/// of a proposal is exposed by the election protocol via the stream of proposals.
pub trait ProposerElection<T> {
    /// If a given author is a valid candidate for being a proposer, generate the info,
    /// otherwise return None.
    /// Note that this function is synchronous.
    fn is_valid_proposer(&self, author: Author, round: Round) -> Option<Author>;

    /// Return all the possible valid proposers for a given round (this information can be
    /// used by e.g., voters for choosing the destinations for sending their votes to).
    fn get_valid_proposers(&self, round: Round) -> Vec<Author>;

    /// Notify proposer election about a new proposal. The function doesn't return any information:
    /// proposer election is going to notify the client about the chosen proposal via a dedicated
    /// channel (to be passed in constructor).
    fn process_proposal(&mut self, proposal: Block<T>) -> Option<Block<T>>;

    /// Take the highest ranked backup proposal if available for a given round
    /// (removes it from the struct),
    /// or returns None if no proposals have been received for a given round.
    /// A backup proposal is a valid proposal that was not chosen immediately in the
    /// `process_proposal()` return value.
    ///
    /// Note that once the backup proposal is taken and no other proposals are submitted, the
    /// following take requests are going to return None.
    fn take_backup_proposal(&mut self, round: Round) -> Option<Block<T>>;
}


