src/tools/clippy/tests/ui/format_push_string.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![warn(clippy::format_push_string)]

fn main() {
    let mut string = String::new();
    string += &format!("{:?}", 1234);
    string.push_str(&format!("{:?}", 5678));
}


