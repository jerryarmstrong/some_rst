tests/ui/rfc-2565-param-attrs/issue-64682-dropping-first-attrs-in-impl-fns.rs
=============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:param-attrs.rs

// check-pass

extern crate param_attrs;

use param_attrs::rename_params;

#[rename_params(send_help)]
impl Foo {
    fn hello(#[angery(true)] a: i32, #[a2] b: i32, #[what = "how"] c: u32) {}
    fn hello2(#[a1] #[a2] a: i32, #[what = "how"] b: i32, #[angery(true)] c: u32) {}
    fn hello_self(
        #[a1] #[a2] &self,
        #[a1] #[a2] a: i32,
        #[what = "how"] b: i32,
        #[angery(true)] c: u32
    ) {}
}

fn main() {}


