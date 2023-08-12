tests/ui/did_you_mean/issue-49746-unicode-confusable-in-float-literal-expt.rs
=============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    const UNIVERSAL_GRAVITATIONAL_CONSTANT: f64 = 6.674e−11; // m³⋅kg⁻¹⋅s⁻²
//~^ ERROR expected at least one digit in exponent
//~| ERROR unknown start of token: \u{2212}
//~| ERROR cannot subtract `{integer}` from `{float}`

fn main() {}


