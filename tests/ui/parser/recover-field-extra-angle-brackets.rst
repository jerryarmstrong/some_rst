tests/ui/parser/recover-field-extra-angle-brackets.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Tests that we recover from extra trailing angle brackets
// in a struct field

struct BadStruct {
    first: Vec<u8>>, //~ ERROR unmatched angle bracket
    second: bool
}

fn bar(val: BadStruct) {
    val.first;
    val.second;
}

fn main() {}


