tests/ui/unboxed-closures/unboxed-closures-call-sugar-autoderef.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Test that the call operator autoderefs when calling a bounded type parameter.

use std::ops::FnMut;

fn call_with_2<F>(x: &mut F) -> isize
    where F : FnMut(isize) -> isize
{
    x(2) // look ma, no `*`
}

pub fn main() {
    let z = call_with_2(&mut |x| x - 22);
    assert_eq!(z, -20);
}


