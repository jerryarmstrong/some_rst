tests/ui/parser/extern-abi-string-escaping.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

// Check that the string literal in `extern lit` will escapes.

fn main() {}

extern "\x43" fn foo() {}

extern "\x43" {
    fn bar();
}

type T = extern "\x43" fn();


