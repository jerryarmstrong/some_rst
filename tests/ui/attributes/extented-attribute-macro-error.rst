tests/ui/attributes/extented-attribute-macro-error.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // normalize-stderr-test: "couldn't read.*" -> "couldn't read the file"

#![doc = include_str!("../not_existing_file.md")]
struct Documented {}
//~^^ ERROR couldn't read

fn main() {}


