tests/ui/methods/method-ambig-two-traits-cross-crate.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test an ambiguity scenario where one copy of the method is available
// from a trait imported from another crate.

// aux-build:ambig_impl_2_lib.rs
extern crate ambig_impl_2_lib;
use ambig_impl_2_lib::Me;
trait Me2 {
    fn me(&self) -> usize;
}
impl Me2 for usize { fn me(&self) -> usize { *self } }
fn main() { 1_usize.me(); } //~ ERROR E0034


