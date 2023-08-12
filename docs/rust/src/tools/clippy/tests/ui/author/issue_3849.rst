src/tools/clippy/tests/ui/author/issue_3849.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(dead_code)]
#![allow(clippy::zero_ptr)]
#![allow(clippy::transmute_ptr_to_ref)]
#![allow(clippy::transmuting_null)]

pub const ZPTR: *const usize = 0 as *const _;

fn main() {
    unsafe {
        #[clippy::author]
        let _: &i32 = std::mem::transmute(ZPTR);
        let _: &i32 = std::mem::transmute(0 as *const i32);
    }
}


