network/netcore/src/transport/timeout.rs
========================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

// Timeout Transport

use crate::transport::Transport;
use futures::{compat::Compat01As03, future::Future, stream::Stream};
use parity_multiaddr::Multiaddr;
use pin_utils::{unsafe_pinned, unsafe_unpinned};
use std::{
    pin::Pin,
    task::{Context, Poll},
    time::{Duration, Instant},
};
use tokio::{executor::Executor, timer::Delay};

/// A [`TimeoutTransport`] is a transport which wraps another transport with a timeout on all
/// inbound and outbound connection setup.
///
/// Note: The [Listener](Transport::Listener) stream is not subject to the provided timeout.
#[derive(Debug)]
pub struct TimeoutTransport<T> {
    transport: T,
    timeout: Duration,
}

impl<T> TimeoutTransport<T> {
    /// Wraps around a [`Transport`] and adds timeouts to all inbound and outbound connections
    /// created by it.
    pub(crate) fn new(transport: T, timeout: Duration) -> Self {
        Self { transport, timeout }
    }
}

impl<T> Transport for TimeoutTransport<T>
where
    T: Transport,
    T::Error: 'static,
{
    type Output = T::Output;
    type Error = TimeoutTransportError<T::Error>;
    type Listener = TimeoutStream<T::Listener>;
    type Inbound = TimeoutFuture<T::Inbound>;
    type Outbound = TimeoutFuture<T::Outbound>;

    fn listen_on(&self, addr: Multiaddr) -> Result<(Self::Listener, Multiaddr), Self::Error> {
        let (listener, addr) = self.transport.listen_on(addr)?;
        let listener = TimeoutStream::new(listener, self.timeout);

        Ok((listener, addr))
    }

    fn dial(&self, addr: Multiaddr) -> Result<Self::Outbound, Self::Error> {
        let fut = self.transport.dial(addr)?;

        Ok(TimeoutFuture::new(fut, self.timeout))
    }
}

/// Listener stream returned by [listen_on](Transport::listen_on) on a TimeoutTransport.
#[derive(Debug)]
#[must_use = "streams do nothing unless polled"]
pub struct TimeoutStream<St> {
    inner: St,
    timeout: Duration,
}

impl<St> TimeoutStream<St>
where
    St: Stream,
{
    // This use of `unsafe_pinned` is safe because:
    //   1. This struct does not implement [`Drop`]
    //   2. This struct does not implement [`Unpin`]
    //   3. This struct is not `#[repr(packed)]`
    unsafe_pinned!(inner: St);

    fn new(stream: St, timeout: Duration) -> Self {
        Self {
            inner: stream,
            timeout,
        }
    }
}

impl<St, Fut, O, E> Stream for TimeoutStream<St>
where
    St: Stream<Item = Result<(Fut, Multiaddr), E>>,
    Fut: Future<Output = Result<O, E>>,
    E: ::std::error::Error,
{
    type Item = Result<(TimeoutFuture<Fut>, Multiaddr), TimeoutTransportError<E>>;

    fn poll_next(mut self: Pin<&mut Self>, context: &mut Context) -> Poll<Option<Self::Item>> {
        match self.as_mut().inner().poll_next(context) {
            Poll::Pending => Poll::Pending,
            Poll::Ready(None) => Poll::Ready(None),
            Poll::Ready(Some(Err(e))) => {
                Poll::Ready(Some(Err(TimeoutTransportError::TransportError(e))))
            }
            Poll::Ready(Some(Ok((fut, addr)))) => {
                let fut = TimeoutFuture::new(fut, self.timeout);
                Poll::Ready(Some(Ok((fut, addr))))
            }
        }
    }
}

/// Future which wraps an inner Future with a timeout.
#[derive(Debug)]
#[must_use = "futures do nothing unless polled"]
pub struct TimeoutFuture<F> {
    future: F,
    timeout: Compat01As03<Delay>,
}

impl<F> TimeoutFuture<F>
where
    F: Future,
{
    // This use of `unsafe_pinned` is safe because:
    //   1. This struct does not implement [`Drop`]
    //   2. This struct does not implement [`Unpin`]
    //   3. This struct is not `#[repr(packed)]`
    unsafe_pinned!(future: F);

    // This use of `unsafe_unpinned` is safe because:
    //   1. `timeout` implements `Unpin`
    //   2. We only use the generated `timeout()` getter to construct a Pin with Pin::new.
    unsafe_unpinned!(timeout: Compat01As03<Delay>);

    fn new(future: F, timeout: Duration) -> Self {
        let deadline = Instant::now() + timeout;
        Self {
            future,
            timeout: Compat01As03::new(Delay::new(deadline)),
        }
    }
}

impl<F, O, E> Future for TimeoutFuture<F>
where
    F: Future<Output = Result<O, E>>,
    E: ::std::error::Error,
{
    type Output = Result<O, TimeoutTransportError<E>>;

    fn poll(mut self: Pin<&mut Self>, mut context: &mut Context) -> Poll<Self::Output> {
        // Make sure we're inside of a Tokio Runtime since Tokio Timers
        // don't work outside of a Tokio context.
        assert!(tokio::executor::DefaultExecutor::current().status().is_ok());

        // Try polling the inner future first
        match self.as_mut().future().poll(&mut context) {
            Poll::Pending => {}
            Poll::Ready(Err(e)) => {
                return Poll::Ready(Err(TimeoutTransportError::TransportError(e)))
            }
            Poll::Ready(Ok(output)) => return Poll::Ready(Ok(output)),
        }

        // Now check to see if we've overshot the timeout
        match Pin::new(self.as_mut().timeout()).poll(&mut context) {
            Poll::Pending => Poll::Pending,
            Poll::Ready(Err(err)) => Poll::Ready(Err(TimeoutTransportError::TimerError(err))),
            Poll::Ready(Ok(())) => Poll::Ready(Err(TimeoutTransportError::Timeout)),
        }
    }
}

#[derive(Debug)]
pub enum TimeoutTransportError<E> {
    Timeout,
    TimerError(::tokio::timer::Error),
    TransportError(E),
}

impl<E> ::std::convert::From<E> for TimeoutTransportError<E> {
    fn from(error: E) -> Self {
        TimeoutTransportError::TransportError(error)
    }
}

impl<E> ::std::fmt::Display for TimeoutTransportError<E>
where
    E: ::std::fmt::Display,
{
    fn fmt(&self, f: &mut ::std::fmt::Formatter<'_>) -> ::std::fmt::Result {
        match self {
            TimeoutTransportError::Timeout => write!(f, "Timeout has been reached"),
            TimeoutTransportError::TimerError(err) => write!(f, "Error in the timer: '{}'", err),
            TimeoutTransportError::TransportError(err) => write!(f, "{}", err),
        }
    }
}

impl<E> ::std::error::Error for TimeoutTransportError<E>
where
    E: ::std::error::Error + 'static,
{
    fn source(&self) -> Option<&(dyn ::std::error::Error + 'static)> {
        match self {
            TimeoutTransportError::Timeout => None,
            TimeoutTransportError::TimerError(err) => Some(err),
            TimeoutTransportError::TransportError(err) => Some(err),
        }
    }
}


