src/tools/clippy/tests/ui/string_to_string.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![warn(clippy::string_to_string)]
#![allow(clippy::redundant_clone)]

fn main() {
    let mut message = String::from("Hello");
    let mut v = message.to_string();
}


