tests/ui/nll/issue-98589-closures-relate-named-regions.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for #98589.
// Previously, named lifetime `'a` that appears in the closure was unrelated to `'a`
// that appears in the parent function iff `'a` is early-bound.
// This made the following tests pass borrowck.

// check-fail

// The bound `'a: 'a` ensures that `'a` is early-bound.
fn test_early_early<'a: 'a, 'b: 'b>() {
    || { None::<&'a &'b ()>; };
    //~^ ERROR lifetime may not live long enough
}

fn test_early_late<'a: 'a, 'b>() {
    || { None::<&'a &'b ()>; };
    //~^ ERROR lifetime may not live long enough
}

// No early-bound lifetime; included for completeness.
fn test_late_late<'a, 'b>() {
    || { None::<&'a &'b ()>; };
    //~^ ERROR lifetime may not live long enough
}

fn test_early_type<'a: 'a, T>() {
    || { None::<&'a T>; };
    //~^ ERROR the parameter type `T` may not live long enough
}

// No early-bound lifetime; included for completeness.
fn test_late_type<'a, T>() {
    || { None::<&'a T>; };
    //~^ ERROR the parameter type `T` may not live long enough
}

fn main() {}


