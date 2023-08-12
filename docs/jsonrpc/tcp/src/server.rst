tcp/src/server.rs
=================

Last edited: 2018-12-07 22:58:36

Contents:

.. code-block:: rs

    use std;
use std::net::SocketAddr;
use std::sync::Arc;

use tokio_service::Service as TokioService;

use jsonrpc::{middleware, MetaIoHandler, Metadata, Middleware};
use jsonrpc::futures::{future, Future, Stream, Sink};
use jsonrpc::futures::sync::{mpsc, oneshot};
use server_utils::{
	tokio_codec::Framed,
	tokio, reactor, codecs,
	SuspendableStream
};

use dispatch::{Dispatcher, SenderChannels, PeerMessageQueue};
use meta::{MetaExtractor, RequestContext, NoopExtractor};
use service::Service;

/// TCP server builder
pub struct ServerBuilder<M: Metadata = (), S: Middleware<M> = middleware::Noop> {
	executor: reactor::UninitializedExecutor,
	handler: Arc<MetaIoHandler<M, S>>,
	meta_extractor: Arc<MetaExtractor<M>>,
	channels: Arc<SenderChannels>,
	incoming_separator: codecs::Separator,
	outgoing_separator: codecs::Separator,
}

impl<M: Metadata + Default, S: Middleware<M> + 'static> ServerBuilder<M, S> {
	/// Creates new `ServerBuilder` wih given `IoHandler`
	pub fn new<T>(handler: T) -> Self where
		T: Into<MetaIoHandler<M, S>>,
	{
		Self::with_meta_extractor(handler, NoopExtractor)
	}
}

impl<M: Metadata, S: Middleware<M> + 'static> ServerBuilder<M, S> {
	/// Creates new `ServerBuilder` wih given `IoHandler`
	pub fn with_meta_extractor<T, E>(handler: T, extractor: E) -> Self where
		T: Into<MetaIoHandler<M, S>>,
		E: MetaExtractor<M> + 'static,
	{
		ServerBuilder {
			executor: reactor::UninitializedExecutor::Unspawned,
			handler: Arc::new(handler.into()),
			meta_extractor: Arc::new(extractor),
			channels: Default::default(),
			incoming_separator: Default::default(),
			outgoing_separator: Default::default(),
		}
	}

	/// Utilize existing event loop executor.
	pub fn event_loop_executor(mut self, handle: tokio::runtime::TaskExecutor) -> Self {
		self.executor = reactor::UninitializedExecutor::Shared(handle);
		self
	}

	/// Sets session meta extractor
	pub fn session_meta_extractor<T: MetaExtractor<M> + 'static>(mut self, meta_extractor: T) -> Self {
		self.meta_extractor = Arc::new(meta_extractor);
		self
	}

	/// Sets the incoming and outgoing requests separator
	pub fn request_separators(mut self, incoming: codecs::Separator, outgoing: codecs::Separator) -> Self {
		self.incoming_separator = incoming;
		self.outgoing_separator = outgoing;
		self
	}

	/// Starts a new server
	pub fn start(self, addr: &SocketAddr) -> std::io::Result<Server> {
		let meta_extractor = self.meta_extractor.clone();
		let rpc_handler = self.handler.clone();
		let channels = self.channels.clone();
		let incoming_separator = self.incoming_separator;
		let outgoing_separator = self.outgoing_separator;
		let address = addr.to_owned();
		let (tx, rx) = std::sync::mpsc::channel();
		let (stop_tx, stop_rx) = oneshot::channel();

		let executor = self.executor.initialize()?;

		executor.spawn(future::lazy(move || {
			let start = move || {
				let listener = tokio::net::TcpListener::bind(&address)?;
				let connections = SuspendableStream::new(listener.incoming());

				let server = connections.for_each(move |socket| {
					let peer_addr = socket.peer_addr().expect("Unable to determine socket peer address");
					trace!(target: "tcp", "Accepted incoming connection from {}", &peer_addr);
					let (sender, receiver) = mpsc::channel(65536);

					let context = RequestContext {
						peer_addr: peer_addr,
						sender: sender.clone(),
					};

					let meta = meta_extractor.extract(&context);
					let service = Service::new(peer_addr, rpc_handler.clone(), meta);
					let (writer, reader) = Framed::new(
		                socket,
		                codecs::StreamCodec::new(
		                    incoming_separator.clone(),
		                    outgoing_separator.clone(),
		                ),
		            ).split();

					let responses = reader.and_then(
						move |req| service.call(req).then(|response| match response {
							Err(e) => {
								warn!(target: "tcp", "Error while processing request: {:?}", e);
								future::ok(String::new())
							},
							Ok(None) => {
								trace!(target: "tcp", "JSON RPC request produced no response");
								future::ok(String::new())
							},
							Ok(Some(response_data)) => {
								trace!(target: "tcp", "Sent response: {}", &response_data);
								future::ok(response_data)
							}
						})
					);

					let peer_message_queue = {
						let mut channels = channels.lock();
						channels.insert(peer_addr.clone(), sender.clone());

						PeerMessageQueue::new(
							responses,
							receiver,
							peer_addr.clone(),
						)
					};

					let shared_channels = channels.clone();
					let writer = writer.send_all(peer_message_queue).then(move |_| {
						trace!(target: "tcp", "Peer {}: service finished", peer_addr);
						let mut channels = shared_channels.lock();
						channels.remove(&peer_addr);
						Ok(())
					});

					tokio::spawn(writer);

					Ok(())
				});

				Ok(server)
			};

			let stop = stop_rx.map_err(|_| ());
			match start() {
				Ok(server) => {
					tx.send(Ok(())).expect("Rx is blocking parent thread.");
					future::Either::A(server.select(stop)
						.map(|_| ())
						.map_err(|(e, _)| {
							error!("Error while executing the server: {:?}", e);
						}))
				},
				Err(e) => {
					tx.send(Err(e)).expect("Rx is blocking parent thread.");
					future::Either::B(stop
						.map_err(|e| {
							error!("Error while executing the server: {:?}", e);
						}))
				},
			}
		}));

		let res = rx.recv().expect("Response is always sent before tx is dropped.");

		res.map(|_| Server {
			executor: Some(executor),
			stop: Some(stop_tx),
		})
	}

	/// Returns dispatcher
	pub fn dispatcher(&self) -> Dispatcher {
		Dispatcher::new(self.channels.clone())
	}
}

/// TCP Server handle
pub struct Server {
	executor: Option<reactor::Executor>,
	stop: Option<oneshot::Sender<()>>,
}

impl Server {
	/// Closes the server (waits for finish)
	pub fn close(mut self) {
		let _ = self.stop.take().map(|sg| sg.send(()));
		self.executor.take().unwrap().close();
	}

	/// Wait for the server to finish
	pub fn wait(mut self) {
		self.executor.take().unwrap().wait();
	}
}

impl Drop for Server {
	fn drop(&mut self) {
		let _ = self.stop.take().map(|sg| sg.send(()));
		self.executor.take().map(|executor| executor.close());
	}
}


