programs/cardinal-reward-distributor/src/instructions/mod.rs
============================================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: rs

    pub mod claim_rewards;
pub mod close_reward_distributor;
pub mod close_reward_entry;
pub mod init_reward_distributor;
pub mod init_reward_entry;
pub mod reclaim_funds;
pub mod transfer_rewards;
pub mod update_reward_distributor;
pub mod update_reward_entry;

pub use claim_rewards::*;
pub use close_reward_distributor::*;
pub use close_reward_entry::*;
pub use init_reward_distributor::*;
pub use init_reward_entry::*;
pub use reclaim_funds::*;
pub use transfer_rewards::*;
pub use update_reward_distributor::*;
pub use update_reward_entry::*;


