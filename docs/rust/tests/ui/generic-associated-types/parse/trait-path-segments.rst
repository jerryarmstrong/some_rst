tests/ui/generic-associated-types/parse/trait-path-segments.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    const _: () = {
    trait X {
        type Y<'a>;
    }

    fn f1<'a>(arg : Box<dyn X<X::Y = u32>>) {}
        //~^ ERROR: expected one of
  };

const _: () = {
    trait X {
        type Y<'a>;
    }

    trait Z {}

    impl<T : X<<Self as X>::Y<'a> = &'a u32>> Z for T {}
        //~^ ERROR: expected one of
};

const _: () = {
    trait X {
      type Y<'a>;
    }

    trait Z {}

    impl<T : X<X::Y<'a> = &'a u32>> Z for T {}
        //~^ ERROR: expected one of
};

fn main() {}


