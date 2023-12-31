tests/ui/borrowck/borrowck-match-binding-is-assignment.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that immutable pattern bindings cannot be reassigned.

enum E {
    Foo(isize)
}

struct S {
    bar: isize,
}

pub fn main() {
    match 1 {
        x => {
            x += 1; //~ ERROR [E0384]
        }
    }

    match E::Foo(1) {
        E::Foo(x) => {
            x += 1; //~ ERROR [E0384]
        }
    }

    match (S { bar: 1 }) {
        S { bar: x } => {
            x += 1; //~ ERROR [E0384]
        }
    }

    match (1,) {
        (x,) => {
            x += 1; //~ ERROR [E0384]
        }
    }

    match [1,2,3] {
        [x,_,_] => {
            x += 1; //~ ERROR [E0384]
        }
    }
}


