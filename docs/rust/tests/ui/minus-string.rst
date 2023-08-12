tests/ui/minus-string.rs
========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // error-pattern:cannot apply unary operator `-` to type `String`

fn main() { -"foo".to_string(); }


