tests/ui/consts/const-extern-fn/issue-68062-const-extern-fns-dont-need-fn-specifier-2.rs
========================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {}

#[cfg(FALSE)]
fn container() {
    const unsafe WhereIsFerris Now() {}
    //~^ ERROR expected one of `extern` or `fn`
}


