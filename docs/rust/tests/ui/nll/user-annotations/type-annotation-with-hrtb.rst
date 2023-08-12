tests/ui/nll/user-annotations/type-annotation-with-hrtb.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for issue #69490

// check-pass

pub trait Trait<T> {
    const S: &'static str;
}

impl<T> Trait<()> for T
where
    T: for<'a> Trait<&'a ()>,
{
    // Use of `T::S` here caused an ICE
    const S: &'static str = T::S;
}

// Some similar cases that didn't ICE:

impl<'a, T> Trait<()> for (T,)
where
    T: Trait<&'a ()>,
{
    const S: &'static str = T::S;
}

impl<T> Trait<()> for [T; 1]
where
    T: Trait<for<'a> fn(&'a ())>,
{
    const S: &'static str = T::S;
}

fn main() {}


