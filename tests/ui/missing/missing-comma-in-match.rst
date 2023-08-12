tests/ui/missing/missing-comma-in-match.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

fn main() {
    match &Some(3) {
        &None => 1
        &Some(2) => { 3 }
        //~^ ERROR expected one of `,`, `.`, `?`, `}`, or an operator, found `=>`
        //~| NOTE expected one of `,`, `.`, `?`, `}`, or an operator
        _ => 2
    };
}


