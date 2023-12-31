network/socket_bench_server/src/lib.rs
======================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

use bytes::Bytes;
use futures::{
    compat::Sink01CompatExt,
    future::{Future, FutureExt, TryFutureExt},
    io::{AsyncRead, AsyncReadExt, AsyncWrite},
    sink::SinkExt,
    stream::{Stream, StreamExt},
};
use parity_multiaddr::Multiaddr;
use solana_libra_memsocket::MemorySocket;
use solana_libra_netcore::{
    multiplexing::{yamux::Yamux, StreamMultiplexer},
    transport::{
        memory::MemoryTransport,
        tcp::{TcpSocket, TcpTransport},
        Transport, TransportExt,
    },
};
use solana_libra_noise::{NoiseConfig, NoiseSocket};
use std::{convert::TryInto, env, ffi::OsString, sync::Arc};
use tokio::{codec::Framed, runtime::TaskExecutor};
use unsigned_varint::codec::UviBytes;

#[derive(Debug)]
pub struct Args {
    pub tcp_addr: Option<Multiaddr>,
    pub tcp_noise_addr: Option<Multiaddr>,
    pub tcp_muxer_addr: Option<Multiaddr>,
    pub tcp_noise_muxer_addr: Option<Multiaddr>,
    pub msg_lens: Option<Vec<usize>>,
}

fn parse_addr(s: OsString) -> Multiaddr {
    s.into_string()
        .expect("Error: Address should be valid Unicode")
        .try_into()
        .expect("Error: Address should be a multiaddr")
}

fn parse_msg_lens(s: OsString) -> Vec<usize> {
    let s = s
        .into_string()
        .expect("Error: $MSG_LENS should be valid Unicode");

    // check for surrounding array brackets
    if &s[..1] != "[" || &s[s.len() - 1..] != "]" {
        panic!(
            "Error: Malformed $MSG_LENS: \"{}\": Should be formatted like an array \"[123, 456]\"",
            s
        );
    }

    // parse Vec<usize> from comma-delimited string
    s[1..s.len() - 1]
        .split(',')
        .map(|ss| {
            ss.trim()
                .parse::<usize>()
                .expect("Error: Malformed $MSG_LENS: Failed to parse usize")
        })
        .collect()
}

impl Args {
    pub fn from_env() -> Self {
        Self {
            tcp_addr: env::var_os("TCP_ADDR").map(parse_addr),
            tcp_noise_addr: env::var_os("TCP_NOISE_ADDR").map(parse_addr),
            tcp_muxer_addr: env::var_os("TCP_MUXER_ADDR").map(parse_addr),
            tcp_noise_muxer_addr: env::var_os("TCP_NOISE_MUXER_ADDR").map(parse_addr),
            msg_lens: env::var_os("MSG_LENS").map(parse_msg_lens),
        }
    }
}

/// Build a MemorySocket + Noise transport
pub fn build_memsocket_noise_transport() -> impl Transport<Output = NoiseSocket<MemorySocket>> {
    MemoryTransport::default().and_then(move |socket, origin| {
        async move {
            let noise_config = Arc::new(NoiseConfig::new_random());
            let (_remote_static_key, socket) =
                noise_config.upgrade_connection(socket, origin).await?;
            Ok(socket)
        }
    })
}

/// Build a MemorySocket + Muxer transport
pub fn build_memsocket_muxer_transport() -> impl Transport<Output = impl StreamMultiplexer> {
    MemoryTransport::default().and_then(Yamux::upgrade_connection)
}

/// Build a MemorySocket + Noise + Muxer transport
pub fn build_memsocket_noise_muxer_transport() -> impl Transport<Output = impl StreamMultiplexer> {
    MemoryTransport::default()
        .and_then(move |socket, origin| {
            async move {
                let noise_config = Arc::new(NoiseConfig::new_random());
                let (_remote_static_key, socket) =
                    noise_config.upgrade_connection(socket, origin).await?;
                Ok(socket)
            }
        })
        .and_then(Yamux::upgrade_connection)
}

/// Build a Tcp + Noise transport
pub fn build_tcp_noise_transport() -> impl Transport<Output = NoiseSocket<TcpSocket>> {
    TcpTransport::default().and_then(move |socket, origin| {
        async move {
            let noise_config = Arc::new(NoiseConfig::new_random());
            let (_remote_static_key, socket) =
                noise_config.upgrade_connection(socket, origin).await?;
            Ok(socket)
        }
    })
}

