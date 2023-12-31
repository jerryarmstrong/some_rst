network/netcore/src/transport/tcp.rs
====================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

//! TCP Transport
use crate::transport::Transport;
use futures::{
    compat::{Compat01As03, Future01CompatExt},
    future::{self, Future},
    io::{AsyncRead, AsyncWrite},
    ready,
    stream::Stream,
};
use parity_multiaddr::{Multiaddr, Protocol};
use std::{
    io,
    net::{Shutdown, SocketAddr},
    pin::Pin,
    task::{Context, Poll},
    time::Duration,
};
use tokio::net::tcp::{ConnectFuture, Incoming, TcpListener, TcpStream};

/// Transport to build TCP connections
#[derive(Debug, Clone, Default)]
pub struct TcpTransport {
    /// Size of the recv buffer size to set for opened sockets, or `None` to keep default.
    recv_buffer_size: Option<usize>,
    /// Size of the send buffer size to set for opened sockets, or `None` to keep default.
    send_buffer_size: Option<usize>,
    /// TTL to set for opened sockets, or `None` to keep default.
    ttl: Option<u32>,
    /// Keep alive duration to set for opened sockets, or `None` to keep default.
    #[allow(clippy::option_option)]
    keepalive: Option<Option<Duration>>,
    /// `TCP_NODELAY` to set for opened sockets, or `None` to keep default.
    nodelay: Option<bool>,
}

impl TcpTransport {
    fn apply_config(&self, stream: &TcpStream) -> ::std::io::Result<()> {
        if let Some(size) = self.recv_buffer_size {
            stream.set_recv_buffer_size(size)?;
        }

        if let Some(size) = self.send_buffer_size {
            stream.set_send_buffer_size(size)?;
        }

        if let Some(ttl) = self.ttl {
            stream.set_ttl(ttl)?;
        }

        if let Some(keepalive) = self.keepalive {
            stream.set_keepalive(keepalive)?;
        }

        if let Some(nodelay) = self.nodelay {
            stream.set_nodelay(nodelay)?;
        }

        Ok(())
    }
}

impl Transport for TcpTransport {
    type Output = TcpSocket;
    type Error = ::std::io::Error;
    type Listener = TcpListenerStream;
    type Inbound = future::Ready<io::Result<TcpSocket>>;
    type Outbound = TcpOutbound;

    fn listen_on(&self, addr: Multiaddr) -> Result<(Self::Listener, Multiaddr), Self::Error> {
        let socket_addr = multiaddr_to_socketaddr(&addr)?;
        let config = self.clone();
        let listener = TcpListener::bind(&socket_addr)?;
        let local_addr = socketaddr_to_multiaddr(listener.local_addr()?);
        Ok((
            TcpListenerStream {
                inner: Compat01As03::new(listener.incoming()),
                config,
            },
            local_addr,
        ))
    }

    fn dial(&self, addr: Multiaddr) -> Result<Self::Outbound, Self::Error> {
        let socket_addr = multiaddr_to_socketaddr(&addr)?;
        let config = self.clone();
        let f = TcpStream::connect(&socket_addr).compat();
        Ok(TcpOutbound { inner: f, config })
    }
}

#[derive(Debug)]
#[must_use = "streams do nothing unless polled"]
pub struct TcpListenerStream {
    inner: Compat01As03<Incoming>,
    config: TcpTransport,
}

impl Stream for TcpListenerStream {
    type Item = io::Result<(future::Ready<io::Result<TcpSocket>>, Multiaddr)>;

    fn poll_next(mut self: Pin<&mut Self>, context: &mut Context) -> Poll<Option<Self::Item>> {
        match Pin::new(&mut self.inner).poll_next(context) {
            Poll::Ready(Some(Ok(socket))) => {
                if let Err(e) = self.config.apply_config(&socket) {
                    return Poll::Ready(Some(Err(e)));
                }
                let dialer_addr = match socket.peer_addr() {
                    Ok(addr) => socketaddr_to_multiaddr(addr),
                    Err(e) => return Poll::Ready(Some(Err(e))),
                };
                Poll::Ready(Some(Ok((
                    future::ready(Ok(TcpSocket::new(socket))),
                    dialer_addr,
                ))))
            }
            Poll::Ready(Some(Err(e))) => Poll::Ready(Some(Err(e))),
            Poll::Ready(None) => Poll::Ready(None),
            Poll::Pending => Poll::Pending,
        }
    }
}

#[derive(Debug)]
#[must_use = "futures do nothing unless polled"]
pub struct TcpOutbound {
    inner: Compat01As03<ConnectFuture>,
    config: TcpTransport,
}

impl Future for TcpOutbound {
    type Output = Result<TcpSocket, ::std::io::Error>;

    fn poll(mut self: Pin<&mut Self>, context: &mut Context) -> Poll<Self::Output> {
        let socket = ready!(Pin::new(&mut self.inner).poll(context))?;
        self.config.apply_config(&socket)?;
        Poll::Ready(Ok(TcpSocket::new(socket)))
    }
}

