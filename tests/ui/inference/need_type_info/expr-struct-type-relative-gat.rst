tests/ui/inference/need_type_info/expr-struct-type-relative-gat.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Foo {
    type Output<T>;

    fn baz();
}

enum Bar<T> {
    Simple {},
    Generic(T),
}

impl Foo for u8 {
    type Output<T> = Bar<T>;
    fn baz() {
        Self::Output::Simple {}; //~ ERROR type annotations needed
    }
}

fn main() {}


