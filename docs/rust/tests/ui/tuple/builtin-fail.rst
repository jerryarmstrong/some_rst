tests/ui/tuple/builtin-fail.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(tuple_trait)]

fn assert_is_tuple<T: std::marker::Tuple + ?Sized>() {}

struct TupleStruct(i32, i32);

fn from_param_env<T>() {
    assert_is_tuple::<T>();
    //~^ ERROR `T` is not a tuple
}

fn main() {
    assert_is_tuple::<i32>();
    //~^ ERROR `i32` is not a tuple
    assert_is_tuple::<(i32)>();
    //~^ ERROR `i32` is not a tuple
    assert_is_tuple::<TupleStruct>();
    //~^ ERROR `TupleStruct` is not a tuple
}


