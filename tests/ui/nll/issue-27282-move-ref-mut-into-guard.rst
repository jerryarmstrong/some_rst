tests/ui/nll/issue-27282-move-ref-mut-into-guard.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Issue 27282: Example 1: This sidesteps the AST checks disallowing
// mutable borrows in match guards by hiding the mutable borrow in a
// guard behind a move (of the ref mut pattern id) within a closure.

#![feature(if_let_guard)]

fn main() {
    match Some(&4) {
        None => {},
        ref mut foo
            if { (|| { let bar = foo; bar.take() })(); false } => {},
        //~^ ERROR cannot move out of `foo` in pattern guard [E0507]
        Some(s) => std::process::exit(*s),
    }

    match Some(&4) {
        None => {},
        ref mut foo
            if let Some(()) = { (|| { let bar = foo; bar.take() })(); None } => {},
        //~^ ERROR cannot move out of `foo` in pattern guard [E0507]
        Some(s) => std::process::exit(*s),
    }
}


