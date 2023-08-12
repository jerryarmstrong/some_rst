tests/ui/structs/incomplete-fn-in-struct-definition.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {}

struct S {
    fn: u8 //~ ERROR expected identifier, found keyword `fn`
}


