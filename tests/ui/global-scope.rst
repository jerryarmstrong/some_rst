tests/ui/global-scope.rs
========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

pub fn f() -> isize { return 1; }

pub mod foo {
    pub fn f() -> isize { return 2; }
    pub fn g() {
        assert_eq!(f(), 2);
        assert_eq!(::f(), 1);
    }
}

pub fn main() { return foo::g(); }


