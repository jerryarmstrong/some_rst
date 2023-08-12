ws/src/server_builder.rs
========================

Last edited: 2018-12-07 22:58:36

Contents:

.. code-block:: rs

    use std::net::SocketAddr;
use std::sync::Arc;

use core;
use server_utils;
use server_utils::cors::Origin;
use server_utils::hosts::{Host, DomainsValidation};
use server_utils::reactor::UninitializedExecutor;
use server_utils::session::SessionStats;

use error::Result;
use metadata::{MetaExtractor, NoopExtractor};
use server::Server;
use session;

/// Builder for `WebSockets` server
pub struct ServerBuilder<M: core::Metadata, S: core::Middleware<M>> {
	handler: Arc<core::MetaIoHandler<M, S>>,
	meta_extractor: Arc<MetaExtractor<M>>,
	allowed_origins: Option<Vec<Origin>>,
	allowed_hosts: Option<Vec<Host>>,
	request_middleware: Option<Arc<session::RequestMiddleware>>,
	session_stats: Option<Arc<SessionStats>>,
	executor: UninitializedExecutor,
	max_connections: usize,
	max_payload_bytes: usize,
}

impl<M: core::Metadata + Default, S: core::Middleware<M>> ServerBuilder<M, S> {
	/// Creates new `ServerBuilder`
	pub fn new<T>(handler: T) -> Self where
		T: Into<core::MetaIoHandler<M, S>>,
	{
		Self::with_meta_extractor(handler, NoopExtractor)
	}
}

impl<M: core::Metadata, S: core::Middleware<M>> ServerBuilder<M, S> {
	/// Creates new `ServerBuilder`
	pub fn with_meta_extractor<T, E>(handler: T, extractor: E) -> Self where
		T: Into<core::MetaIoHandler<M, S>>,
		E: MetaExtractor<M>,
	{
		ServerBuilder {
			handler: Arc::new(handler.into()),
			meta_extractor: Arc::new(extractor),
			allowed_origins: None,
			allowed_hosts: None,
			request_middleware: None,
			session_stats: None,
			executor: UninitializedExecutor::Unspawned,
			max_connections: 100,
			max_payload_bytes: 5 * 1024 * 1024,
		}
	}

	/// Utilize existing event loop executor to poll RPC results.
	pub fn event_loop_executor(mut self, executor: server_utils::tokio::runtime::TaskExecutor) -> Self {
		self.executor = UninitializedExecutor::Shared(executor);
		self
	}

	/// Sets a meta extractor.
	pub fn session_meta_extractor<T: MetaExtractor<M>>(mut self, extractor: T) -> Self {
		self.meta_extractor = Arc::new(extractor);
		self
	}

	/// Allowed origins.
	pub fn allowed_origins(mut self, allowed_origins: DomainsValidation<Origin>) -> Self {
		self.allowed_origins = allowed_origins.into();
		self
	}

	/// Allowed hosts.
	pub fn allowed_hosts(mut self, allowed_hosts: DomainsValidation<Host>) -> Self {
		self.allowed_hosts = allowed_hosts.into();
		self
	}

	/// Session stats
	pub fn session_stats<T: SessionStats>(mut self, stats: T) -> Self {
		self.session_stats = Some(Arc::new(stats));
		self
	}

	/// Sets a request middleware. Middleware will be invoked before each handshake request.
	/// You can either terminate the handshake in the middleware or run a default behaviour after.
	pub fn request_middleware<T: session::RequestMiddleware>(mut self, middleware: T) -> Self {
		self.request_middleware = Some(Arc::new(middleware));
		self
	}

	/// Maximal number of concurrent connections this server supports.
	/// Default: 100
	pub fn max_connections(mut self, max_connections: usize) -> Self {
		self.max_connections = max_connections;
		self
	}

	/// Maximal size of the payload (in bytes)
	/// Default: 5MB
	pub fn max_payload(mut self, max_payload_bytes: usize) -> Self {
		self.max_payload_bytes = max_payload_bytes;
		self
	}

	/// Starts a new `WebSocket` server in separate thread.
	/// Returns a `Server` handle which closes the server when droped.
	pub fn start(self, addr: &SocketAddr) -> Result<Server> {
		Server::start(
			addr,
			self.handler,
			self.meta_extractor,
			self.allowed_origins,
			self.allowed_hosts,
			self.request_middleware,
			self.session_stats,
			self.executor,
			self.max_connections,
			self.max_payload_bytes,
		)
	}

}


