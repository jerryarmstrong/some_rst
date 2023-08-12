tests/ui/drop-bounds/drop-bounds-impl-drop.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![deny(drop_bounds)]
// As a special exemption, `impl Drop` in the return position raises no error.
// This allows a convenient way to return an unnamed drop guard.
fn voldemort_type() -> impl Drop {
  struct Voldemort;
  impl Drop for Voldemort {
    fn drop(&mut self) {}
  }
  Voldemort
}
fn main() {
  let _ = voldemort_type();
}


