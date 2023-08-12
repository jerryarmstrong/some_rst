src/tools/rust-analyzer/crates/parser/test_data/parser/ok/0068_item_modifiers.rs
================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    async fn foo() {}
extern fn foo() {}
const fn foo() {}
const unsafe fn foo() {}
unsafe extern "C" fn foo() {}
unsafe fn foo() {}
async unsafe fn foo() {}
const unsafe fn bar() {}

unsafe trait T {}
auto trait T {}
unsafe auto trait T {}

unsafe impl Foo {}
default impl Foo {}
unsafe default impl Foo {}

unsafe extern "C++" {}


