tests/ui/associated-type-bounds/traits-assoc-type-macros.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// incremental

// This test case makes sure that we can compile with incremental compilation
// enabled when there are macros, traits, inheritance and associated types involved.

trait Deserializer {
    type Error;
}

trait Deserialize {
    fn deserialize<D>(_: D) -> D::Error
    where
        D: Deserializer;
}

macro_rules! impl_deserialize {
    ($name:ident) => {
        impl Deserialize for $name {
            fn deserialize<D>(_: D) -> D::Error
            where
                D: Deserializer,
            {
                loop {}
            }
        }
    };
}

macro_rules! formats {
    {
        $($name:ident,)*
    } => {
        $(
            pub struct $name;

            impl_deserialize!($name);
        )*
    }
}
formats! { Foo, Bar, }

fn main() {}


