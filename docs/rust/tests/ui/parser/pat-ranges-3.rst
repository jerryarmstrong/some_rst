tests/ui/parser/pat-ranges-3.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Parsing of range patterns

fn main() {
    let 10 ..= 10 + 3 = 12; //~ expected one of `:`, `;`, `=`, or `|`, found `+`
}


