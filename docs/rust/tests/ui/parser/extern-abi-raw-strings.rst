tests/ui/parser/extern-abi-raw-strings.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

// Check that the string literal in `extern lit` will accept raw strings.

fn main() {}

extern r#"C"# fn foo() {}

extern r#"C"# {
    fn bar();
}

type T = extern r#"C"# fn();


