tests/ui/privacy/private-in-public-non-principal-2.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(auto_traits)]
#![feature(negative_impls)]

#[allow(private_in_public)]
mod m {
    pub trait PubPrincipal {}
    auto trait PrivNonPrincipal {}
    pub fn leak_dyn_nonprincipal() -> Box<dyn PubPrincipal + PrivNonPrincipal> { loop {} }
}

fn main() {
    m::leak_dyn_nonprincipal();
    //~^ ERROR trait `PrivNonPrincipal` is private
}


