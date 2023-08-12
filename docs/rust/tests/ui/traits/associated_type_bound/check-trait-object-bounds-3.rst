tests/ui/traits/associated_type_bound/check-trait-object-bounds-3.rs
====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that we validate associated type bounds for trait objects

trait X<'a> {
    type Y: Into<&'static str> + From<&'a str>;
}

fn f<'a, T: X<'a> + ?Sized>(s: &'a str) -> &'static str {
    T::Y::from(s).into()
}

pub fn main() {
    let z;
    {
        let s = String::from("abcdef");
        z = f::<dyn X<Y = &str>>(&s);
        //~^ ERROR `s` does not live long enough
    }

    println!("{}", z)
}


