tests/ui/issues/issue-8727.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Verify the compiler fails with an error on infinite function
// recursions.

// build-fail
// normalize-stderr-test: ".nll/" -> "/"

fn generic<T>() { //~ WARN function cannot return without recursing
    generic::<Option<T>>();
}
//~^^ ERROR reached the recursion limit while instantiating `generic::<Option<


fn main () {
    // Use generic<T> at least once to trigger instantiation.
    generic::<i32>();
}


