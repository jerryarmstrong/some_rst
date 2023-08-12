tests/ui/rfc-2497-if-let-chains/chains-without-let.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn and_chain() {
    let z;
    if true && { z = 3; true} && z == 3 {}
    //~^ ERROR E0381
}

fn and_chain_2() {
    let z;
    true && { z = 3; true} && z == 3;
    //~^ ERROR E0381
}

fn or_chain() {
    let z;
    if false || { z = 3; false} || z == 3 {}
    //~^ ERROR E0381
}

fn main() {
}


