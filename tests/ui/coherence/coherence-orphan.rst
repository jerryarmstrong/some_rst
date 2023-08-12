tests/ui/coherence/coherence-orphan.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:coherence_orphan_lib.rs
#![feature(negative_impls)]

extern crate coherence_orphan_lib as lib;

use lib::TheTrait;

struct TheType;

impl TheTrait<usize> for isize { }
//~^ ERROR E0117

impl TheTrait<TheType> for isize { }

impl TheTrait<isize> for TheType { }

impl !Send for Vec<isize> { }
//~^ ERROR E0117

fn main() { }


