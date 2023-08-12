send-transaction-service/src/tpu_info.rs
========================================

Last edited: 2023-08-11 21:38:33

Contents:

.. code-block:: rs

    use {solana_client::connection_cache::Protocol, std::net::SocketAddr};

pub trait TpuInfo {
    fn refresh_recent_peers(&mut self);
    fn get_leader_tpus(&self, max_count: u64, protocol: Protocol) -> Vec<&SocketAddr>;
}

#[derive(Clone)]
pub struct NullTpuInfo;

impl TpuInfo for NullTpuInfo {
    fn refresh_recent_peers(&mut self) {}
    fn get_leader_tpus(&self, _max_count: u64, _protocol: Protocol) -> Vec<&SocketAddr> {
        vec![]
    }
}


