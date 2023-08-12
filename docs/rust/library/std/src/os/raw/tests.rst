library/std/src/os/raw/tests.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use crate::any::TypeId;

macro_rules! ok {
    ($($t:ident)*) => {$(
        assert!(TypeId::of::<libc::$t>() == TypeId::of::<raw::$t>(),
                "{} is wrong", stringify!($t));
    )*}
}

#[test]
fn same() {
    use crate::os::raw;
    ok!(c_char c_schar c_uchar c_short c_ushort c_int c_uint c_long c_ulong
        c_longlong c_ulonglong c_float c_double);
}


