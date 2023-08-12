tests/run-make-fulldeps/extern-fn-mangle/test.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[no_mangle]
pub extern "C" fn foo() -> i32 {
    3
}

#[no_mangle]
pub extern "C" fn bar() -> i32 {
    5
}

#[link(name = "test", kind = "static")]
extern "C" {
    fn add() -> i32;
}

fn main() {
    let back = unsafe { add() };
    assert_eq!(8, back);
}


