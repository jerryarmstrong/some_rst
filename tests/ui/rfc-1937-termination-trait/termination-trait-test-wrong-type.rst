tests/ui/rfc-1937-termination-trait/termination-trait-test-wrong-type.rs
========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --test

use std::num::ParseFloatError;

#[test]
fn can_parse_zero_as_f32() -> Result<f32, ParseFloatError> { //~ ERROR
    "0".parse()
}


