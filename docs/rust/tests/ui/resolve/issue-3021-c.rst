tests/ui/resolve/issue-3021-c.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn siphash<T>() {

    trait U {
        fn g(&self, x: T) -> T;  //~ ERROR can't use generic parameters from outer function
        //~^ ERROR can't use generic parameters from outer function
    }
}

fn main() {}


