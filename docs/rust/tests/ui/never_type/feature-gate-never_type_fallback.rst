tests/ui/never_type/feature-gate-never_type_fallback.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This is a feature gate test for `never_type_fallback`.
// It works by using a scenario where the type fall backs to `()` rather than ´!`
// in the case where `#![feature(never_type_fallback)]` would change it to `!`.

fn main() {}

trait T {}

fn should_ret_unit() {
    foo(panic!()) //~ ERROR
}

fn foo(_: impl T) {}


