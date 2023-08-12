stdio/README.md
===============

Last edited: 2018-12-07 22:58:36

Contents:

.. code-block:: md

    # jsonrpc-stdio-server
STDIN/STDOUT server for JSON-RPC 2.0.
Takes one request per line and outputs each response on a new line.

[Documentation](http://paritytech.github.io/jsonrpc/jsonrpc_stdio_server/index.html)

## Example

`Cargo.toml`

```
[dependencies]
jsonrpc-stdio-server = { git = "https://github.com/paritytech/jsonrpc" }
```

`main.rs`

```rust
extern crate jsonrpc_stdio_server;

use jsonrpc_stdio_server::server;
use jsonrpc_stdio_server::jsonrpc_core::*;

fn main() {
	let mut io = IoHandler::default();
	io.add_method("say_hello", |_params| {
		Ok(Value::String("hello".to_owned()))
	});

	ServerBuilder::new(io).build();
}
```


