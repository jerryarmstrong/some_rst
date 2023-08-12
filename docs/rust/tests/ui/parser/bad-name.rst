tests/ui/parser/bad-name.rs
===========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // error-pattern: expected

fn main() {
  let x.y::<isize>.z foo;
}


