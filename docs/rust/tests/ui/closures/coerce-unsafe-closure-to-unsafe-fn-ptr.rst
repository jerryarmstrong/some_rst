tests/ui/closures/coerce-unsafe-closure-to-unsafe-fn-ptr.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // revisions: mir thir
// [thir]compile-flags: -Z thir-unsafeck

fn main() {
    let _: unsafe fn() = || { ::std::pin::Pin::new_unchecked(&0_u8); };
    //~^ ERROR E0133
    let _: unsafe fn() = || unsafe { ::std::pin::Pin::new_unchecked(&0_u8); }; // OK
}


