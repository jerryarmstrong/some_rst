tests/ui/parser/issue-100197-mut-let.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

fn main() {
    mut let _x = 123;
    //~^ ERROR invalid variable declaration
}


