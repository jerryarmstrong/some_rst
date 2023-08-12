rpc/src/max_slots.rs
====================

Last edited: 2023-08-11 21:38:33

Contents:

.. code-block:: rs

    use std::sync::atomic::AtomicU64;

#[derive(Default)]
pub struct MaxSlots {
    pub retransmit: AtomicU64,
    pub shred_insert: AtomicU64,
}


