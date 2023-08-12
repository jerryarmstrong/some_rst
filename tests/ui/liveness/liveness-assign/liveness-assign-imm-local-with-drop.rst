tests/ui/liveness/liveness-assign/liveness-assign-imm-local-with-drop.rs
========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn test() {
    let b = Box::new(1); //~ NOTE first assignment
                         //~| HELP consider making this binding mutable
                         //~| SUGGESTION mut b
    drop(b);
    b = Box::new(2); //~ ERROR cannot assign twice to immutable variable `b`
                     //~| NOTE cannot assign twice to immutable
    drop(b);
}

fn main() {
}


