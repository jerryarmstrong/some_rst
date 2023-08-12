tests/ui/unboxed-closures/unboxed-closures-infer-arg-types-w-bound-regs-from-expected-bound.rs
==============================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Test that we are able to infer that the type of `x` is `isize` based
// on the expected type from the object.

// pretty-expanded FIXME #23616

pub trait ToPrimitive {
    fn to_int(&self) {}
}

impl ToPrimitive for isize {}
impl ToPrimitive for i32 {}
impl ToPrimitive for usize {}

fn doit<T,F>(val: T, f: &F)
    where F : Fn(&T)
{
    f(&val)
}

pub fn main() {
    doit(0, &|x /*: isize*/ | { x.to_int(); });
}


