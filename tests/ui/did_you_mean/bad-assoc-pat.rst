tests/ui/did_you_mean/bad-assoc-pat.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    match 0u8 {
        [u8]::AssocItem => {}
        //~^ ERROR missing angle brackets in associated item path
        //~| ERROR no associated item named `AssocItem` found
        (u8, u8)::AssocItem => {}
        //~^ ERROR missing angle brackets in associated item path
        //~| ERROR no associated item named `AssocItem` found
        _::AssocItem => {}
        //~^ ERROR missing angle brackets in associated item path
        //~| ERROR no associated item named `AssocItem` found
    }
    match &0u8 {
        &(u8,)::AssocItem => {}
        //~^ ERROR missing angle brackets in associated item path
        //~| ERROR no associated item named `AssocItem` found
    }
}

macro_rules! pat {
    ($ty: ty) => ($ty::AssocItem)
    //~^ ERROR missing angle brackets in associated item path
    //~| ERROR no associated item named `AssocItem` found
}
macro_rules! ty {
    () => (u8)
}

fn check_macros() {
    match 0u8 {
        pat!(u8) => {}
        ty!()::AssocItem => {}
        //~^ ERROR missing angle brackets in associated item path
        //~| ERROR no associated item named `AssocItem` found
    }
}


