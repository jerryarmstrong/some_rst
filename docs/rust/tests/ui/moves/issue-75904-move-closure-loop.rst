tests/ui/moves/issue-75904-move-closure-loop.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for issue #75904
// Tests that we point at an expression
// that required the upvar to be moved, rather than just borrowed.

struct NotCopy;

fn main() {
    let mut a = NotCopy;
    loop {
        || { //~ ERROR use of moved value
            &mut a;
            a;
        };
    }
}


