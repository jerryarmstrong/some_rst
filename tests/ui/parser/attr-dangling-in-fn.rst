tests/ui/parser/attr-dangling-in-fn.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // error-pattern:expected statement

fn f() {
  #[foo = "bar"]
}

fn main() {
}


