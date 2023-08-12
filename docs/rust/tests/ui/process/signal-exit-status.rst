tests/ui/process/signal-exit-status.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// ignore-emscripten no processes
// ignore-sgx no processes
// ignore-windows
// ignore-fuchsia code returned as ZX_TASK_RETCODE_EXCEPTION_KILL, FIXME (#58590)

use std::env;
use std::process::Command;

pub fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() >= 2 && args[1] == "signal" {
        // Raise a segfault.
        unsafe { *(1 as *mut isize) = 0; }
    } else {
        let status = Command::new(&args[0]).arg("signal").status().unwrap();
        assert!(status.code().is_none());
    }
}


