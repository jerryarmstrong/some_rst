tests/ui/mir/mir_codegen_switchint.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
pub fn foo(x: i8) -> i32 {
  match x {
    1 => 0,
    _ => 1,
  }
}

fn main() {
  assert_eq!(foo(0), 1);
  assert_eq!(foo(1), 0);
}


