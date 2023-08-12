tests/ui/feature-gates/feature-gate-doc_masked.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[doc(masked)] //~ ERROR: `#[doc(masked)]` is experimental
extern crate std as realstd;

fn main() {}


