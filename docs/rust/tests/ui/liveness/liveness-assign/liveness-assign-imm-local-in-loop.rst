tests/ui/liveness/liveness-assign/liveness-assign-imm-local-in-loop.rs
======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn test() {
    let v: isize;
    //~^ HELP consider making this binding mutable
    //~| SUGGESTION mut v
    loop {
        v = 1; //~ ERROR cannot assign twice to immutable variable `v`
               //~| NOTE cannot assign twice to immutable variable
    }
}

fn main() {
}


