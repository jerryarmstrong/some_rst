http/examples/http_async.rs
===========================

Last edited: 2018-12-07 22:58:36

Contents:

.. code-block:: rs

    extern crate solana_jsonrpc_http_server as jsonrpc_http_server;

use jsonrpc_http_server::{ServerBuilder, DomainsValidation, AccessControlAllowOrigin};
use jsonrpc_http_server::jsonrpc_core::*;

fn main() {
	let mut io = IoHandler::default();
	io.add_method("say_hello", |_params| {
		futures::finished(Value::String("hello".to_owned()))
	});

	let server = ServerBuilder::new(io)
		.cors(DomainsValidation::AllowOnly(vec![AccessControlAllowOrigin::Null]))
		.start_http(&"127.0.0.1:3030".parse().unwrap())
		.expect("Unable to start RPC server");

	server.wait();
}


