tests/ui/rfc-1445-restrict-constants-in-patterns/cant-hide-behind-direct-struct-param.rs
========================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This is part of a set of tests exploring the different ways a
// structural-match ADT might try to hold a
// non-structural-match in hidden manner that lets matches
// through that we had intended to reject.
//
// See discussion on rust-lang/rust#62307 and rust-lang/rust#62339
#![warn(indirect_structural_match)]
struct NoDerive(i32);

// This impl makes NoDerive irreflexive.
impl PartialEq for NoDerive { fn eq(&self, _: &Self) -> bool { false } }

impl Eq for NoDerive { }

#[derive(PartialEq, Eq)]
struct WrapParam<T>(T);

const WRAP_DIRECT_PARAM: WrapParam<NoDerive> = WrapParam(NoDerive(0));

fn main() {
    match WRAP_DIRECT_PARAM {
        WRAP_DIRECT_PARAM => { panic!("WRAP_DIRECT_PARAM matched itself"); }
        //~^ ERROR must be annotated with `#[derive(PartialEq, Eq)]`
        _ => { println!("WRAP_DIRECT_PARAM did not match itself"); }
    }
}


