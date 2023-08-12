tests/ui/or-patterns/issue-69875-should-have-been-expanded-earlier.rs
=====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

fn main() {
    let (0 | (1 | _)) = 0;
    if let 0 | (1 | 2) = 0 {}
    if let x @ 0 | x @ (1 | 2) = 0 {}
}


