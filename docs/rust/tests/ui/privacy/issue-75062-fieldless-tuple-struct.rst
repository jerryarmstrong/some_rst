tests/ui/privacy/issue-75062-fieldless-tuple-struct.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for issue #75062
// Tests that we don't ICE on a privacy error for a fieldless tuple struct.

mod foo {
    struct Bar();
}

fn main() {
    foo::Bar(); //~ ERROR tuple struct
}


