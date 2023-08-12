src/tools/clippy/tests/ui/string_from_utf8_as_bytes.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
#![warn(clippy::string_from_utf8_as_bytes)]

fn main() {
    let _ = std::str::from_utf8(&"Hello World!".as_bytes()[6..11]);
}


