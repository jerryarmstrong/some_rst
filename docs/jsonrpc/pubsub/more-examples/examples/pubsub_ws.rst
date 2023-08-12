pubsub/more-examples/examples/pubsub_ws.rs
==========================================

Last edited: 2018-12-07 22:58:36

Contents:

.. code-block:: rs

    extern crate solana_jsonrpc_core as jsonrpc_core;
extern crate solana_jsonrpc_pubsub as jsonrpc_pubsub;
extern crate solana_jsonrpc_ws_server as jsonrpc_ws_server;

use std::{time, thread};
use std::sync::Arc;

use jsonrpc_core::*;
use jsonrpc_pubsub::{PubSubHandler, Session, Subscriber, SubscriptionId};
use jsonrpc_ws_server::{ServerBuilder, RequestContext};

use jsonrpc_core::futures::Future;

/// Use following node.js code to test:
///
/// ```js
/// const WebSocket = require('websocket').w3cwebsocket;
///
/// const ws = new WebSocket('ws://localhost:3030');
/// ws.addEventListener('open', () => {
///   console.log('Sending request');
///
///   ws.send(JSON.stringify({
///     jsonrpc: "2.0",
///     id: 1,
///     method: "subscribe_hello",
///     params: null,
///   }));
/// });
///
/// ws.addEventListener('message', (message) => {
///   console.log('Received: ', message.data);
/// });
///
/// console.log('Starting');
/// ```
fn main() {
	let mut io = PubSubHandler::new(MetaIoHandler::default());
	io.add_method("say_hello", |_params: Params| {
		Ok(Value::String("hello".to_string()))
	});

	io.add_subscription(
		"hello",
		("subscribe_hello", |params: Params, _, subscriber: Subscriber| {
			if params != Params::None {
				subscriber.reject(Error {
					code: ErrorCode::ParseError,
					message: "Invalid parameters. Subscription rejected.".into(),
					data: None,
				}).unwrap();
				return;
			}

			let sink = subscriber.assign_id(SubscriptionId::Number(5)).unwrap();
			// or subscriber.reject(Error {} );
			// or drop(subscriber)
			thread::spawn(move || {
				loop {
					thread::sleep(time::Duration::from_millis(1000));
					match sink.notify(Params::Array(vec![Value::Number(10.into())])).wait() {
						Ok(_) => {},
						Err(_) => {
							println!("Subscription has ended, finishing.");
							break;
						}
					}
				}
			});
		}),
		("remove_hello", |_id: SubscriptionId| -> BoxFuture<Value> {
			println!("Closing subscription");
			Box::new(futures::future::ok(Value::Bool(true)))
		}),
	);

	let server = ServerBuilder::with_meta_extractor(io, |context: &RequestContext| Arc::new(Session::new(context.sender())))
		.start(&"127.0.0.1:3030".parse().unwrap())
		.expect("Unable to start RPC server");

	let _ = server.wait();
}


