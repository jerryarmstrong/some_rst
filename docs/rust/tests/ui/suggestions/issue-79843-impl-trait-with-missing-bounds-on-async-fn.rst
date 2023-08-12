tests/ui/suggestions/issue-79843-impl-trait-with-missing-bounds-on-async-fn.rs
==============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test: if we suggest replacing an `impl Trait` argument to an async
// fn with a named type parameter in order to add bounds, the suggested function
// signature should be well-formed.
//
// edition:2018

trait Foo {
    type Bar;
    fn bar(&self) -> Self::Bar;
}

async fn run(_: &(), foo: impl Foo) -> std::io::Result<()> {
    let bar = foo.bar();
    assert_is_send(&bar);
//~^ ERROR: `<impl Foo as Foo>::Bar` cannot be sent between threads safely

    Ok(())
}

// Test our handling of cases where there is a generic parameter list in the
// source, but only synthetic generic parameters
async fn run2< >(_: &(), foo: impl Foo) -> std::io::Result<()> {
    let bar = foo.bar();
    assert_is_send(&bar);
//~^ ERROR: `<impl Foo as Foo>::Bar` cannot be sent between threads safely

    Ok(())
}

fn assert_is_send<T: Send>(_: &T) {}

fn main() {}


