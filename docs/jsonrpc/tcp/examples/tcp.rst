tcp/examples/tcp.rs
===================

Last edited: 2018-12-07 22:58:36

Contents:

.. code-block:: rs

    extern crate solana_jsonrpc_tcp_server as jsonrpc_tcp_server;
extern crate env_logger;

use jsonrpc_tcp_server::ServerBuilder;
use jsonrpc_tcp_server::jsonrpc_core::*;

fn main() {
	env_logger::init();
	let mut io = IoHandler::default();
	io.add_method("say_hello", |_params| {
		println!("Processing");
		Ok(Value::String("hello".to_owned()))
	});

	let server = ServerBuilder::new(io)
		.start(&"0.0.0.0:3030".parse().unwrap())
		.expect("Server must start with no issues");

	server.wait()
}


