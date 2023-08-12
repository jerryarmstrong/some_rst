tests/ui/suggestions/js-style-comparison-op.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
fn main() {
    if 1 === 1 { //~ ERROR invalid comparison operator `===`
        println!("yup!");
    } else if 1 !== 1 { //~ ERROR invalid comparison operator `!==`
        println!("nope!");
    }
}