/// A wrapper around a tokio TcpStream
///
/// In order to properly implement the AsyncRead/AsyncWrite traits we need to wrap a TcpStream to
/// ensure that the "close" method actually closes the write half of the TcpStream.  This is
/// because the "close" method on a TcpStream just performs a no-op instead of actually shutting
/// down the write side of the TcpStream.
//TODO Probably should add some tests for this
#[derive(Debug)]
pub struct TcpSocket {
    inner: Compat01As03<TcpStream>,
}

impl TcpSocket {
    fn new(socket: TcpStream) -> Self {
        Self {
            inner: Compat01As03::new(socket),
        }
    }
}

impl AsyncRead for TcpSocket {
    fn poll_read(
        mut self: Pin<&mut Self>,
        context: &mut Context,
        buf: &mut [u8],
    ) -> Poll<io::Result<usize>> {
        Pin::new(&mut self.inner).poll_read(context, buf)
    }
}

impl AsyncWrite for TcpSocket {
    fn poll_write(
        mut self: Pin<&mut Self>,
        context: &mut Context,
        buf: &[u8],
    ) -> Poll<io::Result<usize>> {
        Pin::new(&mut self.inner).poll_write(context, buf)
    }

    fn poll_flush(mut self: Pin<&mut Self>, context: &mut Context) -> Poll<io::Result<()>> {
        Pin::new(&mut self.inner).poll_flush(context)
    }

    fn poll_close(self: Pin<&mut Self>, _context: &mut Context) -> Poll<io::Result<()>> {
        Poll::Ready(self.inner.get_ref().shutdown(Shutdown::Write))
    }
}

fn socketaddr_to_multiaddr(socketaddr: SocketAddr) -> Multiaddr {
    let ipaddr: Multiaddr = socketaddr.ip().into();
    ipaddr.with(Protocol::Tcp(socketaddr.port()))
}

fn multiaddr_to_socketaddr(addr: &Multiaddr) -> ::std::io::Result<SocketAddr> {
    let mut iter = addr.iter();
    let proto1 = iter.next().ok_or_else(|| {
        io::Error::new(
            io::ErrorKind::InvalidInput,
            format!("Invalid Multiaddr '{:?}'", addr),
        )
    })?;
    let proto2 = iter.next().ok_or_else(|| {
        io::Error::new(
            io::ErrorKind::InvalidInput,
            format!("Invalid Multiaddr '{:?}'", addr),
        )
    })?;

    if iter.next().is_some() {
        return Err(io::Error::new(
            io::ErrorKind::InvalidInput,
            format!("Invalid Multiaddr '{:?}'", addr),
        ));
    }

    match (proto1, proto2) {
        (Protocol::Ip4(ip), Protocol::Tcp(port)) => Ok(SocketAddr::new(ip.into(), port)),
        (Protocol::Ip6(ip), Protocol::Tcp(port)) => Ok(SocketAddr::new(ip.into(), port)),
        _ => Err(io::Error::new(
            io::ErrorKind::InvalidInput,
            format!("Invalid Multiaddr '{:?}'", addr),
        )),
    }
}

#[cfg(test)]
mod test {
    use crate::transport::{tcp::TcpTransport, ConnectionOrigin, Transport, TransportExt};
    use futures::{
        executor::block_on,
        future::{join, FutureExt},
        io::{AsyncReadExt, AsyncWriteExt},
        stream::StreamExt,
    };

    #[test]
    fn simple_listen_and_dial() -> Result<(), ::std::io::Error> {
        let t = TcpTransport::default().and_then(|mut out, connection| {
            async move {
                match connection {
                    ConnectionOrigin::Inbound => {
                        out.write_all(b"Earth").await?;
                        let mut buf = [0; 3];
                        out.read_exact(&mut buf).await?;
                        assert_eq!(&buf, b"Air");
                    }
                    ConnectionOrigin::Outbound => {
                        let mut buf = [0; 5];
                        out.read_exact(&mut buf).await?;
                        assert_eq!(&buf, b"Earth");
                        out.write_all(b"Air").await?;
                    }
                }
                Ok(())
            }
        });

        let (listener, addr) = t.listen_on("/ip4/127.0.0.1/tcp/0".parse().unwrap())?;

        let dial = t.dial(addr)?;
        let listener = listener.into_future().then(|(maybe_result, _stream)| {
            let (incoming, _addr) = maybe_result.unwrap().unwrap();
            incoming.map(Result::unwrap)
        });

        let (outgoing, _incoming) = block_on(join(dial, listener));
        assert!(outgoing.is_ok());
        Ok(())
    }

    #[test]
    fn unsupported_multiaddrs() {
        let t = TcpTransport::default();

        let result = t.listen_on("/memory/0".parse().unwrap());
        assert!(result.is_err());

        let result = t.dial("/memory/22".parse().unwrap());
        assert!(result.is_err());
    }
}


