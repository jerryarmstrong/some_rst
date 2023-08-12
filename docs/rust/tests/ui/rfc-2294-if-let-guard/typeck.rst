tests/ui/rfc-2294-if-let-guard/typeck.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(if_let_guard)]

fn ok() -> Result<Option<bool>, ()> {
    Ok(Some(true))
}

fn main() {
    match ok() {
        Ok(x) if let Err(_) = x => {},
        //~^ ERROR mismatched types
        Ok(x) if let 0 = x => {},
        //~^ ERROR mismatched types
        _ => {}
    }
}


