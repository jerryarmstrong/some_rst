tests/ui/pattern/usefulness/issue-71930-type-of-match-scrutinee.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

// In PR 71930, it was discovered that the code to retrieve the inferred type of a match scrutinee
// was incorrect.

fn f() -> ! {
    panic!()
}

fn g() -> usize {
    match f() { // Should infer type `bool`
        false => 0,
        true => 1,
    }
}

fn h() -> usize {
    match f() { // Should infer type `!`
    }
}

fn main() {}


