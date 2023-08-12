tests/ui/parser/trait-object-polytrait-priority.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(bare_trait_objects)]

trait Trait<'a> {}

fn main() {
    let _: &for<'a> Trait<'a> + 'static;
    //~^ ERROR expected a path on the left-hand side of `+`, not `&for<'a> Trait<'a>`
    //~| HELP try adding parentheses
    //~| SUGGESTION &(for<'a> Trait<'a> + 'static)
}


