src/tools/rust-analyzer/crates/parser/test_data/parser/ok/0042_ufcs_call_list.rs
================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // https://github.com/rust-lang/rust-analyzer/issues/596

struct Foo;

impl Foo {
    fn bar() -> bool {
        unimplemented!()
    }
}

fn baz(_: bool) {}

fn main() {
    baz(<Foo>::bar())
}


