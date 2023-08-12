tests/ui/repr/repr-transparent-issue-87496.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for the ICE described in #87496.

// check-pass

#[repr(transparent)]
struct TransparentCustomZst(());
extern "C" {
    fn good17(p: TransparentCustomZst);
    //~^ WARNING: `extern` block uses type `TransparentCustomZst`, which is not FFI-safe
}

fn main() {}


