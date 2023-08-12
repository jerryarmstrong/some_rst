tests/ui/suggestions/suggest-box.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

fn main() {
    let _x: Box<dyn Fn() -> Result<(), ()>> = || { //~ ERROR mismatched types
        Err(())?;
        Ok(())
    };
}


