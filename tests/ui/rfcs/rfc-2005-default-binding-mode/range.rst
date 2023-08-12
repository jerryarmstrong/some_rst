tests/ui/rfcs/rfc-2005-default-binding-mode/range.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
pub fn main() {
    let i = 5;
    match &&&&i {
        1 ..= 3 => panic!(),
        4 ..= 8 => {},
        _ => panic!(),
    }
}


