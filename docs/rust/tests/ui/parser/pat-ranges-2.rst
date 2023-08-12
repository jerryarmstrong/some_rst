tests/ui/parser/pat-ranges-2.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Parsing of range patterns

fn main() {
    let 10 ..= makropulos!() = 12; //~ error: expected one of `::`, `:`, `;`, `=`, or `|`, found `!`
}


