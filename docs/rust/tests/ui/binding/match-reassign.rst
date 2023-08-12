tests/ui/binding/match-reassign.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Regression test for #23698: The reassignment checker only cared
// about the last assignment in a match arm body

// Use an extra function to make sure no extra assignments
// are introduced by macros in the match statement
fn check_eq(x: i32, y: i32) {
    assert_eq!(x, y);
}

#[allow(unused_assignments)]
fn main() {
    let mut x = Box::new(1);
    match x {
        y => {
            x = Box::new(2);
            let _tmp = 1; // This assignment used to throw off the reassignment checker
            check_eq(*y, 1);
        }
    }
}


