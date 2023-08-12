tests/ui/lint/semicolon-in-expressions-from-macros/warn-semicolon-in-expressions-from-macros.rs
===============================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// Ensure that trailing semicolons cause warnings by default

macro_rules! foo {
    () => {
        true; //~  WARN trailing semicolon in macro
              //~| WARN this was previously
    }
}

fn main() {
    let _val = match true {
        true => false,
        _ => foo!()
    };
}


