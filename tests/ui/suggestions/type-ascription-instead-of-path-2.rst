tests/ui/suggestions/type-ascription-instead-of-path-2.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
fn main() -> Result<(), ()> {
    let _ = vec![Ok(2)].into_iter().collect:<Result<Vec<_>,_>>()?;
    //~^ ERROR expected `::`, found `(`
    Ok(())
}


