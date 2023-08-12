tests/ui/resolve/auxiliary/privacy-struct-ctor.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub mod m {
    pub struct S(u8);

    pub mod n {
        pub(in m) struct Z(pub(in m::n) u8);
    }
}

pub use m::S;


