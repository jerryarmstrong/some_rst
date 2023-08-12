tests/ui/typeck/issue-55810-must-typeck-match-pats-before-guards.rs
===================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

// rust-lang/rust#55810: types for a binding in a match arm can be
// inferred from arms that come later in the match.

struct S;

impl S {
    fn method(&self) -> bool {
        unimplemented!()
    }
}

fn get<T>() -> T {
    unimplemented!()
}

fn main() {
    match get() {
        x if x.method() => {}
        &S => {}
    }
}


