tests/ui/exec-env.rs
====================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// exec-env:TEST_EXEC_ENV=22
// ignore-emscripten FIXME: issue #31622
// ignore-sgx unsupported

use std::env;

pub fn main() {
    assert_eq!(env::var("TEST_EXEC_ENV"), Ok("22".to_string()));
}


