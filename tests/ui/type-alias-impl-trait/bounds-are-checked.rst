tests/ui/type-alias-impl-trait/bounds-are-checked.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Make sure that we check that impl trait types implement the traits that they
// claim to.

#![feature(type_alias_impl_trait)]

type X<'a> = impl Into<&'static str> + From<&'a str>;

fn f<'a: 'static>(t: &'a str) -> X<'a> {
    //~^ WARNING unnecessary lifetime parameter
    t
    //~^ ERROR non-defining opaque type use
}

fn extend_lt<'a>(o: &'a str) -> &'static str {
    X::<'_>::from(o).into()
}

fn main() {
    let r = {
        let s = "abcdef".to_string();
        extend_lt(&s)
    };
    println!("{}", r);
}


