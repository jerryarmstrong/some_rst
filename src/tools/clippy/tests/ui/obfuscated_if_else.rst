src/tools/clippy/tests/ui/obfuscated_if_else.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

#![warn(clippy::obfuscated_if_else)]

fn main() {
    true.then_some("a").unwrap_or("b");
}


