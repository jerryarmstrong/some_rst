tests/debuginfo/auxiliary/issue-13213-aux.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "lib"]
// compile-flags:-g

pub use private::P;

#[derive(Copy, Clone)]
pub struct S {
    p: P,
}

mod private {
    #[derive(Copy, Clone)]
    pub struct P {
        p: i32,
    }
    pub const THREE: P = P { p: 3 };
}

pub static A: S = S { p: private::THREE };


