tests/ui/rfcs/rfc-1937-termination-trait/termination-trait-for-box-dyn-error.rs
===============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
    Ok(())
}


