tests/ui/suggestions/suggest-semicolon-for-fn-in-extern-block.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

#[allow(dead_code)]

extern "C" {
  fn foo() //~ERROR expected `;`
}

fn main() {}


