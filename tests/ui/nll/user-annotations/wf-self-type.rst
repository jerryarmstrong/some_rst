tests/ui/nll/user-annotations/wf-self-type.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo<'a, 'b: 'a>(&'a &'b ());

impl<'a, 'b> Foo<'a, 'b> {
    fn xmute(a: &'b ()) -> &'a () {
        unreachable!()
    }
}

pub fn foo<'a, 'b>(u: &'b ()) -> &'a () {
    Foo::xmute(u) //~ ERROR lifetime may not live long enough
}

fn main() {}


