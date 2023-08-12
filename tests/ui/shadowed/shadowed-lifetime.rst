tests/ui/shadowed/shadowed-lifetime.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that shadowed lifetimes generate an error.

struct Foo<'a>(&'a isize);

impl<'a> Foo<'a> {
    fn shadow_in_method<'a>(&'a self) -> &'a isize {
        //~^ ERROR lifetime name `'a` shadows a lifetime name that is already in scope
        self.0
    }

    fn shadow_in_type<'b>(&'b self) -> &'b isize {
        let x: for<'b> fn(&'b isize) = panic!();
        //~^ ERROR lifetime name `'b` shadows a lifetime name that is already in scope
        self.0
    }

    fn not_shadow_in_item<'b>(&'b self) {
        struct Bar<'a, 'b>(&'a isize, &'b isize); // not a shadow, separate item
        fn foo<'a, 'b>(x: &'a isize, y: &'b isize) { } // same
    }
}

fn main() {
}


