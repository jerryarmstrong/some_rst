tests/ui/regions/regions-close-param-into-object.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait X { fn foo(&self) {} }

fn p1<T>(v: T) -> Box<dyn X + 'static>
    where T : X
{
    Box::new(v) //~ ERROR parameter type `T` may not live long enough
}

fn p2<T>(v: Box<T>) -> Box<dyn X + 'static>
    where Box<T> : X
{
    Box::new(v) //~ ERROR parameter type `T` may not live long enough
}

fn p3<'a,T>(v: T) -> Box<dyn X + 'a>
    where T : X
{
    Box::new(v) //~ ERROR parameter type `T` may not live long enough
}

fn p4<'a,T>(v: Box<T>) -> Box<dyn X + 'a>
    where Box<T> : X
{
    Box::new(v) //~ ERROR parameter type `T` may not live long enough
}

fn main() {}


