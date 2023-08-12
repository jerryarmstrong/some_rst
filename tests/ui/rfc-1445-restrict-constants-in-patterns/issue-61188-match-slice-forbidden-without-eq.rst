tests/ui/rfc-1445-restrict-constants-in-patterns/issue-61188-match-slice-forbidden-without-eq.rs
================================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Issue 61188 pointed out a case where we hit an ICE during code gen:
// the compiler assumed that `PartialEq` was always implemented on any
// use of a `const` item in a pattern context, but the pre-existing
// structural-match checking was too shallow
// (see rust-lang/rust#62307), and so we hit cases where we were
// trying to dispatch to `PartialEq` on types that did not implement
// that trait.

struct B(i32);

const A: &[B] = &[];

pub fn main() {
    match &[][..] {
        A => (),
        //~^ ERROR must be annotated with `#[derive(PartialEq, Eq)]`
        _ => (),
    }
}


