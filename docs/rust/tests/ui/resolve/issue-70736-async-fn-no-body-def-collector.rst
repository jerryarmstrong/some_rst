tests/ui/resolve/issue-70736-async-fn-no-body-def-collector.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018

async fn free(); //~ ERROR without a body

struct A;
impl A {
    async fn inherent(); //~ ERROR without body
}

trait B {
    async fn associated();
    //~^ ERROR cannot be declared `async`
}
impl B for A {
    async fn associated(); //~ ERROR without body
    //~^ ERROR cannot be declared `async`
}

fn main() {}


