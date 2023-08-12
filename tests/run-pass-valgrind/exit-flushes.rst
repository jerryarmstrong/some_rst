tests/run-pass-valgrind/exit-flushes.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // ignore-emscripten
// ignore-sgx no processes
// ignore-macos this needs valgrind 3.11 or higher; see
// https://github.com/rust-lang/rust/pull/30365#issuecomment-165763679

use std::env;
use std::process::{exit, Command};

fn main() {
    if env::args().len() > 1 {
        print!("hello!");
        exit(0);
    } else {
        let out = Command::new(env::args().next().unwrap()).arg("foo")
                          .output().unwrap();
        assert!(out.status.success());
        assert_eq!(String::from_utf8(out.stdout).unwrap(), "hello!");
        assert_eq!(String::from_utf8(out.stderr).unwrap(), "");
    }
}


