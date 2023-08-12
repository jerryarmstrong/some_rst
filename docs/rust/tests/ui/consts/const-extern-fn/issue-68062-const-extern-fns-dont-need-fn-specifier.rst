tests/ui/consts/const-extern-fn/issue-68062-const-extern-fns-dont-need-fn-specifier.rs
======================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {}

#[cfg(FALSE)]
fn container() {
    const extern "Rust" PUT_ANYTHING_YOU_WANT_HERE bug() -> usize { 1 }
    //~^ ERROR expected `fn`
}


