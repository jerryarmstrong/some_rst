tests/ui/nll/match-cfg-fake-edges2.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we have enough false edges to avoid exposing the exact matching
// algorithm in borrow checking.

fn all_previous_tests_may_be_done(y: &mut (bool, bool)) {
    let r = &mut y.1;
    // We don't actually test y.1 to select the second arm, but we don't want
    // borrowck results to be based on the order we match patterns.
    match y { //~ ERROR cannot use `y.1` because it was mutably borrowed
        (false, true) => 1,
        (true, _) => {
            r;
            2
        }
        (false, _) => 3,
    };
}

fn main() {}


