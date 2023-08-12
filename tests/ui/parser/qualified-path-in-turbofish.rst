tests/ui/parser/qualified-path-in-turbofish.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
trait T {
    type Ty;
}

struct Impl;

impl T for Impl {
    type Ty = u32;
}

fn template<T>() -> i64 {
    3
}

fn main() {
    template::<<Impl as T>:Ty>();
    //~^ ERROR found single colon before projection in qualified path
}


