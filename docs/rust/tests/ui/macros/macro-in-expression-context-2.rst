tests/ui/macros/macro-in-expression-context-2.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    macro_rules! empty { () => () }

fn main() {
    match 42 {
        _ => { empty!() }
//~^ ERROR macro expansion ends with an incomplete expression
    };
}


