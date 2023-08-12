tests/rustdoc-ui/unused-braces-lint.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

// This tests the bug in #70814, where the unused_braces lint triggered on the following code
// without providing a span.

#![deny(unused_braces)]

fn main() {
    {
        {
            use std;
        }
    }
}


