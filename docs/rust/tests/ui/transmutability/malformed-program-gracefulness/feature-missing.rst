tests/ui/transmutability/malformed-program-gracefulness/feature-missing.rs
==========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // The trait must not be available if its feature flag is absent.

#![crate_type = "lib"]

use std::mem::BikeshedIntrinsicFrom;
//~^ ERROR use of unstable library feature 'transmutability' [E0658]

use std::mem::Assume;
//~^ ERROR use of unstable library feature 'transmutability' [E0658]


