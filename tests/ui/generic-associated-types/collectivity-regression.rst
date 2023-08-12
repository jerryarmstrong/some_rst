tests/ui/generic-associated-types/collectivity-regression.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test from https://github.com/rust-lang/rust/pull/98109

pub trait Get {
    type Value<'a>
    where
        Self: 'a;
}

fn multiply_at<T>(x: T)
where
    for<'a> T: Get<Value<'a> = ()>,
{
    || {
        //~^ `T` does not live long enough
        //
        // FIXME(#98437). This regressed at some point and
        // probably should work.
        let _x = x;
    };
}

fn main() {}


