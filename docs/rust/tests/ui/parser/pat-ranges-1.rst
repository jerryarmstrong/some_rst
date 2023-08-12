tests/ui/parser/pat-ranges-1.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Parsing of range patterns

fn main() {
    let macropus!() ..= 11 = 12; //~ error: expected one of `:`, `;`, `=`, or `|`, found `..=`
}


