tests/ui/rfc-1937-termination-trait/termination-trait-for-box-dyn-error.rs
==========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// error-pattern:returned Box<dyn Error> from main()
// failure-status: 1
// ignore-emscripten no processes

use std::error::Error;
use std::io;

fn main() -> Result<(), Box<dyn Error>> {
    Err(Box::new(io::Error::new(io::ErrorKind::Other, "returned Box<dyn Error> from main()")))
}


