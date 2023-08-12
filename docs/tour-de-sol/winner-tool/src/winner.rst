winner-tool/src/winner.rs
=========================

Last edited: 2020-05-07 05:29:37

Contents:

.. code-block:: rs

    use solana_sdk::pubkey::Pubkey;

#[derive(Debug)]
pub enum Category {
    Availability(String),
    ConfirmationLatency(String),
    RewardsEarned,
}

pub type Winner = (Pubkey, String);

pub struct Winners {
    pub category: Category,
    pub top_winners: Vec<Winner>,
    pub bucket_winners: Vec<(String, Vec<Winner>)>,
}


