tests/ui/use/use-from-trait-xc.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:use-from-trait-xc.rs

extern crate use_from_trait_xc;

use use_from_trait_xc::Trait::foo;
//~^ ERROR `foo` is not directly importable

use use_from_trait_xc::Trait::Assoc;
//~^ ERROR `Assoc` is not directly importable

use use_from_trait_xc::Trait::CONST;
//~^ ERROR `CONST` is not directly importable

use use_from_trait_xc::Foo::new; //~ ERROR struct `Foo` is private
//~^ ERROR unresolved import `use_from_trait_xc::Foo`

use use_from_trait_xc::Foo::C; //~ ERROR struct `Foo` is private
//~^ ERROR unresolved import `use_from_trait_xc::Foo`

use use_from_trait_xc::Bar::new as bnew;
//~^ ERROR unresolved import `use_from_trait_xc::Bar`

use use_from_trait_xc::Baz::new as baznew;
//~^ ERROR unresolved import `use_from_trait_xc::Baz::new`

fn main() {}


