tests/ui/lifetimes/copy_modulo_regions.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[derive(Clone)]
struct Foo<'a>(fn(&'a ()) -> &'a ());

impl Copy for Foo<'static> {}

fn mk_foo<'a>() -> Foo<'a> {
    println!("mk_foo");
    Foo(|x| x)
}

fn foo<'a>() -> [Foo<'a>; 100] {
    [mk_foo::<'a>(); 100] //~ ERROR lifetime may not live long enough
}

fn main() {
    foo();
}


