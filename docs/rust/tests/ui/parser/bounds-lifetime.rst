tests/ui/parser/bounds-lifetime.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    type A = for<'a:> fn(); // OK
type A = for<'a:,> fn(); // OK
type A = for<'a> fn(); // OK
type A = for<> fn(); // OK
type A = for<'a: 'b + 'c> fn(); // OK (rejected later by ast_validation)
type A = for<'a: 'b,> fn(); // OK(rejected later by ast_validation)
type A = for<'a: 'b +> fn(); // OK (rejected later by ast_validation)
type A = for<'a, T> fn(); // OK (rejected later by ast_validation)
type A = for<,> fn(); //~ ERROR expected one of `#`, `>`, `const`, identifier, or lifetime

fn main() {}


