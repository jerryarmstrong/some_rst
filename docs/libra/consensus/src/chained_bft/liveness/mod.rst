consensus/src/chained_bft/liveness/mod.rs
=========================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

pub(crate) mod multi_proposer_election;
pub(crate) mod pacemaker;
pub(crate) mod pacemaker_timeout_manager;
pub(crate) mod proposal_generator;
pub(crate) mod proposer_election;
pub(crate) mod rotating_proposer_election;

#[cfg(test)]
mod multi_proposer_test;
#[cfg(test)]
mod pacemaker_test;
#[cfg(test)]
mod rotating_proposer_test;


