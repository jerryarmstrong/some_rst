tests/ui/cast/cast-int-to-char.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo<T>(_t: T) {}

fn main() {
    foo::<u32>('0');  //~ ERROR
    foo::<i32>('0');  //~ ERROR
    foo::<u64>('0');  //~ ERROR
    foo::<i64>('0');  //~ ERROR
    foo::<char>(0u32);  //~ ERROR
}


