tests/ui/parser/unbalanced-doublequote.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // error-pattern: unterminated double quote string


fn main() {
    "
}


