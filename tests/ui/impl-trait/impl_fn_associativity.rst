tests/ui/impl-trait/impl_fn_associativity.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![feature(impl_trait_in_fn_trait_return)]
use std::fmt::Debug;

fn f_debug() -> impl Fn() -> impl Debug {
    || ()
}

fn ff_debug() -> impl Fn() -> impl Fn() -> impl Debug {
    || f_debug()
}

fn multi() -> impl Fn() -> (impl Debug + Send) {
    || ()
}

fn main() {
    // Check that `ff_debug` is `() -> (() -> Debug)` and not `(() -> ()) -> Debug`
    let debug = ff_debug()()();
    assert_eq!(format!("{:?}", debug), "()");

    let x = multi()();
    assert_eq!(format!("{:?}", x), "()");
    fn assert_send(_: &impl Send) {}
    assert_send(&x);
}


