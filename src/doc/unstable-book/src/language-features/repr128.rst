src/doc/unstable-book/src/language-features/repr128.md
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: md

    # `repr128`

The tracking issue for this feature is: [#56071]

[#56071]: https://github.com/rust-lang/rust/issues/56071

------------------------

The `repr128` feature adds support for `#[repr(u128)]` on `enum`s.

```rust
#![feature(repr128)]

#[repr(u128)]
enum Foo {
    Bar(u64),
}
```


