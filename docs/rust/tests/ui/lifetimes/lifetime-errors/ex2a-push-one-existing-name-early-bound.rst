tests/ui/lifetimes/lifetime-errors/ex2a-push-one-existing-name-early-bound.rs
=============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Foo<'a> {}
impl<'a, T> Foo<'a> for T {}

fn baz<'a, 'b, T>(x: &mut Vec<&'a T>, y: &T)
    where i32: Foo<'a>,
          u32: Foo<'b>
{
    x.push(y); //~ ERROR explicit lifetime required
}
fn main() {
}


