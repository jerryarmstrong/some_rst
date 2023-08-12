tests/ui/object-lifetime/object-lifetime-default.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(rustc_attrs)]

#[rustc_object_lifetime_default]
struct A<
    T, //~ ERROR BaseDefault
>(T);

#[rustc_object_lifetime_default]
struct B<
    'a,
    T, //~ ERROR BaseDefault
>(&'a (), T);

#[rustc_object_lifetime_default]
struct C<
    'a,
    T: 'a, //~ ERROR 'a
>(&'a T);

#[rustc_object_lifetime_default]
struct D<
    'a,
    'b,
    T: 'a + 'b, //~ ERROR Ambiguous
>(&'a T, &'b T);

#[rustc_object_lifetime_default]
struct E<
    'a,
    'b: 'a,
    T: 'b, //~ ERROR 'b
>(&'a T, &'b T);

#[rustc_object_lifetime_default]
struct F<
    'a,
    'b,
    T: 'a, //~ ERROR 'a
    U: 'b, //~ ERROR 'b
>(&'a T, &'b U);

#[rustc_object_lifetime_default]
struct G<
    'a,
    'b,
    T: 'a,      //~ ERROR 'a
    U: 'a + 'b, //~ ERROR Ambiguous
>(&'a T, &'b U);

fn main() {}


