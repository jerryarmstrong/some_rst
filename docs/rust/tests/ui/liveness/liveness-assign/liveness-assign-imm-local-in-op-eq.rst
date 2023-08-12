tests/ui/liveness/liveness-assign/liveness-assign-imm-local-in-op-eq.rs
=======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn test() {
    let v: isize;
    //~^ HELP consider making this binding mutable
    //~| SUGGESTION mut v
    v = 2;  //~ NOTE first assignment
    v += 1; //~ ERROR cannot assign twice to immutable variable `v`
            //~| NOTE cannot assign twice to immutable
    v.clone();
}

fn main() {
}


