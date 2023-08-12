plerkle/src/config.rs
=====================

Last edited: 2023-08-03 21:06:53

Contents:

.. code-block:: rs

    use std::env;

use tracing_subscriber::fmt;

pub fn init_logger() {
    // tracing doesn't seem to load RUST_LOG even though its supposed to, set it
    // manually
    let env_filter = env::var("RUST_LOG").unwrap_or_else(|_| "info".to_string());
    fmt()
        .with_env_filter(env_filter)
        .event_format(fmt::format::json())
        .init();
}


