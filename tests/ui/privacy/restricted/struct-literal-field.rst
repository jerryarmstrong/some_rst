tests/ui/privacy/restricted/struct-literal-field.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(warnings)]

mod foo {
    pub mod bar {
        pub struct S {
            pub(in foo) x: i32,
        }
    }

    fn f() {
        use foo::bar::S;
        S { x: 0 }; // ok
    }
}

fn main() {
    use foo::bar::S;
    S { x: 0 }; //~ ERROR private
}


