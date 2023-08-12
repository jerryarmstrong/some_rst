src/tools/miri/tests/fail/function_calls/exported_symbol_clashing.rs
====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[no_mangle]
fn foo() {}
//~^ HELP: it's first defined here, in crate `exported_symbol_clashing`

#[export_name = "foo"]
fn bar() {}
//~^ HELP: then it's defined here again, in crate `exported_symbol_clashing`

fn main() {
    extern "Rust" {
        fn foo();
    }
    unsafe { foo() }
    //~^ ERROR: multiple definitions of symbol `foo`
}


