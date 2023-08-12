tests/ui/binop/binop-mul-bool.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // error-pattern:cannot multiply `bool` by `bool`

fn main() { let x = true * false; }


