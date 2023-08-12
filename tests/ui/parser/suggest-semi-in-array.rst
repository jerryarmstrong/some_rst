tests/ui/parser/suggest-semi-in-array.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let v = [1
    2];
    //~^ ERROR expected one of `,`, `.`, `;`, `?`, `]`, or an operator, found `2`
}


