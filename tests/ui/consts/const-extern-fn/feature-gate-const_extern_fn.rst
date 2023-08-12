tests/ui/consts/const-extern-fn/feature-gate-const_extern_fn.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that `const extern fn` and `const unsafe extern fn` are feature-gated
// for certain ABIs.

const extern fn foo1() {}
const extern "C" fn foo2() {}
const extern "Rust" fn foo3() {}
const extern "cdecl" fn foo4() {} //~ ERROR `cdecl` as a `const fn` ABI is unstable
const unsafe extern fn bar1() {}
const unsafe extern "C" fn bar2() {}
const unsafe extern "Rust" fn bar3() {}
const unsafe extern "cdecl" fn bar4() {} //~ ERROR `cdecl` as a `const fn` ABI is unstable

fn main() {}


