tests/ui/type-inference/unbounded-type-param-in-fn.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo<T>() -> T {
    panic!()
}

fn main() {
    foo(); //~ ERROR type annotations needed
}


