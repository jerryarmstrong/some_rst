tests/ui/parser/better-expected.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let x: [isize 3]; //~ ERROR expected one of `!`, `(`, `+`, `::`, `;`, `<`, or `]`, found `3`
}


