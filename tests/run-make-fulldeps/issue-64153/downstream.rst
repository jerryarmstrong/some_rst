tests/run-make-fulldeps/issue-64153/downstream.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern crate upstream;

#[no_mangle]
pub extern "C" fn foo() {
    print!("1 + 1 = {}", upstream::issue64153_test_function(1));
}


