tests/ui/inference/cannot-infer-async.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018

use std::io::Error;

fn make_unit() -> Result<(), Error> {
    Ok(())
}

fn main() {
    let fut = async {
        make_unit()?;

        Ok(())
        //~^ ERROR type annotations needed
    };
}


