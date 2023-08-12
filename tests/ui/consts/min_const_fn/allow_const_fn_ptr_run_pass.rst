tests/ui/consts/min_const_fn/allow_const_fn_ptr_run_pass.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![feature(rustc_allow_const_fn_unstable)]

#![feature(rustc_attrs, staged_api)]
#![stable(feature = "rust1", since = "1.0.0")]

#[stable(feature = "rust1", since = "1.0.0")]
#[rustc_const_stable(since="1.0.0", feature = "mep")]
const fn takes_fn_ptr(_: fn()) {}

const FN: fn() = || ();

const fn gives_fn_ptr() {
    takes_fn_ptr(FN)
}

fn main() {
    gives_fn_ptr();
}


