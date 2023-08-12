tests/ui/feature-gates/feature-gate-rustdoc_internals.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[doc(keyword = "match")] //~ ERROR: `#[doc(keyword)]` is meant for internal use only
/// wonderful
mod foo {}

trait Mine {}

#[doc(fake_variadic)]  //~ ERROR: `#[doc(fake_variadic)]` is meant for internal use only
impl<T> Mine for (T,) {}

fn main() {}


