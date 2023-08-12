tests/ui/consts/const-eval/const_panic_2021.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2021
#![crate_type = "lib"]

const MSG: &str = "hello";

const A: () = std::panic!("blåhaj");
//~^ ERROR evaluation of constant value failed

const B: () = std::panic!();
//~^ ERROR evaluation of constant value failed

const C: () = std::unreachable!();
//~^ ERROR evaluation of constant value failed

const D: () = std::unimplemented!();
//~^ ERROR evaluation of constant value failed

const E: () = std::panic!("{}", MSG);
//~^ ERROR evaluation of constant value failed

const A_CORE: () = core::panic!("shark");
//~^ ERROR evaluation of constant value failed

const B_CORE: () = core::panic!();
//~^ ERROR evaluation of constant value failed

const C_CORE: () = core::unreachable!();
//~^ ERROR evaluation of constant value failed

const D_CORE: () = core::unimplemented!();
//~^ ERROR evaluation of constant value failed

const E_CORE: () = core::panic!("{}", MSG);
//~^ ERROR evaluation of constant value failed


