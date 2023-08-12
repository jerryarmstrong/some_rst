tests/ui/cross-crate/auxiliary/static_init_aux.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub static V: &u32 = &X;
pub static F: fn() = f;

static X: u32 = 42;

pub fn v() -> *const u32 {
    V
}

fn f() {}


