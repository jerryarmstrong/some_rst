tests/ui/parser/recover-field-extra-angle-brackets-in-struct-with-a-field.rs
============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct TypedArenaChunk {
    next: Option<String>>
    //~^ ERROR unmatched angle bracket
}

fn main() {}


