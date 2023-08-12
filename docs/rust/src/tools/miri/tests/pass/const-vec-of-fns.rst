src/tools/miri/tests/pass/const-vec-of-fns.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    /*!
 * Try to double-check that static fns have the right size (with or
 * without dummy env ptr, as appropriate) by iterating a size-2 array.
 * If the static size differs from the runtime size, the second element
 * should be read as a null or otherwise wrong pointer and crash.
 */

fn f() {}
static mut CLOSURES: &'static mut [fn()] = &mut [f as fn(), f as fn()];

pub fn main() {
    unsafe {
        for closure in &mut *CLOSURES {
            (*closure)()
        }
    }
}


