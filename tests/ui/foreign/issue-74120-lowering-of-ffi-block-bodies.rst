tests/ui/foreign/issue-74120-lowering-of-ffi-block-bodies.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Previously this ICE'd because `fn g()` would be lowered, but the block associated with `fn f()`
// wasn't.

// compile-flags: --crate-type=lib

extern "C" {
    fn f() {
    //~^ incorrect function inside `extern` block
        fn g() {}
    }
}


