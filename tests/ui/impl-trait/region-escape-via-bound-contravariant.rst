tests/ui/impl-trait/region-escape-via-bound-contravariant.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // In contrast to `region-escape-via-bound-invariant`, in this case we
// *can* return a value of type `&'x u32`, even though `'x` does not
// appear in the bounds. This is because `&` is contravariant, and so
// we are *actually* returning a `&'y u32`.
//
// See https://github.com/rust-lang/rust/issues/46541 for more details.

// run-pass

#![allow(dead_code)]

trait Trait<'a> { }

impl<'a, 'b> Trait<'b> for &'a u32 { }

fn foo<'x, 'y>(x: &'x u32) -> impl Trait<'y>
where 'x: 'y
{
    x
}

fn main() { }


