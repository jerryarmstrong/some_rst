tests/ui/rfc-2005-default-binding-mode/slice.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub fn main() {
    let sl: &[u8] = b"foo";

    match sl { //~ ERROR non-exhaustive patterns
        [first, remainder @ ..] => {},
    };
}


