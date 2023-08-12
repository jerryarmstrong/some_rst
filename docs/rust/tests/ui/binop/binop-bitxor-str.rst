tests/ui/binop/binop-bitxor-str.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // error-pattern:no implementation for `String ^ String`

fn main() { let x = "a".to_string() ^ "b".to_string(); }


