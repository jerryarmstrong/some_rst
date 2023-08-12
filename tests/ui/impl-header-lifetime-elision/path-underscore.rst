tests/ui/impl-header-lifetime-elision/path-underscore.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that `impl MyTrait for Foo<'_>` works.

// run-pass

#![allow(warnings)]

trait MyTrait { }

struct Foo<'a> { x: &'a u32 }

impl MyTrait for Foo<'_> {
}

fn impls_my_trait<T: MyTrait>() { }

fn impls_my_trait_val<T: MyTrait>(_: T) {
    impls_my_trait::<T>();
}

fn random_where_clause()
where for<'a> Foo<'a>: MyTrait { }

fn main() {
    let x = 22;
    let f = Foo { x: &x };

    // This type is `Foo<'x>` for a local lifetime `'x`; so the impl
    // must apply to any lifetime to apply to this.
    impls_my_trait_val(f);

    impls_my_trait::<Foo<'static>>();

    random_where_clause();
}


