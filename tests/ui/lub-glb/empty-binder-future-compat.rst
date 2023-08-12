tests/ui/lub-glb/empty-binder-future-compat.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
fn lt_in_fn_fn<'a: 'a>() -> fn(fn(&'a ())) {
    |_| ()
}


fn foo<'a, 'b, 'lower>(v: bool)
where
    'a: 'lower,
    'b: 'lower,
{
        // if we infer `x` to be higher ranked in the future,
        // this would cause a type error.
        let x = match v {
            true => lt_in_fn_fn::<'a>(),
            false => lt_in_fn_fn::<'b>(),
        };

        let _: fn(fn(&'lower())) = x;
}

fn main() {}


