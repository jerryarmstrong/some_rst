ipc/src/logger.rs
=================

Last edited: 2018-12-07 22:58:36

Contents:

.. code-block:: rs

    #![allow(dead_code)]

use std::env;
use log::LevelFilter;
use env_logger::Builder;

lazy_static! {
	static ref LOG_DUMMY: bool = {
		let mut builder = Builder::new();
		builder.filter(None, LevelFilter::Info);

		if let Ok(log) = env::var("RUST_LOG") {
			builder.parse(&log);
		}

		if let Ok(_) = builder.try_init() {
			println!("logger initialized");
		}
		true
	};
}

/// Intialize log with default settings
pub fn init_log() {
	let _ = *LOG_DUMMY;
}


