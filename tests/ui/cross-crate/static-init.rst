tests/ui/cross-crate/static-init.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:static_init_aux.rs
extern crate static_init_aux as aux;

static V: &u32 = aux::V;
static F: fn() = aux::F;

fn v() -> *const u32 {
    V
}

fn main() {
    assert_eq!(aux::v(), crate::v());
    F();
}


