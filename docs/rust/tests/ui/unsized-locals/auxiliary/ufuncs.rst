tests/ui/unsized-locals/auxiliary/ufuncs.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(unsized_locals, unsized_fn_params)]

pub fn udrop<T: ?Sized>(_x: T) {}


