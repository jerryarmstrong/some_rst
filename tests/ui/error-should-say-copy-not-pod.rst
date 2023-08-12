tests/ui/error-should-say-copy-not-pod.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Tests that the error message uses the word Copy, not Pod.

fn check_bound<T:Copy>(_: T) {}

fn main() {
    check_bound("nocopy".to_string()); //~ ERROR : Copy` is not satisfied
}


