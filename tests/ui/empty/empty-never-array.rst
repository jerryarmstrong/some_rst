tests/ui/empty/empty-never-array.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(never_type)]

enum Helper<T, U> {
    T(T, [!; 0]),
    #[allow(dead_code)]
    U(U),
}

fn transmute<T, U>(t: T) -> U {
    let Helper::U(u) = Helper::T(t, []);
    //~^ ERROR refutable pattern in local binding
    //~| `Helper::T(_, _)` not covered
    u
}

fn main() {
    println!("{:?}", transmute::<&str, (*const u8, u64)>("type safety"));
}


