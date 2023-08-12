tests/ui/inference/need_type_info/expr-struct-type-relative.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // regression test for #98598

trait Foo {
    type Output;

    fn baz() -> Self::Output;
}

fn needs_infer<T>() {}

struct Bar {}

impl Foo for u8 {
    type Output = Bar;
    fn baz() -> Self::Output {
        needs_infer(); //~ ERROR type annotations needed
        Self::Output {}
    }
}

fn main() {}


