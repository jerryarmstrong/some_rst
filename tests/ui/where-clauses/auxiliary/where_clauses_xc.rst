tests/ui/where-clauses/auxiliary/where_clauses_xc.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub trait Equal {
    fn equal(&self, other: &Self) -> bool;
    fn equals<T,U>(&self, this: &T, that: &T, x: &U, y: &U) -> bool
            where T: Eq, U: Eq;
}

impl<T> Equal for T where T: Eq {
    fn equal(&self, other: &T) -> bool {
        self == other
    }
    fn equals<U,X>(&self, this: &U, other: &U, x: &X, y: &X) -> bool
            where U: Eq, X: Eq {
        this == other && x == y
    }
}

pub fn equal<T>(x: &T, y: &T) -> bool where T: Eq {
    x == y
}


