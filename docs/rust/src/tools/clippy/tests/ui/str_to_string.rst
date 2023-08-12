src/tools/clippy/tests/ui/str_to_string.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![warn(clippy::str_to_string)]

fn main() {
    let hello = "hello world".to_string();
    let msg = &hello[..];
    msg.to_string();
}


