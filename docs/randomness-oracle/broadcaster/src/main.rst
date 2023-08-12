broadcaster/src/main.rs
=======================

Last edited: 2021-12-14 12:31:39

Contents:

.. code-block:: rs

    mod broadcaster;
mod subscriber;
mod utils;

use broadcaster::*;
use serde::{Deserialize, Serialize};
use solana_sdk::signature::Keypair;
use std::fs;
use subscriber::*;

#[derive(Serialize, Deserialize)]
struct Config {
    pub rpc: String,
    pub key: Vec<u8>,
}

#[tokio::main]
async fn main() {
    let data = fs::read_to_string("./conf.json").expect("Unable to read file");
    let v: Config = serde_json::from_str(data.as_ref()).unwrap();
    let broadcaster = Broadcaster::new(v.rpc.clone(), Keypair::from_bytes(v.key.as_ref()).unwrap());

    let subscriber = Subscriber::new(v.rpc);
    subscriber.run(&broadcaster).await.unwrap();
}


