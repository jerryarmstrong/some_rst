tests/ui/intrinsics/auxiliary/cci_intrinsic.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(intrinsics)]

pub mod rusti {
    extern "rust-intrinsic" {
        pub fn atomic_xchg_seqcst<T>(dst: *mut T, src: T) -> T;
    }
}

#[inline(always)]
pub fn atomic_xchg_seqcst(dst: *mut isize, src: isize) -> isize {
    unsafe {
        rusti::atomic_xchg_seqcst(dst, src)
    }
}


