tests/ui/modules/mod-inside-fn.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn f() -> isize {
    mod m {
        pub fn g() -> isize { 720 }
    }

    m::g()
}

pub fn main() {
    assert_eq!(f(), 720);
}


