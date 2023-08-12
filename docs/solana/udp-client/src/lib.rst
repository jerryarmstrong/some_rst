udp-client/src/lib.rs
=====================

Last edited: 2023-08-11 21:38:33

Contents:

.. code-block:: rs

    #![allow(clippy::integer_arithmetic)]

pub mod nonblocking;
pub mod udp_client;

use {
    crate::{
        nonblocking::udp_client::UdpClientConnection as NonblockingUdpConnection,
        udp_client::UdpClientConnection as BlockingUdpConnection,
    },
    solana_connection_cache::{
        connection_cache::{
            BaseClientConnection, ClientError, ConnectionManager, ConnectionPool,
            ConnectionPoolError, Protocol,
        },
        connection_cache_stats::ConnectionCacheStats,
    },
    std::{
        net::{IpAddr, Ipv4Addr, SocketAddr, UdpSocket},
        sync::Arc,
    },
};

pub struct UdpPool {
    connections: Vec<Arc<Udp>>,
}
impl ConnectionPool for UdpPool {
    type BaseClientConnection = Udp;
    type NewConnectionConfig = UdpConfig;

    fn add_connection(&mut self, config: &Self::NewConnectionConfig, addr: &SocketAddr) {
        let connection = self.create_pool_entry(config, addr);
        self.connections.push(connection);
    }

    fn num_connections(&self) -> usize {
        self.connections.len()
    }

    fn get(&self, index: usize) -> Result<Arc<Self::BaseClientConnection>, ConnectionPoolError> {
        self.connections
            .get(index)
            .cloned()
            .ok_or(ConnectionPoolError::IndexOutOfRange)
    }

    fn create_pool_entry(
        &self,
        config: &Self::NewConnectionConfig,
        _addr: &SocketAddr,
    ) -> Arc<Self::BaseClientConnection> {
        Arc::new(Udp(config.udp_socket.clone()))
    }
}

pub struct UdpConfig {
    udp_socket: Arc<UdpSocket>,
}

impl UdpConfig {
    fn new() -> Result<Self, ClientError> {
        let socket = solana_net_utils::bind_with_any_port(IpAddr::V4(Ipv4Addr::UNSPECIFIED))
            .map_err(Into::<ClientError>::into)?;
        Ok(Self {
            udp_socket: Arc::new(socket),
        })
    }
}

pub struct Udp(Arc<UdpSocket>);
impl BaseClientConnection for Udp {
    type BlockingClientConnection = BlockingUdpConnection;
    type NonblockingClientConnection = NonblockingUdpConnection;

    fn new_blocking_connection(
        &self,
        addr: SocketAddr,
        _stats: Arc<ConnectionCacheStats>,
    ) -> Arc<Self::BlockingClientConnection> {
        Arc::new(BlockingUdpConnection::new_from_addr(self.0.clone(), addr))
    }

    fn new_nonblocking_connection(
        &self,
        addr: SocketAddr,
        _stats: Arc<ConnectionCacheStats>,
    ) -> Arc<Self::NonblockingClientConnection> {
        Arc::new(NonblockingUdpConnection::new_from_addr(
            self.0.try_clone().unwrap(),
            addr,
        ))
    }
}

#[derive(Default)]
pub struct UdpConnectionManager {}

impl ConnectionManager for UdpConnectionManager {
    type ConnectionPool = UdpPool;
    type NewConnectionConfig = UdpConfig;

    const PROTOCOL: Protocol = Protocol::UDP;

    fn new_connection_pool(&self) -> Self::ConnectionPool {
        UdpPool {
            connections: Vec::default(),
        }
    }

    fn new_connection_config(&self) -> Self::NewConnectionConfig {
        UdpConfig::new().unwrap()
    }
}


