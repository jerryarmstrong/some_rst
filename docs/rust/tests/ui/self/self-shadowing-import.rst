tests/ui/self/self-shadowing-import.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

mod a {
    pub mod b {
        pub mod a {
            pub fn foo() -> isize { return 1; }
        }
    }
}

mod c {
    use a::b::a;
    pub fn bar() { assert_eq!(a::foo(), 1); }
}

pub fn main() { c::bar(); }


