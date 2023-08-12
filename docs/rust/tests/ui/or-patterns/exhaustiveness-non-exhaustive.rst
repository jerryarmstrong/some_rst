tests/ui/or-patterns/exhaustiveness-non-exhaustive.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(unreachable_patterns)]

// We wrap patterns in a tuple because top-level or-patterns were special-cased.
fn main() {
    match (0u8, 0u8) {
        //~^ ERROR non-exhaustive patterns: `(2_u8..=u8::MAX, _)`
        (0 | 1, 2 | 3) => {}
    }
    match ((0u8,),) {
        //~^ ERROR non-exhaustive patterns: `((4_u8..=u8::MAX))`
        ((0 | 1,) | (2 | 3,),) => {}
    }
    match (Some(0u8),) {
        //~^ ERROR non-exhaustive patterns: `(Some(2_u8..=u8::MAX))`
        (None | Some(0 | 1),) => {}
    }
}


