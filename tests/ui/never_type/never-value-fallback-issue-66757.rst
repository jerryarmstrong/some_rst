tests/ui/never_type/never-value-fallback-issue-66757.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for #66757
//
// Test than when you have a `!` value (e.g., the local variable
// never) and an uninferred variable (here the argument to `From`) it
// doesn't fallback to `()` but rather `!`.
//
// revisions: nofallback fallback
//[fallback] run-pass
//[nofallback] check-fail

#![feature(never_type)]

#![cfg_attr(fallback, feature(never_type_fallback))]

struct E;

impl From<!> for E {
    fn from(_: !) -> E {
        E
    }
}

#[allow(unreachable_code)]
#[allow(dead_code)]
#[allow(unused_must_use)]
fn foo(never: !) {
    <E as From<!>>::from(never);  // Ok
    <E as From<_>>::from(never);  //[nofallback]~ ERROR trait bound `E: From<()>` is not satisfied
}

fn main() { }


