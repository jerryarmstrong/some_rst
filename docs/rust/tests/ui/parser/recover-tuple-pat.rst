tests/ui/parser/recover-tuple-pat.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // NOTE: This doesn't recover anymore.

fn main() {
    let x = (1, 2, 3, 4);
    match x {
        (1, .., 4) => {}
        (1, .=., 4) => { let _: usize = ""; }
        //~^ ERROR expected pattern, found `.`
        (.=., 4) => {}
        (1, 2, 3, 4) => {}
    }
}


