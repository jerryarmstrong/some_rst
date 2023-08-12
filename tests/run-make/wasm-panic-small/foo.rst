tests/run-make/wasm-panic-small/foo.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "cdylib"]

#[no_mangle]
#[cfg(a)]
pub fn foo() {
    panic!("test");
}

#[no_mangle]
#[cfg(b)]
pub fn foo() {
    panic!("{}", 1);
}

#[no_mangle]
#[cfg(c)]
pub fn foo() {
    panic!("{}", "a");
}

#[no_mangle]
#[cfg(d)]
pub fn foo() -> usize {
    use std::cell::Cell;
    thread_local!(static A: Cell<Vec<u32>> = Cell::new(Vec::new()));
    A.try_with(|x| x.take().len()).unwrap_or(0)
}


