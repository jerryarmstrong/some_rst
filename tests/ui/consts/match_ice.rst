tests/ui/consts/match_ice.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // https://github.com/rust-lang/rust/issues/53708

struct S;

#[derive(PartialEq, Eq)]
struct T;

fn main() {
    const C: &S = &S;
    match C {
        C => {}
        //~^ ERROR must be annotated with `#[derive(PartialEq, Eq)]`
    }
    const K: &T = &T;
    match K {
        K => {}
    }
}


