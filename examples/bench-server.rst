examples/bench-server.rs
========================

Last edited: 2018-12-06 12:44:12

Contents:

.. code-block:: rs

    /// WebSocket server used for testing the bench example.
extern crate ws;

use ws::{Builder, Sender, Settings};

fn main() {
    Builder::new()
        .with_settings(Settings {
            max_connections: 10_000,
            ..Settings::default()
        })
        .build(|out: Sender| move |msg| out.send(msg))
        .unwrap()
        .listen("127.0.0.1:3012")
        .unwrap();
}


