tests/ui/imports/glob-shadowing.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(decl_macro)]

mod m {
    pub macro env($e: expr) { $e }
    pub macro fenv() { 0 }
}

mod glob_in_normal_module {
    use m::*;
    fn check() {
        let x = env!("PATH"); //~ ERROR `env` is ambiguous
    }
}

mod glob_in_block_module {
    fn block() {
        use m::*;
        fn check() {
            let x = env!("PATH"); //~ ERROR `env` is ambiguous
        }
    }
}

mod glob_shadows_item {
    pub macro fenv($e: expr) { $e }
    fn block() {
        use m::*;
        fn check() {
            let x = fenv!(); //~ ERROR `fenv` is ambiguous
        }
    }
}

fn main() {}


