tests/ui/rfc-1937-termination-trait/termination-trait-for-result-box-error_err.rs
=================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// error-pattern:returned Box<Error> from main()
// failure-status: 1
// ignore-emscripten no processes

use std::io::{Error, ErrorKind};

fn main() -> Result<(), Box<Error>> {
    Err(Box::new(Error::new(ErrorKind::Other, "returned Box<Error> from main()")))
}


