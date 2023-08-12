tests/ui/mismatched_types/assignment-operator-unimplemented.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo;

fn main() {
  let mut a = Foo;
  let ref b = Foo;
  a += *b; //~ Error: binary assignment operation `+=` cannot be applied to type `Foo`
}


