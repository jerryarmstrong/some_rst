tests/ui/attributes/multiple-invalid.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This test checks that all expected errors occur when there are multiple invalid attributes
// on an item.

#[inline]
//~^ ERROR attribute should be applied to function or closure [E0518]
#[target_feature(enable = "sse2")]
//~^ ERROR attribute should be applied to a function
const FOO: u8 = 0;

fn main() { }


