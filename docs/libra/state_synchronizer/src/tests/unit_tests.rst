state_synchronizer/src/tests/unit_tests.rs
==========================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

use crate::{
    peer_manager::{PeerManager, PeerScoreUpdateType},
    PeerId,
};
use solana_libra_channel;
use solana_libra_network::validator_network::StateSynchronizerSender;
use std::collections::HashMap;

#[test]
fn test_peer_manager() {
    let peers = vec![
        PeerId::random(),
        PeerId::random(),
        PeerId::random(),
        PeerId::random(),
    ];
    let mut peer_manager = PeerManager::new(peers.clone());
    let (network_reqs_tx, _) = solana_libra_channel::new_test(8);
    let sender = StateSynchronizerSender::new(network_reqs_tx);
    for peer_id in peers.clone() {
        peer_manager.enable_peer(peer_id, sender.clone());
    }

    for _ in 0..50 {
        peer_manager.update_score(&peers[0], PeerScoreUpdateType::InvalidChunk);
    }

    let mut pick_counts = HashMap::new();
    for _ in 0..1000 {
        let (picked_peer_id, _) = peer_manager.pick_peer().unwrap();
        let counter = pick_counts.entry(picked_peer_id).or_insert(0);
        *counter += 1;
    }

    // unwrap_or needed because the peer with bad score may never be picked, and may be
    // missing from pick_counts
    assert!(pick_counts.get(&peers[0]).unwrap_or(&0) < pick_counts.get(&peers[1]).unwrap());
    assert!(pick_counts.get(&peers[0]).unwrap_or(&0) < pick_counts.get(&peers[2]).unwrap());
    assert!(pick_counts.get(&peers[0]).unwrap_or(&0) < pick_counts.get(&peers[3]).unwrap());
}

#[test]
fn test_remove_requests() {
    let peers = vec![PeerId::random(), PeerId::random()];
    let mut peer_manager = PeerManager::new(peers.clone());

    peer_manager.process_request(1, peers[0]);
    peer_manager.process_request(3, peers[1]);
    peer_manager.process_request(5, peers[0]);
    peer_manager.process_request(10, peers[0]);
    peer_manager.process_request(12, peers[1]);

    peer_manager.remove_requests(5);

    assert!(!peer_manager.has_requested(1, peers[0]));
    assert!(!peer_manager.has_requested(3, peers[1]));
    assert!(!peer_manager.has_requested(5, peers[0]));
    assert!(peer_manager.has_requested(10, peers[0]));
    assert!(peer_manager.has_requested(12, peers[1]));
}


