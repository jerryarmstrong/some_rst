tests/ui/parser/range-3.rs
==========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test range syntax - syntax errors.

pub fn main() {
    let r = 1..2..3;
    //~^ ERROR expected one of `.`, `;`, `?`, `else`, or an operator, found `..`
}


