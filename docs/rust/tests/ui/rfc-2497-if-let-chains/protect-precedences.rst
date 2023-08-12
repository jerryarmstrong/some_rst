tests/ui/rfc-2497-if-let-chains/protect-precedences.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(irrefutable_let_patterns)]

fn main() {
    let x: bool;
    // This should associate as: `(x = (true && false));`.
    x = true && false;
    assert!(!x);

    fn _f1() -> bool {
        // Should associate as `(let _ = (return (true && false)))`.
        if let _ = return true && false {};
        //~^ WARNING unreachable block in `if`
    }
    assert!(!_f1());
}


