tests/ui/consts/const_in_pattern/incomplete-slice.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[derive(PartialEq)]
enum E {
    A,
}

const E_SL: &[E] = &[E::A];

fn main() {
    match &[][..] {
        //~^ ERROR non-exhaustive patterns: `&_` not covered [E0004]
        E_SL => {}
        //~^ WARN to use a constant of type `E` in a pattern, `E` must be annotated with `#[derive(PartialEq, Eq)]`
        //~| WARN this was previously accepted by the compiler but is being phased out
    }
}


