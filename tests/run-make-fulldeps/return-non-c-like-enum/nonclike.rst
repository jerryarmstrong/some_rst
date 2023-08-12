tests/run-make-fulldeps/return-non-c-like-enum/nonclike.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[repr(C, u8)]
pub enum TT {
    AA(u64, u64),
    BB,
}

#[no_mangle]
pub extern "C" fn tt_new(a: u64, b: u64) -> TT {
    TT::AA(a, b)
}

#[repr(C,u8)]
pub enum T {
    A(u64),
    B,
}

#[no_mangle]
pub extern "C" fn t_new(a: u64) -> T {
    T::A(a)
}


