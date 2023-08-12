tests/ui/parser/issues/issue-3036.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

// Testing that semicolon tokens are printed correctly in errors

fn main() {
    let _x = 3 //~ ERROR: expected `;`
}


