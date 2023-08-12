tests/ui/consts/refs_check_const_eq-issue-88384.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(fn_traits)]
#![feature(adt_const_params)]
//~^ WARNING the feature `adt_const_params` is incomplete

#[derive(PartialEq, Eq)]
struct CompileTimeSettings{
    hooks: &'static[fn()],
}

struct Foo<const T: CompileTimeSettings>;
//~^ ERROR using function pointers as const generic parameters is forbidden

impl<const T: CompileTimeSettings> Foo<T> {
    //~^ ERROR using function pointers as const generic parameters is forbidden
    fn call_hooks(){
    }
}

fn main(){
    const SETTINGS: CompileTimeSettings = CompileTimeSettings{
        hooks: &[],
    };

    Foo::<SETTINGS>::call_hooks();
}


