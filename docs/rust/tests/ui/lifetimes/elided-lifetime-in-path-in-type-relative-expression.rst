tests/ui/lifetimes/elided-lifetime-in-path-in-type-relative-expression.rs
=========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

struct Sqlite {}

trait HasArguments<'q> {
    type Arguments;
}

impl<'q> HasArguments<'q> for Sqlite {
    type Arguments = std::marker::PhantomData<&'q ()>;
}

fn foo() {
    let _ = <Sqlite as HasArguments>::Arguments::default();
}

fn main() {}


