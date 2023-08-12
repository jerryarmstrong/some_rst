tests/ui/parser/foreign-static-semantic-fail.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Syntactically, a foreign static may not have a body.

fn main() {}

extern "C" {
    static X: u8 = 0; //~ ERROR incorrect `static` inside `extern` block
    static mut Y: u8 = 0; //~ ERROR incorrect `static` inside `extern` block
}


