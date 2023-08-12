tests/ui/lint/lint-forbid-internal-unsafe.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![forbid(unsafe_code)]
#![feature(allow_internal_unsafe)]

#[allow_internal_unsafe]
//~^ ERROR: `allow_internal_unsafe` allows defining
macro_rules! evil {
    ($e:expr) => {
        unsafe {
            $e
        }
    }
}

fn main() {
    println!("{}", evil!(*(0 as *const u8)));
    //~^ WARNING dereferencing a null pointer
}


