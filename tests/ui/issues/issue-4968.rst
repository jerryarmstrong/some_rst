tests/ui/issues/issue-4968.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for issue #4968

const A: (isize,isize) = (4,2);
fn main() {
    match 42 { A => () }
    //~^ ERROR mismatched types
    //~| expected type `{integer}`
    //~| found tuple `(isize, isize)`
    //~| expected integer, found tuple
}


