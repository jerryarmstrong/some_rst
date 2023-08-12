tests/ui/rfc-1445-restrict-constants-in-patterns/match-empty-array-allowed-without-eq-issue-62336.rs
====================================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Pre-existing behavior has been to reject patterns with consts
// denoting non-empty arrays of non-`Eq` types, but *accept* empty
// arrays of such types.
//
// See rust-lang/rust#62336.

// run-pass

#[derive(PartialEq, Debug)]
struct B(i32);

fn main() {
    const FOO: [B; 0] = [];
    match [] {
        FOO => { }
    }
}


