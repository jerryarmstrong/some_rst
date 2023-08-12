tests/ui/parser/raw/raw-str-unterminated.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    static s: &'static str =
    r#" string literal goes on
        and on
    //~^^ ERROR unterminated raw string


