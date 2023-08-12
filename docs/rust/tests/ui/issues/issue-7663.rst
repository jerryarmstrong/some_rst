tests/ui/issues/issue-7663.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(unused_imports, dead_code)]

mod test1 {

    mod foo { pub fn p() -> isize { 1 } }
    mod bar { pub fn p() -> isize { 2 } }

    pub mod baz {
        use test1::bar::p;

        pub fn my_main() { assert_eq!(p(), 2); }
    }
}

mod test2 {

    mod foo { pub fn p() -> isize { 1 } }
    mod bar { pub fn p() -> isize { 2 } }

    pub mod baz {
        use test2::bar::p;

        pub fn my_main() { assert_eq!(p(), 2); }
    }
}

fn main() {
    test1::baz::my_main();
    test2::baz::my_main();
}


