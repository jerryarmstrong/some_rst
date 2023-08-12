tests/ui/issues/issue-3680.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    match None {
        Err(_) => ()
        //~^ ERROR mismatched types
        //~| expected enum `Option<_>`
        //~| found enum `Result<_, _>`
        //~| expected enum `Option`, found enum `Result`
    }
}


