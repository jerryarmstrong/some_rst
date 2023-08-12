tests/ui/statics/auxiliary/static_fn_inline_xc_aux.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub mod num {
    pub trait Num2 {
        fn from_int2(n: isize) -> Self;
    }
}

pub mod f64 {
    impl ::num::Num2 for f64 {
        #[inline]
        fn from_int2(n: isize) -> f64 { return n as f64;  }
    }
}


