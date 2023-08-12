src/lib.rs
==========

Last edited: 2023-07-17 22:54:02

Contents:

.. code-block:: rs

    use solana_program::pubkey;
use solana_sdk::pubkey::Pubkey;
use spl_governance::state::vote_record::{Vote as SplVote, VoteChoice};
use std::{fmt, str::FromStr};

pub mod args;
pub mod config;
pub mod instruction;
pub mod processor;

pub enum Cluster {
    Devnet,
    Mainnet,
}

impl fmt::Display for Cluster {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            Cluster::Devnet => write!(f, "devnet"),
            Cluster::Mainnet => write!(f, "mainnet-beta"),
        }
    }
}

#[derive(Clone, Copy)]
pub enum Vote {
    Yes,
    No,
}

impl fmt::Display for Vote {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            Vote::Yes => write!(f, "yes"),
            Vote::No => write!(f, "no"),
        }
    }
}

impl FromStr for Vote {
    type Err = anyhow::Error;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        match s.to_lowercase().as_str() {
            "yes" | "yay" | "yeah" | "true" | "yea" => Ok(Vote::Yes),
            "no" | "nay" | "nah" => Ok(Vote::No),
            _ => Err(anyhow::anyhow!("Invalid vote")),
        }
    }
}

impl From<Vote> for SplVote {
    fn from(vote: Vote) -> Self {
        match vote {
            Vote::Yes => SplVote::Approve(vec![VoteChoice {
                rank: 0,
                weight_percentage: 100,
            }]),
            Vote::No => SplVote::Deny,
        }
    }
}

pub const GOVERNANCE_PROGRAM_ID: Pubkey = pubkey!("mrgTA4fqsDqtvizQBoTMGXosiwruTmu2yXZxmPNLKiJ");
pub const BPF_UPLOADER_ID: Pubkey = pubkey!("BPFLoaderUpgradeab1e11111111111111111111111");


