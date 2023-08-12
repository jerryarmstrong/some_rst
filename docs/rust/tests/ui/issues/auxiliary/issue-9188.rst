tests/ui/issues/auxiliary/issue-9188.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub fn foo<T>() -> &'static isize {
    if false {
        static a: isize = 4;
        return &a;
    } else {
        static a: isize = 5;
        return &a;
    }
}

pub fn bar() -> &'static isize {
    foo::<isize>()
}


