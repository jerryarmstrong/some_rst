tests/rustdoc-ui/search-index-generics-recursion-bug-issue-59502.rs
===================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

// Minimization of issue #59502

trait MyTrait<T> {
    type Output;
}

pub fn pow<T: MyTrait<T, Output = T>>(arg: T) -> T {
    arg
}


