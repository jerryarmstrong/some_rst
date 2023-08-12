tests/ui/parser/pat-ranges-4.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Parsing of range patterns

fn main() {
    let 10 - 3 ..= 10 = 8;
    //~^ error: expected one of `...`, `..=`, `..`, `:`, `;`, `=`, or `|`, found `-`
}


