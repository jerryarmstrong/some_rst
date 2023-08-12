tests/ui/nll/user-annotations/pattern_substs_on_brace_struct.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo<'a> { field: &'a u32 }

fn in_let() {
    let y = 22;
    let foo = Foo { field: &y };
    //~^ ERROR `y` does not live long enough
    let Foo::<'static> { field: _z } = foo;
}

fn in_main() {
    let y = 22;
    let foo = Foo { field: &y };
    //~^ ERROR `y` does not live long enough
    match foo {
        Foo::<'static> { field: _z } => {
        }
    }
}

fn main() { }


