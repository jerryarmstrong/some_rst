tests/rustdoc/stability.rs
==========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(staged_api)]

#![unstable(feature = "test", issue = "none")]

pub struct Unstable {
    // @has stability/struct.Unstable.html \
    //      '//span[@class="item-info"]//div[@class="stab unstable"]' \
    //      'This is a nightly-only experimental API'
    // @count stability/struct.Unstable.html '//span[@class="stab unstable"]' 0
    pub foo: u32,
    pub bar: u32,
}


