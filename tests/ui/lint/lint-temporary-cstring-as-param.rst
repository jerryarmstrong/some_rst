tests/ui/lint/lint-temporary-cstring-as-param.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(temporary_cstring_as_ptr)]

use std::ffi::CString;
use std::os::raw::c_char;

fn some_function(data: *const c_char) {}

fn main() {
    some_function(CString::new("").unwrap().as_ptr());
    //~^ ERROR getting the inner pointer of a temporary `CString`
}


