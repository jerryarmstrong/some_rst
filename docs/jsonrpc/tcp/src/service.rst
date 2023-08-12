tcp/src/service.rs
==================

Last edited: 2018-12-07 22:58:36

Contents:

.. code-block:: rs

    use std::sync::Arc;
use std::net::SocketAddr;

use tokio_service;

use jsonrpc::{middleware, FutureResult, Metadata, MetaIoHandler, Middleware};

pub struct Service<M: Metadata = (), S: Middleware<M> = middleware::Noop> {
	handler: Arc<MetaIoHandler<M, S>>,
	peer_addr: SocketAddr,
	meta: M,
}

impl<M: Metadata, S: Middleware<M>> Service<M, S> {
	pub fn new(peer_addr: SocketAddr, handler: Arc<MetaIoHandler<M, S>>, meta: M) -> Self {
		Service { peer_addr: peer_addr, handler: handler, meta: meta }
	}
}

impl<M: Metadata, S: Middleware<M>> tokio_service::Service for Service<M, S> {
	// These types must match the corresponding protocol types:
	type Request = String;
	type Response = Option<String>;

	// For non-streaming protocols, service errors are always io::Error
	type Error = ();

	// The future for computing the response; box it for simplicity.
	type Future = FutureResult<S::Future, S::CallFuture>;

	// Produce a future for computing a response from a request.
	fn call(&self, req: Self::Request) -> Self::Future {
		trace!(target: "tcp", "Accepted request from peer {}: {}", &self.peer_addr, req);
		self.handler.handle_request(&req, self.meta.clone())
	}
}


