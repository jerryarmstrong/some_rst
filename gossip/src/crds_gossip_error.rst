gossip/src/crds_gossip_error.rs
===============================

Last edited: 2023-08-11 21:38:33

Contents:

.. code-block:: rs

    #[derive(PartialEq, Eq, Debug)]
pub enum CrdsGossipError {
    NoPeers,
    PushMessageTimeout,
    PushMessageOldVersion,
    BadPruneDestination,
    PruneMessageTimeout,
}


