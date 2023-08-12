ledger/src/entry_notifier_interface.rs
======================================

Last edited: 2023-08-11 21:38:33

Contents:

.. code-block:: rs

    use {
    solana_entry::entry::EntrySummary,
    solana_sdk::clock::Slot,
    std::sync::{Arc, RwLock},
};

pub trait EntryNotifier {
    fn notify_entry(&self, slot: Slot, index: usize, entry: &EntrySummary);
}

pub type EntryNotifierLock = Arc<RwLock<dyn EntryNotifier + Sync + Send>>;


