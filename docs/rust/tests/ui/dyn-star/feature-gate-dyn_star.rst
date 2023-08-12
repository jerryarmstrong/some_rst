tests/ui/dyn-star/feature-gate-dyn_star.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Feature gate test for dyn_star

/// dyn* is not necessarily the final surface syntax (if we have one at all),
/// but for now we will support it to aid in writing tests independently.
pub fn dyn_star_parameter(_: &dyn* Send) {
    //~^ dyn* trait objects are unstable
}

fn main() {}


