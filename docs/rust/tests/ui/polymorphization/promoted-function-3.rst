tests/ui/polymorphization/promoted-function-3.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// compile-flags: -Zpolymorphize=on -Zmir-opt-level=4

fn caller<T, U>() -> &'static usize {
    callee::<U>()
}

fn callee<T>() -> &'static usize {
    &std::mem::size_of::<T>()
}

fn main() {
    assert_eq!(caller::<(), ()>(), &0);
}


