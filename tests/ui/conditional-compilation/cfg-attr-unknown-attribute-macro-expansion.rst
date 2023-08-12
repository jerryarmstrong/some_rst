tests/ui/conditional-compilation/cfg-attr-unknown-attribute-macro-expansion.rs
==============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    macro_rules! foo {
    () => {
        #[cfg_attr(all(), unknown)]
        //~^ ERROR cannot find attribute `unknown` in this scope
        fn foo() {}
    }
}

foo!();

fn main() {}


