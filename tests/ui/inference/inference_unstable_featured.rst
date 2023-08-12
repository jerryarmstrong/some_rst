tests/ui/inference/inference_unstable_featured.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // There should be E0034 "multiple applicable items in scope" if we opt-in for
// the feature.

// aux-build:inference_unstable_iterator.rs
// aux-build:inference_unstable_itertools.rs

#![feature(ipu_flatten)]

extern crate inference_unstable_iterator;
extern crate inference_unstable_itertools;

use inference_unstable_iterator::IpuIterator;
use inference_unstable_itertools::IpuItertools;

fn main() {
    assert_eq!('x'.ipu_flatten(), 0);   //~ ERROR E0034
}


