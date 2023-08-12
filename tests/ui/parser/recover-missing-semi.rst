tests/ui/parser/recover-missing-semi.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let _: usize = ()
    //~^ ERROR mismatched types
    //~| ERROR expected `;`
    let _ = 3;
}

fn foo() -> usize {
    let _: usize = ()
    //~^ ERROR mismatched types
    //~| ERROR expected `;`
    return 3;
}


