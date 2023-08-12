tests/run-make-fulldeps/inline-always-many-cgu/foo.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "lib"]

pub mod a {
    #[inline(always)]
    pub fn foo() {
    }

    pub fn bar() {
    }
}

#[no_mangle]
pub fn bar() {
    a::foo();
}


