tests/ui/traits/privacy.rs
==========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass (FIXME(62277): could be check-pass?)
#![allow(dead_code)]
mod foo {
    pub use self::bar::T;
    mod bar {
        pub trait T {
            fn f(&self) {}
        }
        impl T for () {}
    }
}

fn g() {
    use foo::T;
    ().f(); // Check that this does not trigger a privacy error
}

fn f() {
    let error = ::std::thread::spawn(|| {}).join().unwrap_err();
    error.type_id(); // Regression test for #21670
}


fn main() {}


