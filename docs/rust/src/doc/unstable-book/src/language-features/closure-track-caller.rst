src/doc/unstable-book/src/language-features/closure-track-caller.md
===================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: md

    # `closure_track_caller`

The tracking issue for this feature is: [#87417]

[#87417]: https://github.com/rust-lang/rust/issues/87417

------------------------

Allows using the `#[track_caller]` attribute on closures and generators.
Calls made to the closure or generator will have caller information
available through `std::panic::Location::caller()`, just like using
`#[track_caller]` on a function.


