tests/ui/liveness/liveness-assign/liveness-assign-imm-local-with-init.rs
========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn test() {
    let v: isize = 1; //~ NOTE first assignment
                      //~| HELP consider making this binding mutable
                      //~| SUGGESTION mut v
    v.clone();
    v = 2; //~ ERROR cannot assign twice to immutable variable `v`
           //~| NOTE cannot assign twice to immutable
    v.clone();
}

fn main() {
}


