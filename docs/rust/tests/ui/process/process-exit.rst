tests/ui/process/process-exit.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_imports)]
// ignore-emscripten no processes
// ignore-sgx no processes

use std::env;
use std::process::{self, Command, Stdio};

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() > 1 && args[1] == "child" {
        child();
    } else {
        parent();
    }
}

fn parent() {
    let args: Vec<String> = env::args().collect();
    let status = Command::new(&args[0]).arg("child").status().unwrap();
    assert_eq!(status.code(), Some(2));
}

fn child() -> i32 {
    process::exit(2);
}


