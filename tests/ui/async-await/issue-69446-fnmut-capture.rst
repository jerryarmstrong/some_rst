tests/ui/async-await/issue-69446-fnmut-capture.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for issue #69446 - we should display
// which variable is captured
// edition:2018

use core::future::Future;

struct Foo;
impl Foo {
    fn foo(&mut self) {}
}

async fn bar<T>(_: impl FnMut() -> T)
where
    T: Future<Output = ()>,
{}

fn main() {
    let mut x = Foo;
    bar(move || async { //~ ERROR captured
        x.foo();
    });
}