/// Build a Tcp + Muxer transport
pub fn build_tcp_muxer_transport() -> impl Transport<Output = impl StreamMultiplexer> {
    TcpTransport::default().and_then(Yamux::upgrade_connection)
}

/// Build a Tcp + Noise + Muxer transport
pub fn build_tcp_noise_muxer_transport() -> impl Transport<Output = impl StreamMultiplexer> {
    TcpTransport::default()
        .and_then(move |socket, origin| {
            async move {
                let noise_config = Arc::new(NoiseConfig::new_random());
                let (_remote_static_key, socket) =
                    noise_config.upgrade_connection(socket, origin).await?;
                Ok(socket)
            }
        })
        .and_then(Yamux::upgrade_connection)
}

/// Server side handler for send throughput benchmark when the messages are sent
/// over a simple stream (tcp or in-memory).
pub async fn server_stream_handler<L, I, S, E>(mut server_listener: L)
where
    L: Stream<Item = Result<(I, Multiaddr), E>> + Unpin,
    I: Future<Output = Result<S, E>>,
    S: AsyncRead + AsyncWrite + Unpin,
    E: ::std::error::Error,
{
    // Wait for next inbound connection
    while let Some(Ok((f_stream, _client_addr))) = server_listener.next().await {
        let stream = f_stream.await.unwrap();
        let mut stream = Framed::new(stream.compat(), UviBytes::<Bytes>::default()).sink_compat();

        // Drain all messages from the client.
        while let Some(_) = stream.next().await {}
        stream.close().await.unwrap();
    }
}

/// Server side handler for send throughput benchmark when the messages are sent
/// over a muxer substream.
pub async fn server_muxer_handler<L, I, M, E>(mut server_listener: L)
where
    L: Stream<Item = Result<(I, Multiaddr), E>> + Unpin,
    I: Future<Output = Result<M, E>>,
    M: StreamMultiplexer,
    E: ::std::error::Error,
{
    // Wait for next inbound connection
    while let Some(Ok((f_muxer, _client_addr))) = server_listener.next().await {
        let muxer = f_muxer.await.unwrap();

        // Wait for inbound client substream
        let mut muxer_inbounds = muxer.listen_for_inbound();
        let substream = muxer_inbounds.next().await.unwrap().unwrap();
        let mut stream =
            Framed::new(substream.compat(), UviBytes::<Bytes>::default()).sink_compat();

        // Drain all messages from the client.
        while let Some(_) = stream.next().await {}
        stream.close().await.unwrap();
    }
}

pub fn start_stream_server<T, L, I, S, E>(
    executor: &TaskExecutor,
    transport: T,
    listen_addr: Multiaddr,
) -> Multiaddr
where
    T: Transport<Output = S, Error = E, Listener = L, Inbound = I>,
    L: Stream<Item = Result<(I, Multiaddr), E>> + Unpin + Send + 'static,
    I: Future<Output = Result<S, E>> + Send + 'static,
    S: AsyncRead + AsyncWrite + Unpin + Send + 'static,
    E: ::std::error::Error + Send + Sync + 'static,
{
    let (listener, server_addr) = transport.listen_on(listen_addr).unwrap();
    executor.spawn(
        server_stream_handler(listener)
            .boxed()
            .unit_error()
            .compat(),
    );
    server_addr
}

pub fn start_muxer_server<T, L, I, M, E>(
    executor: &TaskExecutor,
    transport: T,
    listen_addr: Multiaddr,
) -> Multiaddr
where
    T: Transport<Output = M, Error = E, Listener = L, Inbound = I>,
    L: Stream<Item = Result<(I, Multiaddr), E>> + Unpin + Send + 'static,
    I: Future<Output = Result<M, E>> + Send + 'static,
    M: StreamMultiplexer + 'static,
    E: ::std::error::Error + Send + Sync + 'static,
{
    let (listener, server_addr) = transport.listen_on(listen_addr).unwrap();
    executor.spawn(server_muxer_handler(listener).boxed().unit_error().compat());
    server_addr
}


