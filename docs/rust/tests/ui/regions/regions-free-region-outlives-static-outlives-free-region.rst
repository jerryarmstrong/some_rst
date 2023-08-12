tests/ui/regions/regions-free-region-outlives-static-outlives-free-region.rs
============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
// Test that we recognize that if you have
//
//     'a : 'static
//
// then
//
//     'a : 'b

fn test<'a,'b>(x: &'a i32) -> &'b i32
    where 'a: 'static //~ WARN unnecessary lifetime parameter `'a`
{
    x
}

fn main() { }


