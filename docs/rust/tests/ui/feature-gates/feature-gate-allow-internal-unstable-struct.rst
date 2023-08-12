tests/ui/feature-gates/feature-gate-allow-internal-unstable-struct.rs
=====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // checks that this attribute is caught on non-macro items.
// this needs a different test since this is done after expansion

#[allow_internal_unstable()] //~ ERROR allow_internal_unstable side-steps
//~| ERROR attribute should
struct S;

fn main() {}


