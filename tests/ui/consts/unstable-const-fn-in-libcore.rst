tests/ui/consts/unstable-const-fn-in-libcore.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This is a non-regression test for const-qualification of unstable items in libcore
// as explained in issue #67053.
// const-qualification could miss some `const fn`s if they were unstable and the feature
// gate was not enabled in libcore.

#![stable(feature = "core", since = "1.6.0")]
#![feature(staged_api, const_trait_impl)]

enum Opt<T> {
    Some(T),
    None,
}

impl<T> Opt<T> {
    #[rustc_const_unstable(feature = "foo", issue = "none")]
    #[stable(feature = "rust1", since = "1.0.0")]
    const fn unwrap_or_else<F: ~const FnOnce() -> T>(self, f: F) -> T {
    //~^ ERROR destructor of
    //~| ERROR destructor of
        match self {
            Opt::Some(t) => t,
            Opt::None => f(),
        }
    }
}

fn main() {}


