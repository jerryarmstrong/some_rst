tests/ui/coherence/coherence-fundamental-trait-objects.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that trait objects from #[fundamental] traits are not
// treated as #[fundamental] types - the 2 meanings of #[fundamental]
// are distinct.

// aux-build:coherence_fundamental_trait_lib.rs

extern crate coherence_fundamental_trait_lib;

use coherence_fundamental_trait_lib::{Fundamental, Misc};

pub struct Local;
impl Misc for dyn Fundamental<Local> {}
//~^ ERROR E0117

fn main() {}


