tests/ui/extern/extern-with-type-bounds.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(intrinsics)]

extern "rust-intrinsic" {
    // Real example from libcore
    #[rustc_safe_intrinsic]
    fn type_id<T: ?Sized + 'static>() -> u64;

    // Silent bounds made explicit to make sure they are actually
    // resolved.
    fn transmute<T: Sized, U: Sized>(val: T) -> U;

    // Bounds aren't checked right now, so this should work
    // even though it's incorrect.
    #[rustc_safe_intrinsic]
    fn size_of<T: Clone>() -> usize;

    // Unresolved bounds should still error.
    fn align_of<T: NoSuchTrait>() -> usize;
    //~^ ERROR cannot find trait `NoSuchTrait` in this scope
}

fn main() {}


