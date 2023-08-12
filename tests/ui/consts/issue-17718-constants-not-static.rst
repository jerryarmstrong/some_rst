tests/ui/consts/issue-17718-constants-not-static.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn id<T>(x: T) -> T { x }

const FOO: usize = 3;

fn foo() -> &'static usize { &id(FOO) }
//~^ ERROR: cannot return reference to temporary value

fn main() {
}


