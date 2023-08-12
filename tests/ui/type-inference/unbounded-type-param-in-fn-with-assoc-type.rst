tests/ui/type-inference/unbounded-type-param-in-fn-with-assoc-type.rs
=====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[allow(invalid_type_param_default)]

fn foo<T, U = u64>() -> (T, U) {
    panic!()
}

fn main() {
    foo(); //~ ERROR type annotations needed
}


