tests/ui/numeric/numeric-suffix/numeric-suffix-isize.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

fn foo<N>(_x: N) {}
//~^ NOTE function defined here
//~| NOTE function defined here
//~| NOTE function defined here
//~| NOTE function defined here
//~| NOTE function defined here
//~| NOTE function defined here
//~| NOTE function defined here
//~| NOTE function defined here
//~| NOTE function defined here
//~| NOTE function defined here
//~| NOTE function defined here
//~| NOTE
//~| NOTE
//~| NOTE
//~| NOTE
//~| NOTE
//~| NOTE
//~| NOTE
//~| NOTE
//~| NOTE
//~| NOTE
//~| NOTE

fn main() {
    foo::<isize>(42_usize);
    //~^ ERROR mismatched types
    //~| NOTE expected
    //~| NOTE arguments
    foo::<isize>(42_u64);
    //~^ ERROR mismatched types
    //~| NOTE expected
    //~| NOTE arguments
    foo::<isize>(42_u32);
    //~^ ERROR mismatched types
    //~| NOTE expected
    //~| NOTE arguments
    foo::<isize>(42_u16);
    //~^ ERROR mismatched types
    //~| NOTE expected
    //~| NOTE arguments
    foo::<isize>(42_u8);
    //~^ ERROR mismatched types
    //~| NOTE expected
    //~| NOTE arguments
    foo::<isize>(42_isize);
    foo::<isize>(42_i64);
    //~^ ERROR mismatched types
    //~| NOTE expected
    //~| NOTE arguments
    foo::<isize>(42_i32);
    //~^ ERROR mismatched types
    //~| NOTE expected
    //~| NOTE arguments
    foo::<isize>(42_i16);
    //~^ ERROR mismatched types
    //~| NOTE expected
    //~| NOTE arguments
    foo::<isize>(42_i8);
    //~^ ERROR mismatched types
    //~| NOTE expected
    //~| NOTE arguments
    foo::<isize>(42.0_f64);
    //~^ ERROR mismatched types
    //~| NOTE expected
    //~| NOTE arguments
    foo::<isize>(42.0_f32);
    //~^ ERROR mismatched types
    //~| NOTE expected
    //~| NOTE arguments
}


