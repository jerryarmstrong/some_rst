tests/ui/did_you_mean/issue-56028-there-is-an-enum-variant.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    enum PutDown { Set }
enum AffixHeart { Set }
enum CauseToBe { Set }
enum Determine { Set }
enum TableDishesAction { Set }
enum Solidify { Set }
enum UnorderedCollection { Set }

fn setup() -> Set { Set }
//~^ ERROR cannot find type `Set` in this scope
//~| ERROR cannot find value `Set` in this scope

fn main() {
    setup();
}


