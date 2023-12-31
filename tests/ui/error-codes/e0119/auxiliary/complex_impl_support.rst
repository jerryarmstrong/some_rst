tests/ui/error-codes/e0119/auxiliary/complex_impl_support.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::marker::PhantomData;

pub trait External {}

pub struct M<'a, 'b, 'c, T, U, V> {
    a: PhantomData<&'a ()>,
    b: PhantomData<&'b ()>,
    c: PhantomData<&'c ()>,
    d: PhantomData<T>,
    e: PhantomData<U>,
    f: PhantomData<V>,
}

impl<'a, 'b, 'c, T, U, V, W> External for (T, M<'a, 'b, 'c, Box<U>, V, W>)
where
    'b: 'a,
    T: 'a,
    U: (FnOnce(T) -> V) + 'static,
    V: Iterator<Item=T> + Clone,
    W: std::ops::Add,
    W::Output: Copy,
{}


