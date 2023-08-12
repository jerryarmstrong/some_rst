tests/ui/nll/user-annotations/pattern_substs_on_tuple_enum_variant.rs
=====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    enum Foo<'a> {
    Bar(&'a u32)
}

fn in_let() {
    let y = 22;
    let foo = Foo::Bar(&y);
    //~^ ERROR `y` does not live long enough
    let Foo::Bar::<'static>(_z) = foo;
}

fn in_match() {
    let y = 22;
    let foo = Foo::Bar(&y);
    //~^ ERROR `y` does not live long enough
    match foo {
        Foo::Bar::<'static>(_z) => {
        }
    }
}

fn main() { }


