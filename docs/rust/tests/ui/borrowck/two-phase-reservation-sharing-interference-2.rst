tests/ui/borrowck/two-phase-reservation-sharing-interference-2.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test for #56254. The last example originally failed with the ast checker, was
// accidentally allowed under migrate/nll, then linted against in migrate mode
// but disallowed under NLL. Now, we accept it everywhere.

//ignore-compare-mode-polonius

fn double_conflicts() {
    let mut v = vec![0, 1, 2];
    let shared = &v;

    v.extend(shared);
    //~^ ERROR cannot borrow `v` as mutable
}

fn activation_conflict() {
    let mut v = vec![0, 1, 2];

    v.extend(&v);
    //~^ ERROR cannot borrow `v` as mutable
}

fn reservation_allowed() {
    let mut v = vec![0, 1, 2];
    let shared = &v;

    v.push(shared.len());
}

fn main() {}


