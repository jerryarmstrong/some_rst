tests/ui/array-slice-vec/subslice-only-once-semantic-restriction.rs
===================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let a: &[u8] = &[];
    match a {
        [1, tail @ .., tail @ ..] => {},
        //~^ ERROR identifier `tail` is bound more than once in the same pattern
        //~| ERROR `..` can only be used once per slice pattern
        _ => ()
    }
}

const RECOVERY_WITNESS: () = 0; //~ ERROR mismatched types


