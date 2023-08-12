src/tools/rustfmt/tests/source/configs/type_punctuation_density/compressed.rs
=============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-type_punctuation_density: Compressed
// Type punctuation density

fn lorem<Ipsum:Dolor+Sit=Amet>() {
    // body
}

struct Foo<T: Eq + Clone, U>
where U: Eq + Clone {
    // body
}

trait Foo<'a, T = usize>
where T: 'a + Eq + Clone
{
    type Bar: Eq + Clone;
}

trait Foo: Eq + Clone {
    // body
}

impl<T> Foo<'a> for Bar
where for<'a> T: 'a + Eq + Clone
{
    // body
}

fn foo<'a, 'b, 'c>()
where 'a: 'b + 'c
{
    // body
}

fn Foo<T = Foo, Output = Expr<'tcx> + Foo>() {
    let i = 6;
}


