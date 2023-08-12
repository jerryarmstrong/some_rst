tests/ui/impl-trait/region-escape-via-bound.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we do not allow the region `'x` to escape in the impl
// trait **even though** `'y` escapes, which outlives `'x`.
//
// See https://github.com/rust-lang/rust/issues/46541 for more details.

#![allow(dead_code)]

use std::cell::Cell;

trait Trait<'a> { }

impl<'a, 'b> Trait<'b> for Cell<&'a u32> { }

fn foo<'x, 'y>(x: Cell<&'x u32>) -> impl Trait<'y>
where 'x: 'y
{
    x
    //~^ ERROR hidden type for `impl Trait<'y>` captures lifetime that does not appear in bounds [E0700]
}

fn main() { }


