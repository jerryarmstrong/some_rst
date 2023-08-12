tests/ui/parser/foreign-static-syntactic-pass.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Syntactically, a foreign static may have a body.

// check-pass

fn main() {}

#[cfg(FALSE)]
extern "C" {
    static X: u8;
    static mut Y: u8;
}


