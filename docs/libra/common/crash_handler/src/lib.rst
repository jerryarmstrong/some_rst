common/crash_handler/src/lib.rs
===============================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

use backtrace::Backtrace;
use serde::Serialize;
use solana_libra_logger::prelude::*;
use std::{
    panic::{self, PanicInfo},
    process, thread, time,
};

#[derive(Debug, Serialize)]
pub struct CrashInfo {
    details: String,
    backtrace: String,
}

/// Invoke to ensure process exits on a thread panic.
///
/// Tokio's default behavior is to catch panics and ignore them.  Invoking this function will
/// ensure that all subsequent thread panics (even Tokio threads) will report the
/// details/backtrace and then exit.
pub fn setup_panic_handler() {
    panic::set_hook(Box::new(move |pi: &PanicInfo<'_>| {
        handle_panic(pi);
    }));
}

// Formats and logs panic information
fn handle_panic(panic_info: &PanicInfo<'_>) {
    // The Display formatter for a PanicInfo contains the message, payload and location.
    let details = format!("{}", panic_info);
    let backtrace = format!("{:#?}", Backtrace::new());

    let info = CrashInfo { details, backtrace };
    crit!("{}", toml::to_string_pretty(&info).unwrap());

    // Provide some time to save the log to disk
    thread::sleep(time::Duration::from_millis(100));

    // Kill the process
    process::exit(12);
}


