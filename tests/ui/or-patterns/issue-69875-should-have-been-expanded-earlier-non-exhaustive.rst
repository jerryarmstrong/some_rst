tests/ui/or-patterns/issue-69875-should-have-been-expanded-earlier-non-exhaustive.rs
====================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let (0 | (1 | 2)) = 0; //~ ERROR refutable pattern in local binding
    match 0 {
        //~^ ERROR non-exhaustive patterns
        0 | (1 | 2) => {}
    }
}


