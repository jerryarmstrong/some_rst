src/tools/miri/tests/fail/stacked_borrows/deallocate_against_protector2.rs
==========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //@error-pattern: /deallocating while item \[SharedReadWrite for .*\] is strongly protected/
use std::marker::PhantomPinned;

pub struct NotUnpin(i32, PhantomPinned);

fn inner(x: &mut NotUnpin, f: fn(&mut NotUnpin)) {
    // `f` may mutate, but it may not deallocate!
    f(x)
}

fn main() {
    inner(Box::leak(Box::new(NotUnpin(0, PhantomPinned))), |x| {
        let raw = x as *mut _;
        drop(unsafe { Box::from_raw(raw) });
    });
}


