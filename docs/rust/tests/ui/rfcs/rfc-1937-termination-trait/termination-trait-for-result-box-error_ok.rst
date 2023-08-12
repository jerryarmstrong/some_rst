tests/ui/rfcs/rfc-1937-termination-trait/termination-trait-for-result-box-error_ok.rs
=====================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
use std::io::Error;

fn main() -> Result<(), Box<Error>> {
    Ok(())
}


