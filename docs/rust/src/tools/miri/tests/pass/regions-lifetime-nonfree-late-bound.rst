src/tools/miri/tests/pass/regions-lifetime-nonfree-late-bound.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This is a regression test for the ICE from issue #10846.
//
// The original issue causing the ICE: the LUB-computations during
// type inference were encountering late-bound lifetimes, and
// asserting that such lifetimes should have already been substituted
// with a concrete lifetime.
//
// However, those encounters were occurring within the lexical scope
// of the binding for the late-bound lifetime; that is, the late-bound
// lifetimes were perfectly valid. The core problem was that the type
// folding code was over-zealously passing back all lifetimes when
// doing region-folding, when really all clients of the region-folding
// case only want to see *free* lifetime variables, not bound ones.

#![feature(box_syntax)]

pub fn main() {
    fn explicit() {
        fn test<F>(_x: Option<Box<F>>)
        where
            F: FnMut(Box<dyn for<'a> FnMut(&'a isize)>),
        {
        }
        test(Some(box |_f: Box<dyn for<'a> FnMut(&'a isize)>| {}));
    }

    // The code below is shorthand for the code above (and more likely
    // to represent what one encounters in practice).
    fn implicit() {
        fn test<F>(_x: Option<Box<F>>)
        where
            F: FnMut(Box<dyn FnMut(&isize)>),
        {
        }
        test(Some(box |_f: Box<dyn FnMut(&isize)>| {}));
    }

    explicit();
    implicit();
}


