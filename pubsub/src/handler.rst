pubsub/src/handler.rs
=====================

Last edited: 2018-12-07 22:58:36

Contents:

.. code-block:: rs

    use core;
use core::futures::{Future, IntoFuture};

use types::{PubSubMetadata, SubscriptionId};
use subscription::{Subscriber, new_subscription};

/// Subscribe handler
pub trait SubscribeRpcMethod<M: PubSubMetadata>: Send + Sync + 'static {
	/// Called when client is requesting new subscription to be started.
	fn call(&self, params: core::Params, meta: M, subscriber: Subscriber);
}

impl<M, F> SubscribeRpcMethod<M> for F where
	F: Fn(core::Params, M, Subscriber) + Send + Sync + 'static,
	M: PubSubMetadata,
{
	fn call(&self, params: core::Params, meta: M, subscriber: Subscriber) {
		(*self)(params, meta, subscriber)
	}
}

/// Unsubscribe handler
pub trait UnsubscribeRpcMethod: Send + Sync + 'static {
	/// Output type
	type Out: Future<Item = core::Value, Error = core::Error> + Send + 'static;
	/// Called when client is requesting to cancel existing subscription.
	fn call(&self, id: SubscriptionId) -> Self::Out;
}

impl<F, I> UnsubscribeRpcMethod for F where
	F: Fn(SubscriptionId) -> I + Send + Sync + 'static,
	I: IntoFuture<Item = core::Value, Error = core::Error>,
	I::Future: Send + 'static,
{
	type Out = I::Future;
	fn call(&self, id: SubscriptionId) -> Self::Out {
		(*self)(id).into_future()
	}
}

/// Publish-Subscribe extension of `IoHandler`.
pub struct PubSubHandler<T: PubSubMetadata, S: core::Middleware<T> = core::middleware::Noop> {
	handler: core::MetaIoHandler<T, S>,
}

impl<T: PubSubMetadata> Default for PubSubHandler<T> {
	fn default() -> Self {
		PubSubHandler {
			handler: Default::default(),
		}
	}
}

impl<T: PubSubMetadata, S: core::Middleware<T>> PubSubHandler<T, S> {
	/// Creates new `PubSubHandler`
	pub fn new(handler: core::MetaIoHandler<T, S>) -> Self {
		PubSubHandler {
			handler: handler,
		}
	}

	/// Adds new subscription.
	pub fn add_subscription<F, G>(
		&mut self,
		notification: &str,
		subscribe: (&str, F),
		unsubscribe: (&str, G),
	) where
		F: SubscribeRpcMethod<T>,
		G: UnsubscribeRpcMethod,
	{
		let (sub, unsub) = new_subscription(notification, subscribe.1, unsubscribe.1);
		self.handler.add_method_with_meta(subscribe.0, sub);
		self.handler.add_method_with_meta(unsubscribe.0, unsub);
	}
}

impl<T: PubSubMetadata, S: core::Middleware<T>> ::std::ops::Deref for PubSubHandler<T, S> {
	type Target = core::MetaIoHandler<T, S>;

	fn deref(&self) -> &Self::Target {
		&self.handler
	}
}

impl<T: PubSubMetadata, S: core::Middleware<T>> ::std::ops::DerefMut for PubSubHandler<T, S> {
	fn deref_mut(&mut self) -> &mut Self::Target {
		&mut self.handler
	}
}

impl<T: PubSubMetadata, S: core::Middleware<T>> Into<core::MetaIoHandler<T, S>> for PubSubHandler<T, S> {
	fn into(self) -> core::MetaIoHandler<T, S> {
		self.handler
	}
}

#[cfg(test)]
mod tests {
	use std::sync::Arc;
	use std::sync::atomic::{AtomicBool, Ordering};

	use core;
	use core::futures::future;
	use core::futures::sync::mpsc;
	use subscription::{Session, Subscriber};
	use types::{PubSubMetadata, SubscriptionId};

	use super::PubSubHandler;

	#[derive(Clone, Default)]
	struct Metadata;
	impl core::Metadata for Metadata {}
	impl PubSubMetadata for Metadata {
		fn session(&self) -> Option<Arc<Session>> {
			let (tx, _rx) = mpsc::channel(1);
			Some(Arc::new(Session::new(tx)))
		}
	}

	#[test]
	fn should_handle_subscription() {
		// given
		let mut handler = PubSubHandler::default();
		let called = Arc::new(AtomicBool::new(false));
		let called2 = called.clone();
		handler.add_subscription(
			"hello",
			("subscribe_hello", |params, _meta, subscriber: Subscriber| {
				assert_eq!(params, core::Params::None);
				let _sink = subscriber.assign_id(SubscriptionId::Number(5));
			}),
			("unsubscribe_hello", move |id| {
				// Should be called because session is dropped.
				called2.store(true, Ordering::SeqCst);
				assert_eq!(id, SubscriptionId::Number(5));
				future::ok(core::Value::Bool(true))
			}),
		);

		// when
		let meta = Metadata;
		let req = r#"{"jsonrpc":"2.0","id":1,"method":"subscribe_hello","params":null}"#;
		let res = handler.handle_request_sync(req, meta);

		// then
		let response = r#"{"jsonrpc":"2.0","result":5,"id":1}"#;
		assert_eq!(res, Some(response.into()));
		assert_eq!(called.load(Ordering::SeqCst), true);
	}

}


