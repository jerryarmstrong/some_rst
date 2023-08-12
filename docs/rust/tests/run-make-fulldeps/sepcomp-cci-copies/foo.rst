tests/run-make-fulldeps/sepcomp-cci-copies/foo.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern crate cci_lib;
use cci_lib::cci_fn;

fn call1() -> usize {
    cci_fn()
}

mod a {
    use cci_lib::cci_fn;
    pub fn call2() -> usize {
        cci_fn()
    }
}

mod b {
    pub fn call3() -> usize {
        0
    }
}

fn main() {
    call1();
    a::call2();
    b::call3();
}


