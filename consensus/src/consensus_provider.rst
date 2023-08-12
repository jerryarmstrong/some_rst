consensus/src/consensus_provider.rs
===================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

use failure::prelude::*;
use solana_libra_config::config::NodeConfig;
use solana_libra_network::validator_network::{ConsensusNetworkEvents, ConsensusNetworkSender};

use crate::chained_bft::chained_bft_consensus_provider::ChainedBftProvider;
use grpcio::{ChannelBuilder, EnvBuilder};
use solana_libra_executor::Executor;
use solana_libra_mempool::proto::mempool::MempoolClient;
use solana_libra_state_synchronizer::StateSyncClient;
use solana_libra_storage_client::{StorageRead, StorageReadServiceClient};
use solana_libra_vm_runtime::MoveVM;
use std::sync::Arc;

/// Public interface to a consensus protocol.
pub trait ConsensusProvider {
    /// Spawns new threads, starts the consensus operations (retrieve txns, consensus protocol,
    /// execute txns, commit txns, update txn status in the mempool, etc).
    /// The function returns after consensus has recovered its initial state,
    /// and has established the required connections (e.g., to mempool and
    /// executor).
    fn start(&mut self) -> Result<()>;

    /// Stop the consensus operations. The function returns after graceful shutdown.
    fn stop(&mut self);
}

/// Helper function to create a ConsensusProvider based on configuration
pub fn make_consensus_provider(
    node_config: &mut NodeConfig,
    network_sender: ConsensusNetworkSender,
    network_receiver: ConsensusNetworkEvents,
    executor: Arc<Executor<MoveVM>>,
    state_sync_client: Arc<StateSyncClient>,
) -> Box<dyn ConsensusProvider> {
    Box::new(ChainedBftProvider::new(
        node_config,
        network_sender,
        network_receiver,
        create_mempool_client(node_config),
        executor,
        state_sync_client,
    ))
}
/// Create a mempool client assuming the mempool is running on localhost
fn create_mempool_client(config: &NodeConfig) -> Arc<MempoolClient> {
    let port = config.mempool.mempool_service_port;
    let connection_str = format!("localhost:{}", port);

    let env = Arc::new(EnvBuilder::new().name_prefix("grpc-con-mem-").build());
    Arc::new(MempoolClient::new(
        ChannelBuilder::new(env).connect(&connection_str),
    ))
}

/// Create a storage read client based on the config
pub fn create_storage_read_client(config: &NodeConfig) -> Arc<dyn StorageRead> {
    let env = Arc::new(EnvBuilder::new().name_prefix("grpc-con-sto-").build());
    Arc::new(StorageReadServiceClient::new(
        env,
        &config.storage.address,
        config.storage.port,
    ))
}


