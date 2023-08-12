tests/ui/maximal_mir_to_hir_coverage.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Zmaximal-hir-to-mir-coverage
// run-pass

// Just making sure this flag is accepted and doesn't crash the compiler

fn main() {
  let x = 1;
  let y = x + 1;
  println!("{y}");
}


